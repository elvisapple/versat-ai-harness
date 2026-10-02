"""Read-only, repository-bounded input snapshots and Git baseline selection."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess


def local_path(root, value):
    path = Path(value)
    if not value or path.is_absolute() or '..' in path.parts or '\\' in value:
        raise ValueError(f'Expected a repository-relative path: {value}')
    current = root
    for part in path.parts:
        current /= part
        if current.is_symlink():
            raise ValueError(f'Symlink input is forbidden: {value}')
    return current


def under(path, parent):
    return path == parent or parent in path.parents


def input_scope(root, directory, check, inspect_links=True):
    """Validate scope relationships; historical syntax checks read no input files."""
    def scoped(value):
        path = Path(value)
        if not value or path.is_absolute() or '..' in path.parts or '\\' in value:
            raise ValueError(f'Expected a repository-relative path: {value}')
        return local_path(root, value) if inspect_links else root / path

    included = [scoped(p) for p in check['inputs']['include']]
    excluded = [scoped(p) for p in check['inputs']['exclude']]
    outputs = [scoped(p) for p in check['outputs']]
    automatic = [root / '.git', directory]
    for path in included:
        if any(under(path, p) for p in outputs + automatic + excluded):
            raise ValueError(f'Explicit input is excluded or is an output: {path.relative_to(root)}')
    for output in outputs:
        if any(under(output, p) for p in included) and not any(under(output, p) for p in excluded):
            raise ValueError('Output beneath an input root needs an explicit exclusion')
    return included, excluded + outputs + automatic


def input_digest(root, directory, check, cache=None):
    """Hash declared inputs, never execute the described check or read outputs."""
    root = Path(root).resolve()
    directory = Path(directory).resolve()
    included, excluded = input_scope(root, directory, check)
    records = {}
    cache = {} if cache is None else cache
    storage = {root / "specs", root / "specs/changes", root / "specs/archive"}

    def visit(path):
        if any(under(path, p) for p in excluded):
            return
        relative = path.relative_to(root).as_posix()
        if relative in records:
            return
        try:
            info = path.lstat()
        except FileNotFoundError:
            records[relative] = ['missing']
            return
        if stat.S_ISLNK(info.st_mode):
            raise ValueError(f'Symlink input is forbidden: {relative}')
        if stat.S_ISDIR(info.st_mode):
            # Storage containers are bookkeeping; traversal still includes every
            # other dossier/file, while moving this dossier cannot alter its inputs.
            if path not in storage:
                records[relative] = ['directory']
            for child in sorted(path.iterdir()):
                visit(child)
        elif stat.S_ISREG(info.st_mode):
            # Verify the opened file itself, including concurrent replacement.
            flags = os.O_RDONLY | getattr(os, 'O_NOFOLLOW', 0) | getattr(os, 'O_NONBLOCK', 0)
            descriptor = os.open(path, flags)
            with os.fdopen(descriptor, 'rb') as stream:
                before = os.fstat(stream.fileno())
                if not stat.S_ISREG(before.st_mode) or before.st_ino != info.st_ino:
                    raise ValueError(f'Input changed during snapshot: {relative}')
                fingerprint = (str(path), before.st_dev, before.st_ino, before.st_size, before.st_mtime_ns, before.st_ctime_ns, before.st_mode)
                hashed = cache.get(fingerprint)
                if hashed is None:
                    hashed = hashlib.file_digest(stream, 'sha256').hexdigest()
                    cache[fingerprint] = hashed
                after = os.fstat(stream.fileno())
            if (before.st_size, before.st_mtime_ns, before.st_ctime_ns) != (after.st_size, after.st_mtime_ns, after.st_ctime_ns):
                raise ValueError(f'Input changed during snapshot: {relative}')
            records[relative] = ['file', before.st_mode & 0o111, hashed]
        else:
            raise ValueError(f'Special input is forbidden: {relative}')

    for path in included:
        visit(path)
    payload = {'scope': check['inputs'], 'outputs': check['outputs'], 'files': sorted(records.items())}
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def changed_dossiers(root, baseline, locations=("changes", "archive")):
    """Select changed dossier IDs from both sides of moves, using a trusted base."""
    def git(*args):
        result = subprocess.run(['git', '-C', str(root), *args], capture_output=True, check=False)
        if result.returncode:
            raise ValueError('Git baseline selection failed: ' + result.stderr.decode(errors='replace').strip())
        return result.stdout

    if not baseline or baseline.startswith('-') or '\x00' in baseline:
        raise ValueError('A valid trusted baseline revision is required')
    commit = git('rev-parse', '--verify', '--end-of-options', baseline + '^{commit}').strip().decode('ascii')
    # Disable rename detection: both old and new paths are then explicit records.
    roots = ['specs/' + location + '/' for location in locations]
    paths = git('diff', '--name-only', '--no-renames', '-z', commit, '--', *roots).split(b'\0')
    paths += git('ls-files', '--others', '--exclude-standard', '-z', '--', *roots).split(b'\0')
    return sorted({os.fsdecode(p).split('/')[2] for p in paths if p and len(os.fsdecode(p).split('/')) >= 3})


def changed_archives(root, baseline):
    """Select archive changes for historical-inventory/live-delivery separation."""
    return changed_dossiers(root, baseline, locations=("archive",))
