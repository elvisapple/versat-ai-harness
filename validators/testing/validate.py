#!/usr/bin/env python3
"""Pure validation of configured commands and structured test counts. Never executes commands."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import stat
import sys

import yaml
from jsonschema import Draft202012Validator

PACKAGE = Path(__file__).resolve().parents[2]
TOKENS = {'{python}', '{harness_root}', '{report}'}


class UniqueLoader(yaml.SafeLoader):
    def construct_mapping(self, node, deep=False):
        result = {}
        for key, value in node.value:
            name = self.construct_object(key, deep=deep)
            if not isinstance(name, str) or name in result:
                raise ValueError('YAML requires unique string keys')
            result[name] = self.construct_object(value, deep=deep)
        return result


def read_yaml(path: Path):
    if path.stat().st_size > 1024 * 1024:
        raise ValueError('Configuration exceeds 1 MiB')
    return yaml.load(path.read_text(), Loader=UniqueLoader)


def safe_path(root: Path, value: str) -> Path:
    """Reject escapes, links and special files, including existing parent components."""
    path = Path(value)
    if path.is_absolute() or '..' in path.parts or not value or '\x00' in value or '\\' in value:
        raise ValueError(f'Expected safe project-relative path: {value!r}')
    current = root
    for part in path.parts:
        current /= part
        if current.is_symlink():
            raise ValueError(f'Symlink forbidden: {value}')
        if current.exists() and not (current.is_dir() or stat.S_ISREG(current.stat().st_mode)):
            raise ValueError(f'Special file forbidden: {value}')
    return current


def schema_check(data, name):
    schema = read_yaml(PACKAGE/'schemas'/f'{name}.schema.yaml')
    errors = sorted(Draft202012Validator(schema).iter_errors(data), key=lambda e: str(list(e.path)))
    if errors:
        error = errors[0]
        raise ValueError(f'{name} {list(error.path)}: {error.message}')


def covered(root: Path, path: Path, scope: dict) -> bool:
    includes = [safe_path(root, p) for p in scope['include']]
    excludes = [safe_path(root, p) for p in scope['exclude']]
    return any(path.is_relative_to(p) for p in includes) and not any(path.is_relative_to(p) for p in excludes)


def load_config(root: Path, relative='.versat/validation.yaml') -> dict:
    config_path = safe_path(root, relative)
    data = read_yaml(config_path)
    schema_check(data, 'validation')
    ids = [s['id'] for s in data['suites']]
    if len(ids) != len(set(ids)) or not set(data['required_suites']) <= set(ids):
        raise ValueError('Suite IDs must be unique and all required suites must exist')
    for value in data['inputs']['include'] + data['inputs']['exclude']:
        safe_path(root, value)
    if not covered(root, config_path, data['inputs']):
        raise ValueError('Validation configuration must be in the input snapshot')
    for suite in data['suites']:
        safe_path(root, suite['cwd'])
        if suite['kind'] == 'tests' and suite['result'] == 'exit-code':
            raise ValueError('Test suites require actual structured counts')
        if suite['kind'] == 'check' and suite['result'] != 'exit-code':
            raise ValueError('Non-test checks use exit-code; use kind tests for structured counts')
        if suite['result'] == 'unittest' and suite['argv'][:3] != ['{python}', '-m', 'unittest']:
            raise ValueError('unittest adapter requires {python} -m unittest followed by test arguments')
        if suite['result'] == 'json-v1' and '{report}' not in suite['argv']:
            raise ValueError('json-v1 producer must receive the fresh {report} path')
        for arg in suite['argv']:
            if '\x00' in arg or (re.fullmatch(r'\{[^{}]+\}', arg) and arg not in TOKENS):
                raise ValueError('Unknown argument token or NUL')
        for name in suite.get('environment', []):
            if re.search(r'(TOKEN|SECRET|PASSWORD|API_KEY|CREDENTIAL|AUTH)', name):
                raise ValueError('Credential environment names are forbidden in project test suites')
    return data


def validate_counts(data: dict) -> dict:
    schema_check(data, 'validation-result')
    if data['collected'] != data['executed'] + data['skipped']:
        raise ValueError('Collected count differs from executed plus skipped')
    if data['failed'] + data['errors'] > data['executed']:
        raise ValueError('Failure/error counts exceed executed test cases')
    if data['executed'] == 0:
        raise ValueError('No test cases executed (empty or all skipped)')
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path.cwd())
    args = parser.parse_args()
    try:
        data = load_config(args.root.resolve())
        print(json.dumps({'status':'pass','required_suites':data['required_suites']}))
        return 0
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(json.dumps({'status':'fail','reason':str(exc)}))
        return 1


if __name__ == '__main__':
    sys.exit(main())
