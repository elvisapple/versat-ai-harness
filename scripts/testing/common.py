"""Shared offline contracts and process execution. No implicit installation or shell expansion."""
from __future__ import annotations
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import signal
import shutil
import subprocess
import sys
import threading
import time

PACKAGE = Path(__file__).resolve().parents[2]


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


contract = load_module('testing_contract', PACKAGE/'validators/testing/validate.py')
sdd = load_module('testing_sdd', PACKAGE/'validators/sdd/validate.py')
LOG_LIMIT = 1024 * 1024


def digest_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def provider_digest():
    files = []
    for folder in ('scripts/testing', 'validators/testing', 'validators/sdd', 'schemas', 'sdd/schemas'):
        for p in sorted((PACKAGE/folder).rglob('*')):
            if p.is_file() and '__pycache__' not in p.parts:
                files.append((p.relative_to(PACKAGE).as_posix(), digest_file(p)))
    return hashlib.sha256(json.dumps(files).encode()).hexdigest()


def atomic_json(path, data):
    path = Path(path)
    temporary = path.with_suffix(path.suffix+'.tmp')
    with temporary.open('x', encoding='utf-8') as stream:
        json.dump(data, stream, indent=2, allow_nan=False)
        stream.write('\n')
    temporary.replace(path)


def clean_environment(names=()):
    allowed = {'PATH','LANG','LC_ALL','SYSTEMROOT','TMPDIR','TMP','TEMP'} | set(names)
    env = {k:v for k,v in os.environ.items() if k in allowed}
    env.update(PYTHONDONTWRITEBYTECODE='1', PYTHONUNBUFFERED='1')
    return env


def execute(argv, cwd, directory, timeout, environment=None, stdin=None):
    """Drain capped streams without unbounded memory/disk; terminate descendants on cancellation."""
    if os.name != 'posix' or sys.platform not in ('linux','darwin'):
        return {'result':'unverified','reason':'Supported process isolation requires Linux or macOS'}
    start = time.monotonic()
    record = {'argv':argv, 'cwd':str(cwd), 'result':'running', 'truncated':{}}
    process = None
    workers = []
    stream_errors = []
    def drain(pipe, target, label):
        size = 0
        try:
            with target.open('xb') as output:
                while chunk := pipe.read(8192):
                    remaining = max(0, LOG_LIMIT-size)
                    output.write(chunk[:remaining])
                    size += len(chunk)
            record['truncated'][label] = size > LOG_LIMIT
        except OSError as exc:
            stream_errors.append(f'{label}: {exc}')
        finally:
            pipe.close()
    def terminate():
        try:
            os.killpg(process.pid, signal.SIGTERM)
        except ProcessLookupError:
            return
        try:
            process.wait(timeout=1)
        except subprocess.TimeoutExpired:
            pass
        # The parent can exit while descendants ignore SIGTERM.
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        process.wait()
    try:
        if stdin is not None and len(stdin.encode()) > 4096:
            return dict(record, result='unverified', reason='Prompt exceeds bounded 4096-byte input')
        environment = clean_environment() if environment is None else environment
        # Preserve the invocation path: resolving a venv Python symlink loses its environment.
        executable = os.path.abspath(Path(cwd)/argv[0]) if '/' in argv[0] else shutil.which(argv[0],path=environment.get('PATH',os.defpath))
        if not executable:
            raise FileNotFoundError(f'Executable unavailable: {argv[0]}')
        record['resolved_executable'] = str(Path(executable).resolve())
        process = subprocess.Popen([executable,*argv[1:]], cwd=cwd, env=environment,
                                   stdin=subprocess.PIPE if stdin is not None else subprocess.DEVNULL,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True)
        for label in ('stdout','stderr'):
            worker = threading.Thread(target=drain, args=(getattr(process,label),directory/(label+'.txt'),label), daemon=True)
            worker.start(); workers.append(worker)
        if stdin is not None:
            # Evaluation prompts are capped by the caller and fit in a pipe buffer.
            try:
                process.stdin.write(stdin.encode()); process.stdin.close()
            except BrokenPipeError:
                pass
        try:
            code = process.wait(timeout=timeout)
            record.update(exit_code=code, result='pass' if code == 0 else 'fail', reason='exit')
        except (subprocess.TimeoutExpired, KeyboardInterrupt) as exc:
            terminate()
            record.update(exit_code=process.returncode, result='fail', reason='timeout' if isinstance(exc,subprocess.TimeoutExpired) else 'interrupted')
        finally:
            # Close stray descendants that keep captured streams open after parent exit.
            terminate()
            for worker in workers:
                worker.join(timeout=3)
            if any(worker.is_alive() for worker in workers):
                record.update(result='fail',reason='Output stream did not terminate')
            if stream_errors:
                record.update(result='fail',reason='Output capture failed: '+'; '.join(stream_errors))
    except OSError as exc:
        record.update(result='unverified',reason=f'Cannot launch command: {exc}')
    except BaseException:
        # An enclosing evaluation deadline must also reap active project commands.
        if process is not None:
            terminate()
        for worker in workers:
            worker.join(timeout=3)
        raise
    record['duration_seconds'] = round(time.monotonic()-start,3)
    return record
