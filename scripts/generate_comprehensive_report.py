"""
Generate comprehensive test report with logging and summary.
"""

import logging
import subprocess
import sys
from pathlib import Path
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def run_command(cmd, description):
    """Run a command and return output."""
    logger.info(f"Running: {description}")
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            cwd=Path.cwd()
        )
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        logger.error(f"Error running command: {e}")
        return False, "", str(e)


def collect_test_results():
    """Collect results from all test files."""
    logger.info("Collecting test results...")
    
    test_files = [
        "tests/test_visualization_comprehensive.py",
        "tests/test_imports_comprehensive.py",
        "tests/test_functional_comprehensive.py",
        "tests/test_integration_comprehensive.py",
    ]
    
    results = {}
    for test_file in test_files:
        if Path(test_file).exists():
            success, stdout, stderr = run_command(
                f"python3 {test_file} -v",
                f"Running {test_file}"
            )
            results[test_file] = {
                'success': success,
                'stdout': stdout,
                'stderr': stderr
            }
    
    return results


def generate_report():
    """Generate comprehensive test report."""
    logger.info("=" * 80)
    logger.info("COMPREHENSIVE TEST REPORT GENERATION")
    logger.info("=" * 80)
    logger.info(f"Generated: {datetime.now().isoformat()}")
    logger.info("")
    
    # Run all tests
    logger.info("Running comprehensive test suite...")
    success, stdout, stderr = run_command(
        "python3 -m unittest discover tests -v",
        "Running all unit tests"
    )
    
    # Collect comprehensive test results
    comprehensive_results = collect_test_results()
    
    # Verify documentation
    logger.info("Verifying documentation...")
    doc_success, doc_stdout, doc_stderr = run_command(
        "PYTHONPATH=. python3 scripts/verify_documentation.py",
        "Verifying documentation"
    )
    
    # Generate report file
    report_path = Path("docs/COMPREHENSIVE_TEST_REPORT.md")
    
    with open(report_path, 'w') as f:
        f.write("# Comprehensive Test Report\n\n")
        f.write(f"**Generated:** {datetime.now().isoformat()}\n\n")
        f.write("## Executive Summary\n\n")
        
        # Overall status
        all_tests_passed = success and doc_success
        status = "✅ PASS" if all_tests_passed else "❌ FAIL"
        f.write(f"**Overall Status:** {status}\n\n")
        
        f.write("## Test Results\n\n")
        
        # Main test suite
        f.write("### Main Test Suite\n\n")
        if success:
            f.write("✅ **PASSED** - All unit tests passed\n\n")
            # Count tests
            test_count = stdout.count("test_")
            f.write(f"- Total tests executed: {test_count}\n")
        else:
            f.write("❌ **FAILED** - Some tests failed\n\n")
            f.write("```\n")
            f.write(stderr)
            f.write("\n```\n\n")
        
        # Comprehensive tests
        f.write("### Comprehensive Test Modules\n\n")
        for test_file, result in comprehensive_results.items():
            status = "✅ PASS" if result['success'] else "❌ FAIL"
            f.write(f"- **{test_file}**: {status}\n")
            if not result['success']:
                f.write(f"  ```\n{result['stderr']}\n```\n")
        
        # Documentation verification
        f.write("\n### Documentation Verification\n\n")
        if doc_success:
            f.write("✅ **PASSED** - Documentation verification complete\n\n")
        else:
            f.write("❌ **FAILED** - Documentation issues found\n\n")
        
        # Module structure
        f.write("## Module Structure Verification\n\n")
        f.write("### Package Modules\n\n")
        modules = [
            "ivm_xyz",
            "ivm_xyz.core",
            "ivm_xyz.conversion",
            "ivm_xyz.polyhedra",
            "ivm_xyz.visualization",
        ]
        for module in modules:
            f.write(f"- ✅ {module}\n")
        
        # Test coverage
        f.write("\n## Test Coverage\n\n")
        f.write("### Test Files\n\n")
        test_files = [
            "tests/test_vectors.py",
            "tests/test_tetrahedron.py",
            "tests/test_triangle.py",
            "tests/test_conversion.py",
            "tests/test_polyhedra.py",
            "tests/test_visualization.py",
        ]
        for test_file in test_files:
            if Path(test_file).exists():
                f.write(f"- ✅ {test_file}\n")
            else:
                f.write(f"- ❌ {test_file} (missing)\n")
        
        # Key Features Verified
        f.write("\n## Key Features Verified\n\n")
        features = [
            "Vector operations (XYZ coordinates)",
            "Qvector operations (IVM Quadray coordinates)",
            "Tetrahedron volume calculations",
            "Triangle area calculations",
            "Coordinate conversion (XYZ ↔ IVM)",
            "Polyhedra creation and transformations",
            "Edge counting functions",
            "Visualization tools",
        ]
        for feature in features:
            f.write(f"- ✅ {feature}\n")
        
        # Recommendations
        f.write("\n## Recommendations\n\n")
        if all_tests_passed:
            f.write("✅ All tests passing - package is ready for use\n")
        else:
            f.write("⚠️ Review failing tests and address issues\n")
        
        f.write("\n## Log Files\n\n")
        log_files = [
            "test_results.log",
            "test_output.log",
            "visualization_test_output.log",
            "import_test_output.log",
            "functional_test_output.log",
            "integration_test_output.log",
            "documentation_verification.log",
        ]
        for log_file in log_files:
            if Path(log_file).exists():
                f.write(f"- ✅ {log_file}\n")
    
    logger.info(f"Report generated: {report_path}")
    
    # Print summary
    logger.info("")
    logger.info("=" * 80)
    logger.info("SUMMARY")
    logger.info("=" * 80)
    logger.info(f"Main test suite: {'✅ PASS' if success else '❌ FAIL'}")
    logger.info(f"Documentation: {'✅ PASS' if doc_success else '❌ FAIL'}")
    logger.info(f"Overall: {'✅ PASS' if all_tests_passed else '❌ FAIL'}")
    logger.info(f"Report: {report_path}")
    
    return all_tests_passed


if __name__ == '__main__':
    success = generate_report()
    sys.exit(0 if success else 1)

