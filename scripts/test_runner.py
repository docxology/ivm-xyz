"""
Comprehensive test runner with detailed logging and reporting.

Always resolves the repository root (parent of ``scripts/``), changes the
process working directory to that root, and writes logs under
``outputs/logs/`` and the text summary under ``outputs/reports/`` so
discovery, imports (``tests._support``), and subprocesses behave consistently.
"""

import logging
import os
import sys
import time
import unittest
from datetime import datetime
from io import StringIO
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_LOG_DIR = REPO_ROOT / "outputs" / "logs"
OUTPUT_REPORT_DIR = REPO_ROOT / "outputs" / "reports"


def _setup_logging() -> None:
    OUTPUT_LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_path = OUTPUT_LOG_DIR / "test_results.log"
    root = logging.getLogger()
    root.handlers.clear()
    root.setLevel(logging.INFO)
    fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    fh = logging.FileHandler(log_path)
    fh.setFormatter(fmt)
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    root.addHandler(fh)
    root.addHandler(sh)


_setup_logging()
logger = logging.getLogger(__name__)


class TestRunner:
    """Comprehensive test runner with logging and reporting."""

    def __init__(self) -> None:
        self.start_time = None
        self.end_time = None
        self.test_results = {
            "total": 0,
            "passed": 0,
            "failed": 0,
            "errors": 0,
            "skipped": 0,
            "tests": [],
        }

    def run_all_tests(self) -> bool:
        """Run all tests with detailed logging."""
        os.chdir(REPO_ROOT)
        root_s = str(REPO_ROOT)
        if root_s not in sys.path:
            sys.path.insert(0, root_s)

        logger.info("=" * 80)
        logger.info("COMPREHENSIVE TEST SUITE EXECUTION")
        logger.info("=" * 80)
        logger.info("Repository root: %s", REPO_ROOT)
        logger.info("Start time: %s", datetime.now().isoformat())

        self.start_time = time.time()

        loader = unittest.TestLoader()
        suite = loader.discover(
            str(REPO_ROOT / "tests"),
            pattern="test_*.py",
            top_level_dir=str(REPO_ROOT),
        )

        logger.info("Found %s test cases", suite.countTestCases())
        logger.info("")

        stream = StringIO()
        runner = unittest.TextTestRunner(stream=stream, verbosity=2, buffer=True)

        result = runner.run(suite)

        self.end_time = time.time()
        duration = self.end_time - self.start_time

        self.test_results["total"] = result.testsRun
        self.test_results["passed"] = (
            result.testsRun - len(result.failures) - len(result.errors) - len(result.skipped)
        )
        self.test_results["failed"] = len(result.failures)
        self.test_results["errors"] = len(result.errors)
        self.test_results["skipped"] = len(result.skipped)

        logger.info("")
        logger.info("=" * 80)
        logger.info("TEST RESULTS SUMMARY")
        logger.info("=" * 80)
        logger.info("Total tests: %s", self.test_results["total"])
        logger.info("Passed: %s", self.test_results["passed"])
        logger.info("Failed: %s", self.test_results["failed"])
        logger.info("Errors: %s", self.test_results["errors"])
        logger.info("Skipped: %s", self.test_results["skipped"])
        logger.info("Duration: %.3f seconds", duration)
        logger.info("")

        if result.failures:
            logger.warning("FAILURES:")
            for test, traceback in result.failures:
                logger.warning("  %s: %s", test, traceback)

        if result.errors:
            logger.error("ERRORS:")
            for test, traceback in result.errors:
                logger.error("  %s: %s", test, traceback)

        logger.info("DETAILED TEST OUTPUT:")
        logger.info(stream.getvalue())

        self.generate_report(result, duration)

        return result.wasSuccessful()

    def generate_report(self, result: unittest.TestResult, duration: float) -> None:
        """Write ``test_report.txt`` under ``outputs/reports/``."""
        OUTPUT_REPORT_DIR.mkdir(parents=True, exist_ok=True)
        report_path = OUTPUT_REPORT_DIR / "test_report.txt"
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("=" * 80 + "\n")
            f.write("COMPREHENSIVE TEST REPORT\n")
            f.write("=" * 80 + "\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n")
            f.write(f"Duration: {duration:.3f} seconds\n")
            f.write("\n")
            f.write("SUMMARY:\n")
            f.write(f"  Total tests: {self.test_results['total']}\n")
            f.write(f"  Passed: {self.test_results['passed']}\n")
            f.write(f"  Failed: {self.test_results['failed']}\n")
            f.write(f"  Errors: {self.test_results['errors']}\n")
            f.write(f"  Skipped: {self.test_results['skipped']}\n")
            f.write("\n")
            if result.failures:
                f.write("FAILURES:\n")
                for test, traceback in result.failures:
                    f.write(f"  {test}\n")
                    f.write(f"    {traceback}\n")
                f.write("\n")
            if result.errors:
                f.write("ERRORS:\n")
                for test, traceback in result.errors:
                    f.write(f"  {test}\n")
                    f.write(f"    {traceback}\n")
        logger.info("Test report saved to: %s", report_path)


if __name__ == "__main__":
    success = TestRunner().run_all_tests()
    sys.exit(0 if success else 1)
