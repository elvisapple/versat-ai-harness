"""Synthetic fixtures shared by execution tests, never real approval evidence."""
from pathlib import Path
import sys
import tempfile
import yaml

PACKAGE=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(PACKAGE/'scripts/testing'))
import run as runner
from common import contract, sdd


def write_config(root,suites=None):
    (root/'.versat').mkdir(exist_ok=True)
    (root/'tests').mkdir(exist_ok=True)
    (root/'src').mkdir(exist_ok=True)
    config={'schema_version':1,'required_suites':['unit'],
            'suites':suites or [{'id':'unit','kind':'tests','argv':['{python}','-m','unittest','discover','-s','tests'],
                               'cwd':'.','timeout_seconds':10,'result':'unittest'}],
            'inputs':{'include':['.versat/validation.yaml','tests','src','scripts'], 'exclude':[]}}
    (root/'.versat/validation.yaml').write_text(yaml.safe_dump(config,sort_keys=False))
    return config


def simple_test(root,body='self.assertEqual(2 + 2, 4)'):
    (root/'tests/test_sample.py').write_text('import unittest\nclass TestSample(unittest.TestCase):\n    def test_behavior(self):\n        '+body+'\n')
