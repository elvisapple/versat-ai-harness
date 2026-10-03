#!/usr/bin/env python3
"""Run actual unittest cases and produce JSON-v1 counts; empty/all-skipped is non-passing."""
import argparse
import json
from pathlib import Path
import sys
import unittest


class CountedResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.executed_subtests = set()

    def addSubTest(self, test, subtest, err):
        self.executed_subtests.add(test.id())
        super().addSubTest(test, subtest, err)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--report', required=True, type=Path)
    parser.add_argument('arguments', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    arguments = args.arguments
    if arguments[:1] == ['--']:
        arguments = arguments[1:]
    sys.path.insert(0, str(Path.cwd()))
    test_runner = unittest.TextTestRunner(resultclass=CountedResult)
    program = unittest.TestProgram(module=None, argv=['unittest', *arguments], exit=False, testRunner=test_runner)
    result = program.result
    def identity(case):
        return getattr(case, 'test_case', case).id()
    errors = {identity(t) for t,_ in result.errors}
    failed = {identity(t) for t,_ in result.failures} | {identity(t) for t in result.unexpectedSuccesses}
    failed -= errors
    skipped = {identity(t) for t,_ in result.skipped} - result.executed_subtests - failed - errors
    report = dict(schema_version=1, collected=result.testsRun, executed=result.testsRun-len(skipped),
                  skipped=len(skipped), failed=len(failed), errors=len(errors))
    with args.report.open('x') as stream:
        json.dump(report, stream)
    return 0 if result.wasSuccessful() and report['executed'] > 0 else 1


if __name__ == '__main__':
    sys.exit(main())
