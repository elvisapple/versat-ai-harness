#!/usr/bin/env python3
"""Validate versioned SDD documents without performing Git or network operations."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

try:
    import yaml
    from jsonschema import Draft202012Validator
    from referencing import Registry, Resource
except ImportError as exc:
    DEPENDENCY_ERROR = str(exc)
else:
    DEPENDENCY_ERROR = None

ARTIFACTS = ("proposal", "requirements", "design", "tasks")
STAGES = ("proposal", "design", "tasks")
PHASES = ("planning", "implementation", "delivery")
CHANGE_ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DIGEST = re.compile(r"^[a-f0-9]{64}$")
SCHEMA_ROOT = Path(__file__).resolve().parents[2] / "sdd" / "schemas"
BOOKKEEPING = {"Planning review", "Validation evidence", "Progress", "Delivery"}
CHECKBOX = re.compile(r"^\s*[-*+]\s+\[([ xX])\]\s+(TASK-[0-9]{3,})\b", re.MULTILINE)


if DEPENDENCY_ERROR is None:
    class UniqueKeyLoader(yaml.SafeLoader):
        """Reject duplicate YAML fields instead of silently accepting the last one."""

        def construct_mapping(self, node, deep=False):
            self.flatten_mapping(node)
            mapping = {}
            for key_node, value_node in node.value:
                key = self.construct_object(key_node, deep=deep)
                if not isinstance(key, str):
                    raise ValueError("YAML mapping keys must be strings")
                if key in mapping:
                    raise ValueError(f"Duplicate YAML key: {key}")
                mapping[key] = self.construct_object(value_node, deep=deep)
            return mapping


def _dependencies():
    if DEPENDENCY_ERROR:
        raise ValueError(
            "Missing validation dependency: " + DEPENDENCY_ERROR
            + ". Install requirements-validation.txt using Python 3.11 or newer."
        )


def _json(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False)


def _read_artifact(path):
    _dependencies()
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    lines = text.splitlines()
    if not lines or lines[0].rstrip() != "---":
        raise ValueError("Expected YAML frontmatter beginning on the first line")
    try:
        end = next(index for index, line in enumerate(lines[1:], 1) if line.rstrip() == "---")
    except ValueError as exc:
        raise ValueError("Missing closing YAML frontmatter delimiter") from exc
    metadata = yaml.load("\n".join(lines[1:end]), Loader=UniqueKeyLoader)
    if not isinstance(metadata, dict):
        raise ValueError("Frontmatter must be a mapping")
    _json(metadata)  # Reject cycles, timestamps, non-finite numbers and non-JSON values.
    return {"metadata": metadata, "body": "\n".join(lines[end + 1:]), "path": path}


def _normalized_body(body):
    lines = []
    bookkeeping = False
    fence = None
    for raw in body.splitlines():
        line = raw.rstrip()
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            value = marker.group(1)
            if fence is None:
                fence = (value[0], len(value))
            elif value[0] == fence[0] and len(value) >= fence[1]:
                fence = None
        if fence is None and line.startswith("## "):
            bookkeeping = line[3:].strip() in BOOKKEEPING
        if not bookkeeping:
            line = re.sub(r"^(\s*[-*+]\s+)\[[ xX]\](\s+TASK-[0-9]{3,}\b)", r"\1[ ]\2", line)
            lines.append(line)
    return "\n".join(lines).strip()


def _digest_artifacts(artifacts, stage):
    names = ("proposal", "requirements") if stage == "proposal" else (stage,)
    normalized = []
    for name in names:
        artifact = artifacts[name]
        metadata = copy.deepcopy(artifact["metadata"])
        metadata.pop("review", None)
        if name == "proposal":
            metadata.pop("status", None)
        if name == "tasks":
            metadata.pop("validation", None)
            metadata.pop("closure", None)
            for task in metadata.get("tasks", []):
                if isinstance(task, dict):
                    task.pop("status", None)
        normalized.append({"artifact": name, "metadata": metadata, "body": _normalized_body(artifact["body"])})
    return hashlib.sha256(_json(normalized).encode("utf-8")).hexdigest()


def stage_digest(change_dir: Path, stage: str) -> str:
    """Return the canonical content digest; this does not grant approval."""
    if stage not in STAGES:
        raise ValueError(f"Unknown stage: {stage}")
    change_dir = Path(change_dir)
    if change_dir.is_symlink() or not change_dir.is_dir():
        raise ValueError("Change directory must be a real directory")
    names = ("proposal", "requirements") if stage == "proposal" else (stage,)
    artifacts = {}
    for name in names:
        path = change_dir / f"{name}.md"
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"Expected a regular artifact file: {path}")
        artifacts[name] = _read_artifact(path)
    return _digest_artifacts(artifacts, stage)


def _safe_path(root, path):
    """Allow only paths inside root and reject symlink components."""
    path = Path(path)
    try:
        relative = path.relative_to(root)
    except ValueError as exc:
        raise ValueError("Path escapes the repository") from exc
    if ".." in relative.parts:
        raise ValueError("Parent traversal is not allowed")
    current = root
    for part in relative.parts:
        current /= part
        if current.is_symlink():
            raise ValueError(f"Symlink paths are not allowed: {current}")
    return path


def _reference(root, reference, adr=False):
    if re.fullmatch(r"ADR-[0-9]{4,}", reference) and adr:
        directory = _safe_path(root, root / "docs" / "decisions")
        matches = list(directory.glob(reference[4:] + "-*.md"))
        if len(matches) != 1:
            raise ValueError(f"ADR identifier does not resolve uniquely: {reference}")
        path = _safe_path(root, matches[0])
    else:
        parsed = urlsplit(reference)
        if parsed.scheme == "https" and parsed.netloc:
            return
        if parsed.scheme or parsed.netloc or not parsed.path or Path(parsed.path).is_absolute():
            raise ValueError("Use a repository-relative file path or an HTTPS URL")
        path = _safe_path(root, root / parsed.path)
    if not path.is_file():
        raise ValueError(f"Referenced file does not exist: {reference}")


def _schemas():
    _dependencies()
    registry = Registry()
    schemas = {}
    for name in ("common",) + ARTIFACTS:
        document = yaml.load((SCHEMA_ROOT / f"{name}.schema.yaml").read_text(), Loader=UniqueKeyLoader)
        Draft202012Validator.check_schema(document)
        registry = registry.with_resource(document["$id"], Resource.from_contents(document))
        schemas[name] = document
    validators = {name: Draft202012Validator(schemas[name], registry=registry) for name in ARTIFACTS}
    for name in ARTIFACTS:
        document = yaml.load((SCHEMA_ROOT / "legacy" / f"{name}.schema.yaml").read_text(), Loader=UniqueKeyLoader)
        Draft202012Validator.check_schema(document)
        validators["legacy_" + name] = Draft202012Validator(document, registry=registry)
    return validators


def _unique_json(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


class RepositoryValidator:
    def __init__(self, root, phase, change_id):
        self.root = root
        self.phase = phase
        self.change_id = change_id
        self.findings = []
        self.warnings = []
        self.checked = []
        self.validators = _schemas()

    def add(self, code, message, path, unverified=False):
        self.findings.append({"code": code, "message": message, "path": str(path),
                              "severity": "unverified" if unverified else "error"})

    def discover(self):
        changes = {}
        for location in ("changes", "archive"):
            directory = self.root / "specs" / location
            try:
                _safe_path(self.root, directory)
                if not directory.exists():
                    continue
                if not directory.is_dir():
                    raise ValueError("Expected a directory")
                for path in sorted(directory.iterdir()):
                    if path.is_symlink():
                        self.add("PATH", "Symlink changes are not allowed", path)
                    elif path.is_dir():
                        if not CHANGE_ID.fullmatch(path.name):
                            self.add("CHANGE_ID", "Invalid change directory identifier", path)
                        elif path.name in changes:
                            self.add("DUPLICATE_CHANGE", "Change exists in both active and archive storage", path)
                        else:
                            changes[path.name] = path
            except (OSError, ValueError) as exc:
                self.add("PATH", str(exc), directory)
        return changes

    def legacy_manifest(self, changes):
        path = self.root / "sdd" / "legacy-changes.json"
        try:
            _safe_path(self.root, path)
            if not path.exists():
                return {}
            data = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique_json)
            if not isinstance(data, dict) or set(data) != {"version", "changes"} or type(data["version"]) is not int or data["version"] != 1 or not isinstance(data["changes"], dict):
                raise ValueError("Expected a version 1 legacy manifest with a changes mapping")
            entries = data["changes"]
            expected = {f"{name}.md" for name in ARTIFACTS}
            for identifier, entry in entries.items():
                if not CHANGE_ID.fullmatch(identifier) or not isinstance(entry, dict) or set(entry) not in ({"reason", "files"}, {"reason", "files", "historical_archive"}):
                    raise ValueError(f"Invalid legacy manifest entry: {identifier}")
                if not isinstance(entry["reason"], str) or not entry["reason"].strip() or not isinstance(entry["files"], dict) or set(entry["files"]) != expected:
                    raise ValueError(f"Legacy entry needs a reason and hashes for all four artifacts: {identifier}")
                if any(not isinstance(value, str) or not DIGEST.fullmatch(value) for value in entry["files"].values()):
                    raise ValueError(f"Invalid legacy content hash: {identifier}")
                if "historical_archive" in entry:
                    archive = entry["historical_archive"]
                    if not isinstance(archive, dict) or set(archive) != {"merge_commit", "evidence"}:
                        raise ValueError(f"Historical archive needs a merge commit and evidence: {identifier}")
                    if not isinstance(archive["merge_commit"], str) or not re.fullmatch(r"[a-f0-9]{40}(?:[a-f0-9]{24})?", archive["merge_commit"]):
                        raise ValueError(f"Invalid historical merge commit: {identifier}")
                    if not isinstance(archive["evidence"], str) or not archive["evidence"].strip():
                        raise ValueError(f"Historical archive needs an evidence reference: {identifier}")
                    _reference(self.root, archive["evidence"])
                    if identifier in changes and changes[identifier].parent.name != "archive":
                        raise ValueError(f"Historical archive record requires archive storage: {identifier}")
                if identifier not in changes:
                    self.add("LEGACY_UNKNOWN", f"Legacy entry has no matching dossier: {identifier}", path)
            return entries
        except (OSError, ValueError) as exc:
            self.add("LEGACY_MANIFEST", str(exc), path)
            return {}

    def artifacts(self, directory, legacy):
        artifacts = {}
        valid = True
        for name in ARTIFACTS:
            path = directory / f"{name}.md"
            try:
                _safe_path(self.root, path)
                if not path.exists():
                    if legacy or name in ("proposal", "requirements"):
                        self.add("MISSING_ARTIFACT", f"Missing {name}.md", path)
                        valid = False
                    continue
                artifact = _read_artifact(path)
                artifacts[name] = artifact
                validator = self.validators[("legacy_" if legacy else "") + name]
                for error in validator.iter_errors(artifact["metadata"]):
                    field = ".".join(str(part) for part in error.absolute_path) or "frontmatter"
                    self.add("SCHEMA", f"{field}: {error.message}", path)
                    valid = False
                if artifact["metadata"].get("change") != directory.name:
                    self.add("CHANGE_ID", "Metadata change does not match the directory identifier", path)
                    valid = False
            except (OSError, ValueError, TypeError, RecursionError, yaml.YAMLError) as exc:
                self.add("PARSE", str(exc), path)
                valid = False
        return artifacts if valid else None

    def unique(self, items, key, path, label):
        seen = set()
        for item in items:
            identifier = item[key]
            if identifier in seen:
                self.add("DUPLICATE_ID", f"Duplicate {label}: {identifier}", path)
            seen.add(identifier)
        return seen

    def coverage(self, actual, expected, path, label):
        missing, extra = expected - actual, actual - expected
        if missing or extra:
            self.add("TRACEABILITY", f"{label}: missing {sorted(missing)}; unknown {sorted(extra)}", path)

    def traceability(self, artifacts, legacy):
        requirements = artifacts["requirements"]
        ids = self.unique(requirements["metadata"]["requirements"], "id", requirements["path"], "requirement")
        design = artifacts.get("design")
        if design:
            self.coverage(set(design["metadata"]["requirements"]), ids, design["path"], "Design requirement coverage")
            for reference in design["metadata"].get("adrs", []):
                try:
                    _reference(self.root, reference, adr=True)
                except (OSError, ValueError) as exc:
                    self.add("REFERENCE", str(exc), design["path"])
            if not legacy:
                checks = design["metadata"]["validation"]
                self.unique(checks, "id", design["path"], "check")
                required_ids = set()
                for check in checks:
                    unknown = set(check["requirements"]) - ids
                    if unknown:
                        self.add("TRACEABILITY", f"{check['id']} references unknown requirements: {sorted(unknown)}", design["path"])
                    if check["required"]:
                        required_ids.update(check["requirements"])
                self.coverage(required_ids, ids, design["path"], "Required check coverage")
        tasks = artifacts.get("tasks")
        if tasks:
            items = tasks["metadata"]["tasks"]
            task_ids = self.unique(items, "id", tasks["path"], "task")
            mapped = {identifier for task in items for identifier in task["requirements"]}
            self.coverage(mapped, ids, tasks["path"], "Task requirement coverage")
            boxes = CHECKBOX.findall(tasks["body"])
            counts = {}
            for mark, identifier in boxes:
                counts.setdefault(identifier, []).append(mark.lower() == "x")
            self.coverage(set(counts), task_ids, tasks["path"], "Task checklist identifiers")
            for task in items:
                marks = counts.get(task["id"], [])
                if len(marks) != 1 or marks[0] != (task["status"] == "completed"):
                    self.add("TASK_CHECKBOX", f"{task['id']} needs one checkbox matching metadata completion", tasks["path"])

    def reviews(self, artifacts):
        digests = {stage: _digest_artifacts(artifacts, stage) for stage in STAGES if stage in artifacts}
        approved = {}
        for stage in STAGES:
            if stage not in artifacts:
                approved[stage] = False
                continue
            artifact = artifacts[stage]
            review = artifact["metadata"]["review"]
            upstream_names = () if stage == "proposal" else (("proposal",) if stage == "design" else ("proposal", "design"))
            current = review["state"] == "approved"
            if review["state"] != "superseded":
                for upstream in upstream_names:
                    if not approved.get(upstream):
                        self.add("GATE_SEQUENCE", f"{stage} requires current {upstream} approval; retain old downstream drafts as superseded", artifact["path"])
                        current = False
                    if review["upstream"].get(upstream) != digests.get(upstream):
                        self.add("UPSTREAM_STALE", f"{stage} is based on a different {upstream} revision", artifact["path"])
                        current = False
            if review["state"] == "approved":
                approval = review["approval"]
                if approval["revision"] != review["revision"] or approval["digest"] != digests[stage]:
                    self.add("APPROVAL_STALE", f"{stage} approval does not match the current content/revision", artifact["path"])
                    current = False
            approved[stage] = current
        return digests, approved

    def evidence(self, artifacts, digests, delivery):
        tasks = artifacts.get("tasks")
        design = artifacts.get("design")
        if not tasks or not design:
            return
        validation = tasks["metadata"]["validation"]
        checks = {check["id"]: check for check in design["metadata"]["validation"]}
        results = validation["results"]
        self.unique(results, "check", tasks["path"], "validation result")
        if (results or delivery) and validation["plan_digest"] != digests["tasks"]:
            self.add("VALIDATION_STALE", "Evidence must identify the current Tasks plan digest", tasks["path"], unverified=True)
        recorded = {result["check"]: result for result in results}
        for result in results:
            if result["check"] not in checks:
                self.add("TRACEABILITY", f"Unknown validation check: {result['check']}", tasks["path"])
            try:
                _reference(self.root, result["evidence"])
            except (OSError, ValueError) as exc:
                self.add("REFERENCE", str(exc), tasks["path"])
            if result["result"] == "fail":
                self.add("VALIDATION_FAILED", f"{result['check']} has a recorded failure", tasks["path"])
        if delivery:
            for identifier, check in checks.items():
                result = recorded.get(identifier)
                if check["required"] and (result is None or result["result"] == "unverified"):
                    self.add("VALIDATION_MISSING", f"{identifier} requires a passing result with evidence", tasks["path"], unverified=True)

    def dossier(self, directory, legacy_entry):
        legacy = legacy_entry is not None
        if legacy:
            for filename, expected in legacy_entry["files"].items():
                path = directory / filename
                try:
                    _safe_path(self.root, path)
                    actual = hashlib.sha256(path.read_bytes()).hexdigest()
                    if actual != expected:
                        self.add("LEGACY_CHANGED", "Allowlisted legacy artifacts must remain byte-for-byte unchanged; explicitly migrate to v2", path)
                except (OSError, ValueError) as exc:
                    self.add("LEGACY_CHANGED", str(exc), path)
        artifacts = self.artifacts(directory, legacy)
        if artifacts is None:
            return
        self.traceability(artifacts, legacy)
        if legacy:
            self.warnings.append({"code": "LEGACY_EXEMPT", "message": "Immutable legacy dossier: v2 approval and evidence gates were not verified", "path": str(directory)})
            historical_archive = "historical_archive" in legacy_entry
            if historical_archive:
                self.warnings.append({"code": "LEGACY_HISTORICAL_ARCHIVE", "message": "Historical archive record preserved; merge evidence requires human review and v2 readiness remains unverified", "path": str(directory)})
                for task in artifacts["tasks"]["metadata"]["tasks"]:
                    if task["status"] != "completed":
                        self.add("TASK_INCOMPLETE", f"{task['id']} is not completed", artifacts["tasks"]["path"])
            if self.phase != "planning" or (directory.parent.name == "archive" and not historical_archive):
                self.add("LEGACY_UNVERIFIED", "Migrate this legacy dossier explicitly before implementation or delivery readiness can be verified", directory, unverified=True)
            return
        digests, approved = self.reviews(artifacts)
        tasks = artifacts.get("tasks")
        delivery = self.phase == "delivery" or directory.parent.name == "archive" or bool(tasks and tasks["metadata"]["closure"] == "prepared")
        executing = bool(tasks and any(task["status"] != "pending" for task in tasks["metadata"]["tasks"]))
        if self.phase == "implementation" or delivery or executing:
            for stage in STAGES:
                if not approved.get(stage):
                    self.add("APPROVAL_REQUIRED", f"Current {stage} approval is required for execution or delivery", directory / f"{stage}.md")
            for stage in STAGES:
                if stage in artifacts and artifacts[stage]["metadata"]["review"]["blockers"]:
                    self.add("BLOCKED", "Resolve review blockers before execution or delivery", artifacts[stage]["path"])
        if delivery and tasks:
            for task in tasks["metadata"]["tasks"]:
                if task["status"] != "completed":
                    self.add("TASK_INCOMPLETE", f"{task['id']} is not completed", tasks["path"])
        self.evidence(artifacts, digests, delivery)

    def run(self):
        changes = self.discover()
        manifest = self.legacy_manifest(changes)
        if self.change_id and self.change_id not in changes:
            self.add("CHANGE_NOT_FOUND", f"Change not found: {self.change_id}", self.root / "specs")
        for identifier, directory in changes.items():
            if self.change_id and identifier != self.change_id:
                continue
            self.checked.append(identifier)
            self.dossier(directory, manifest.get(identifier))
        status = "pass"
        if any(item["severity"] == "error" for item in self.findings):
            status = "fail"
        elif self.findings:
            status = "unable-to-verify"
        return {"status": status, "phase": self.phase, "checked": self.checked,
                "findings": self.findings, "warnings": self.warnings,
                "scope": "Local documentary checks only; no assertion of human identity, remote CI, merge or deployment."}


def validate_repository(root: Path, phase="planning", change_id=None) -> dict:
    """Validate local dossiers. Missing external evidence remains explicitly unverified."""
    root = Path(root)
    try:
        if phase not in PHASES:
            raise ValueError(f"Unknown validation phase: {phase}")
        if change_id is not None and (not isinstance(change_id, str) or not CHANGE_ID.fullmatch(change_id)):
            raise ValueError("Invalid change identifier")
        if root.is_symlink() or not root.is_dir():
            raise ValueError("Repository root must be a real directory")
        return RepositoryValidator(root.resolve(), phase, change_id).run()
    except (OSError, ValueError, TypeError, RecursionError) as exc:
        return {"status": "fail", "phase": phase, "checked": [], "warnings": [],
                "findings": [{"code": "CONFIGURATION", "message": str(exc), "path": str(root), "severity": "error"}]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Consumer repository to validate")
    parser.add_argument("--change", help="Select a change identifier")
    parser.add_argument("--phase", choices=PHASES, default="planning")
    parser.add_argument("--digest", choices=STAGES, help="Print the content digest for one change stage")
    parser.add_argument("--json", action="store_true", help="Emit structured JSON")
    args = parser.parse_args(argv)
    if args.digest:
        try:
            if not args.change or not CHANGE_ID.fullmatch(args.change):
                raise ValueError("--digest requires --change with a valid identifier")
            if args.root.is_symlink() or not args.root.is_dir():
                raise ValueError("Repository root must be a real directory")
            root = args.root.resolve()
            matches = []
            for location in ("changes", "archive"):
                directory = _safe_path(root, root / "specs" / location / args.change)
                if directory.is_dir():
                    matches.append(directory)
            if len(matches) != 1:
                raise ValueError("Expected exactly one matching active or archived change")
            digest = stage_digest(matches[0], args.digest)
            print(_json({"change": args.change, "stage": args.digest, "digest": digest}) if args.json else digest)
            return 0
        except (OSError, ValueError, TypeError, RecursionError) as exc:
            result = {"status": "fail", "findings": [{"code": "DIGEST", "message": str(exc), "path": str(args.root)}]}
        except Exception as exc:
            # PyYAML parse errors are handled here even when optional imports failed.
            result = {"status": "fail", "findings": [{"code": "DIGEST", "message": str(exc), "path": str(args.root)}]}
    else:
        result = validate_repository(args.root, args.phase, args.change)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"SDD validation: {result['status']}")
        for finding in result["findings"]:
            print(f"{finding['code']}: {finding['path']}: {finding['message']}")
        for warning in result.get("warnings", []):
            print(f"WARNING {warning['code']}: {warning['path']}: {warning['message']}")
    return {"pass": 0, "fail": 1, "unable-to-verify": 2}[result["status"]]


if __name__ == "__main__":
    sys.exit(main())
