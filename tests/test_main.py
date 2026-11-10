"""Run the existing Flatlib unittest modules under Bazel."""

import sys
import unittest

import test_angles
import test_chart


suite = unittest.TestSuite(
    [
        unittest.defaultTestLoader.loadTestsFromModule(test_angles),
        unittest.defaultTestLoader.loadTestsFromModule(test_chart),
    ]
)
if suite.countTestCases() == 0:
    raise RuntimeError("Flatlib tests discovered no test cases")

result = unittest.TextTestRunner(verbosity=2).run(suite)
if result.testsRun <= len(result.skipped):
    print("Flatlib tests ran no test cases; all discovered cases were skipped", file=sys.stderr)
    sys.exit(1)
sys.exit(not result.wasSuccessful())
