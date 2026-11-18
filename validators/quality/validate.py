"""Check changed Python files and release notes against a Git baseline."""

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys

RUFF_VERSION = "0.14.14"
CHANGELOG = "CHANGELOG.md"
EXEMPT_PREFIXES = ("specs/changes/", "specs/archive/", "tests/", "docs/validation/")
UNRELEASED = "## [Unreleased]"
NOTE = re.compile(r"^[-*+]\s+(\S.*)$")
GIT_OID = re.compile(r"(?:[a-f0-9]{40}|[a-f0-9]{64})")


def git(root: Path, *args: str) -> bytes:
    result = subprocess.run(
        ["git", *args], cwd=root, stdin=subprocess.DEVNULL, capture_output=True
    )
    if result.returncode:
        raise ValueError(
            f"Git could not run {args[0]}: {os.fsdecode(result.stderr).strip()}"
        )
    return result.stdout


def commit(root: Path, ref: str) -> str:
    try:
        return (
            git(root, "rev-parse", "--verify", "--end-of-options", f"{ref}^{{commit}}")
            .decode()
            .strip()
        )
    except ValueError as exc:
        raise ValueError(
            f"Comparison revision {ref!r} is unavailable. Fetch the required "
            "Git history or select an available base locally."
        ) from exc


def event_oid(value: str) -> str:
    if not GIT_OID.fullmatch(value):
        raise ValueError("Expected a full Git object ID in the GitHub event payload.")
    return value


def event_base(root: Path, event_name: str, payload: dict) -> str:
    head = commit(root, "HEAD")
    if event_name == "pull_request":
        pull = payload["pull_request"]
        base = commit(root, event_oid(pull["base"]["sha"]))
        source = commit(root, event_oid(pull["head"]["sha"]))
        parents = git(root, "show", "-s", "--format=%P", head).decode().split()
        if parents != [base, source]:
            raise ValueError("Check out the GitHub PR merge revision for this event.")
        return base
    if event_name != "push" or not payload["ref"].startswith("refs/heads/"):
        raise ValueError("Quality comparison expects a branch push or pull request.")
    if head != event_oid(payload["after"]):
        raise ValueError("Check out the pushed tip supplied by GitHub.")
    before = event_oid(payload["before"])
    if before.strip("0"):
        return commit(root, before)
    default_name = payload["repository"]["default_branch"]
    default = f"refs/remotes/origin/{default_name}"
    if not payload.get("created"):
        raise ValueError("The push lacks a usable before revision.")
    on_default = payload["ref"] == f"refs/heads/{default_name}"
    if on_default:
        if not git(root, "show", "-s", "--format=%P", head).strip():
            return git(root, "hash-object", "-t", "tree", "--stdin").decode().strip()
    default_commit = commit(root, default)
    if on_default and default_commit == head:
        raise ValueError("The initial push has no independent comparison base.")
    try:
        return git(root, "merge-base", default_commit, head).decode().strip()
    except ValueError as exc:
        raise ValueError(
            f"No merge base with {default!r}. Fetch the default branch and full history."
        ) from exc


def validate_path(name: str) -> Path:
    path = Path(name)
    if path.is_absolute() or not path.parts or ".." in path.parts:
        raise ValueError(f"Unsafe Git path: {name!r}")
    if any(ord(char) < 32 or ord(char) == 127 for char in name):
        raise ValueError(f"Unsupported control character in path: {name!r}")
    return path


def regular_file(root: Path, name: str) -> Path:
    path = root
    for part in validate_path(name).parts:
        path = path / part
        if path.is_symlink():
            raise ValueError(f"Symlink is not allowed as a quality input: {name!r}")
    if not path.is_file():
        raise ValueError(f"Expected a regular file: {name!r}")
    return path


def changed_paths(root: Path, base: str) -> tuple[set[str], set[str]]:
    data = git(
        root,
        "diff",
        "--no-ext-diff",
        "--ignore-submodules=none",
        "--name-status",
        "-z",
        "--find-renames",
        base,
        "--",
    )
    entries = iter(os.fsdecode(data).split("\0")[:-1])
    affected, python_files = set(), set()
    for status in entries:
        if status.startswith(("U", "X", "B")):
            raise ValueError(
                f"Resolve the incomplete Git change with status {status!r}."
            )
        name = next(entries)
        validate_path(name)
        affected.add(name)
        if status.startswith(("R", "C")):
            name = next(entries)
            validate_path(name)
            affected.add(name)
        if not status.startswith("D") and Path(name).suffix in {".py", ".pyi"}:
            python_files.add(name)
    return affected, python_files


