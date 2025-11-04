"""
Comprehensive test runner with detailed logging and reporting.
"""

import unittest
import sys
import logging
import time
from datetime import datetime
from io import StringIO
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('test_results.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


class TestRunner:
    """Comprehensive test runner with logging and reporting."""
    
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.test_results = {
            'total': 0,
            'passed': 0,
            'failed': 0,
            'errors': 0,
            'skipped': 0,
            'tests': []
        }
    
    def run_all_tests(self):
        """Run all tests with detailed logging."""
        logger.info("=" * 80)
        logger.info("COMPREHENSIVE TEST SUITE EXECUTION")
        logger.info("=" * 80)
        logger.info(f"Start time: {datetime.now().isoformat()}")
        
        self.start_time = time.time()
        
        # Discover and run all tests
        loader = unittest.TestLoader()
        suite = loader.discover('tests', pattern='test_*.py')
        
        logger.info(f"Found {suite.countTestCases()} test cases")
        logger.info("")
        
        # Run tests with detailed output
        stream = StringIO()
        runner = unittest.TextTestRunner(
            stream=stream,
            verbosity=2,
            buffer=True
        )
        
        result = runner.run(suite)
        
        self.end_time = time.time()
        duration = self.end_time - self.start_time
        
        # Collect results
        self.test_results['total'] = result.testsRun
        self.test_results['passed'] = result.testsRun - len(result.failures) - len(result.errors) - len(result.skipped)
        self.test_results['failed'] = len(result.failures)
        self.test_results['errors'] = len(result.errors)
        self.test_results['skipped'] = len(result.skipped)
        
        # Log detailed results
        logger.info("")
        logger.info("=" * 80)
        logger.info("TEST RESULTS SUMMARY")
        logger.info("=" * 80)
        logger.info(f"Total tests: {self.test_results['total']}")
        logger.info(f"Passed: {self.test_results['passed']}")
        logger.info(f"Failed: {self.test_results['failed']}")
        logger.info(f"Errors: {self.test_results['errors']}")
        logger.info(f"Skipped: {self.test_results['skipped']}")
        logger.info(f"Duration: {duration:.3f} seconds")
        logger.info("")
        
        # Log failures
        if result.failures:
            logger.warning("FAILURES:")
            for test, traceback in result.failures:
                logger.warning(f"  {test}: {traceback}")
        
        # Log errors
        if result.errors:
            logger.error("ERRORS:")
            for test, traceback in result.errors:
                logger.error(f"  {test}: {traceback}")
        
        # Log test output
        logger.info("DETAILED TEST OUTPUT:")
        logger.info(stream.getvalue())
        
        # Generate report
        self.generate_report(result, duration)
        
        return result.wasSuccessful()
    
    def generate_report(self, result, duration):
        """Generate comprehensive test report."""
        report_path = Path('test_report.txt')
        
        with open(report_path, 'w') as f:
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
        
        logger.info(f"Test report saved to: {report_path}")


if __name__ == '__main__':
    runner = TestRunner()
    success = runner.run_all_tests()
    sys.exit(0 if success else 1)

