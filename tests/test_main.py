"""Run the existing Flatlib unittest modules under Bazel."""

import sys
import unittest
from pathlib import Path
from importlib import import_module

import flatlib

import test_angles
import test_chart


class PackageClosureTest(unittest.TestCase):
    def test_ephemeris_resources_are_present(self):
        swefiles = Path(flatlib.PATH_RES) / "swefiles"
        self.assertTrue(swefiles.is_dir())
        self.assertTrue(any(swefiles.iterdir()))

    def test_imports_from_each_package(self):
        for module in (
            "flatlib.dignities.accidental",
            "flatlib.ephem.ephem",
            "flatlib.predictives.returns",
            "flatlib.protocols.temperament",
            "flatlib.tools.arabicparts",
            "flatlib.tools.chartdynamics",
            "flatlib.tools.planetarytime",
        ):
            with self.subTest(module=module):
                self.assertIsNotNone(import_module(module))


suite = unittest.TestSuite(
    [
        unittest.defaultTestLoader.loadTestsFromModule(test_angles),
        unittest.defaultTestLoader.loadTestsFromModule(test_chart),
        unittest.defaultTestLoader.loadTestsFromTestCase(PackageClosureTest),
    ]
)
if suite.countTestCases() == 0:
    raise RuntimeError("Flatlib tests discovered no test cases")

result = unittest.TextTestRunner(verbosity=2).run(suite)
if result.testsRun <= len(result.skipped):
    print("Flatlib tests ran no test cases; all discovered cases were skipped", file=sys.stderr)
    sys.exit(1)
sys.exit(not result.wasSuccessful())