def changelog_notes(content: str) -> tuple[set[str], set[str], int]:
    notes, unreleased = set(), set()
    heading = ""
    count = 0
    fence = ""
    comment = False
    for line in content.splitlines():
        if comment:
            comment = "-->" not in line
            continue
        if line.lstrip().startswith("<!--"):
            comment = "-->" not in line
            continue
        token = re.match(r"^\s*(`{3,}|~{3,})", line)
        if token and (not fence or token[1].startswith(fence)):
            fence = "" if fence else token[1]
            continue
        if fence:
            continue
        if title := re.match(r"^ {0,3}##\s+(.+?)\s*$", line):
            heading = "## " + re.sub(r"\s+#+$", "", title[1])
            count += heading == UNRELEASED
        elif match := NOTE.match(line):
            note = " ".join(match[1].split()).casefold()
            notes.add(note)
            if heading == UNRELEASED:
                unreleased.add(note)
    return notes, unreleased, count


def check_changelog(root: Path, base: str, affected: set[str]) -> None:
    required = sorted(
        path
        for path in affected
        if path != CHANGELOG and not path.startswith(EXEMPT_PREFIXES)
    )
    if not required:
        print(
            "Changelog: exempt (only changelog, SDD, tests or internal evidence, or no diff)."
        )
        return
    print(f"Changelog: required by {len(required)} path(s), including {required[0]!r}.")
    if CHANGELOG not in affected:
        raise ValueError(f"Add a new entry under {UNRELEASED} in {CHANGELOG}.")
    current = regular_file(root, CHANGELOG).read_text(encoding="utf-8")
    _, new_notes, sections = changelog_notes(current)
    if sections != 1:
        raise ValueError(f"{CHANGELOG} must have exactly one {UNRELEASED} section.")
    entry = git(root, "ls-tree", base, "--", CHANGELOG)
    if entry and not entry.startswith((b"100644 blob ", b"100755 blob ")):
        raise ValueError(f"Base {CHANGELOG} must be a regular file.")
    old = git(root, "show", f"{base}:{CHANGELOG}").decode() if entry else ""
    old_notes, _, _ = changelog_notes(old)
    if not new_notes - old_notes:
        raise ValueError(f"Add a new entry under {UNRELEASED} in {CHANGELOG}.")
    print("Changelog: found a new Unreleased entry.")


def check_python(root: Path, paths: set[str]) -> bool:
    ruff = [sys.executable, "-I", "-B", "-m", "ruff"]
    version = subprocess.run(
        [*ruff, "--version"], cwd=root, capture_output=True, text=True
    )
    if version.returncode or version.stdout.strip() != f"ruff {RUFF_VERSION}":
        raise ValueError(
            f"Install Ruff {RUFF_VERSION} from requirements-validation.txt."
        )
    if not paths:
        print("Ruff: no changed Python sources.")
        return True
    config = regular_file(root, "ruff.toml")
    files = [str(regular_file(root, name)) for name in sorted(paths)]
    print(f"Ruff: checking {len(files)} changed Python source file(s).", flush=True)
    passed = True
    for start in range(0, len(files), 32):
        for command in (
            ("check", "--no-fix", "--select", "E4,E7,E9,F"),
            ("format", "--check"),
        ):
            result = subprocess.run(
                [
                    *ruff,
                    *command,
                    "--no-cache",
                    "--config",
                    str(config),
                    "--force-exclude",
                    "--",
                    *files[start : start + 32],
                ],
                cwd=root,
            )
            passed &= result.returncode == 0
    return passed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--base")
    source.add_argument("--github-event", type=Path)
    args = parser.parse_args()
    try:
        root = args.root.resolve(strict=True)
        if (
            Path(os.fsdecode(git(root, "rev-parse", "--show-toplevel").rstrip(b"\n")))
            != root
        ):
            raise ValueError("Run quality validation at the Git repository root.")
        if args.github_event:
            payload = json.loads(args.github_event.read_text(encoding="utf-8"))
            base = event_base(root, os.environ.get("GITHUB_EVENT_NAME", ""), payload)
        else:
            base = commit(root, args.base)
        print(f"Quality comparison base: {base}", flush=True)
        affected, files = changed_paths(root, base)
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(f"Quality validation failed: {exc}", file=sys.stderr)
        return 1

    passed = True
    try:
        check_changelog(root, base, affected)
    except (ValueError, OSError) as exc:
        print(f"Changelog validation failed: {exc}", file=sys.stderr)
        passed = False
    try:
        passed &= check_python(root, files)
    except (ValueError, OSError) as exc:
        print(f"Python quality validation failed: {exc}", file=sys.stderr)
        passed = False
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
