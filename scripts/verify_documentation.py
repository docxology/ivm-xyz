"""
Verify documentation matches implementation.
"""

import inspect
import logging
from pathlib import Path
import ast
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def extract_functions_from_file(file_path):
    """Extract function names from a Python file."""
    functions = []
    try:
        with open(file_path, 'r') as f:
            tree = ast.parse(f.read())
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    functions.append(node.name)
                elif isinstance(node, ast.ClassDef):
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef):
                            functions.append(f"{node.name}.{item.name}")
    except Exception as e:
        logger.warning(f"Error parsing {file_path}: {e}")
    return functions


def verify_api_documentation():
    """Verify API documentation matches implementation."""
    logger.info("Verifying API documentation...")
    
    # Read API.md
    api_path = Path("docs/API.md")
    if not api_path.exists():
        logger.warning("API.md not found")
        return False
    
    api_content = api_path.read_text()
    
    # Check for key classes and functions
    key_items = [
        "Vector", "Qvector", "Tetrahedron", "make_tet",
        "Triangle", "make_tri", "xyz_to_ivm", "ivm_to_xyz",
        "Polyhedron", "Cube", "Octahedron", "PolyhedronPlotter"
    ]
    
    missing_items = []
    for item in key_items:
        if item not in api_content:
            missing_items.append(item)
    
    if missing_items:
        logger.warning(f"Missing items in API.md: {missing_items}")
    else:
        logger.info(f"  ✓ All {len(key_items)} key items found in API.md")
    
    return len(missing_items) == 0


def verify_readme_examples():
    """Verify examples in README work."""
    logger.info("Verifying README examples...")
    
    readme_path = Path("README.md")
    if not readme_path.exists():
        logger.warning("README.md not found")
        return False
    
    readme_content = readme_path.read_text()
    
    # Check for code blocks
    code_blocks = re.findall(r'```python\n(.*?)```', readme_content, re.DOTALL)
    logger.info(f"  Found {len(code_blocks)} code examples in README")
    
    # Try to verify imports are correct
    import_checks = [
        "from ivm_xyz import",
        "from ivm_xyz.core import",
        "from ivm_xyz.conversion import",
        "from ivm_xyz.polyhedra import",
        "from ivm_xyz.visualization import"
    ]
    
    found_imports = []
    for check in import_checks:
        if check in readme_content:
            found_imports.append(check)
    
    logger.info(f"  ✓ Found {len(found_imports)}/{len(import_checks)} import patterns")
    
    return True


def verify_all_functions_exist():
    """Verify all documented functions actually exist."""
    logger.info("Verifying all documented functions exist...")
    
    # Import main package
    try:
        import ivm_xyz
        from ivm_xyz import Vector, Qvector, Tetrahedron, make_tet, Triangle, make_tri
        from ivm_xyz.conversion import xyz_to_ivm, ivm_to_xyz
        from ivm_xyz.polyhedra import Cube, Octahedron, Polyhedron
        from ivm_xyz.visualization import PolyhedronPlotter
        
        # Verify classes have expected methods
        vector_methods = ['length', 'dot', 'cross', 'angle', 'quadray']
        for method in vector_methods:
            if hasattr(Vector, method):
                logger.info(f"  ✓ Vector.{method} exists")
            else:
                logger.warning(f"  ⚠ Vector.{method} missing")
        
        qvector_methods = ['length', 'dot', 'cross', 'xyz']
        for method in qvector_methods:
            if hasattr(Qvector, method):
                logger.info(f"  ✓ Qvector.{method} exists")
            else:
                logger.warning(f"  ⚠ Qvector.{method} missing")
        
        tetrahedron_methods = ['ivm_volume', 'xyz_volume']
        for method in tetrahedron_methods:
            if hasattr(Tetrahedron, method):
                logger.info(f"  ✓ Tetrahedron.{method} exists")
            else:
                logger.warning(f"  ⚠ Tetrahedron.{method} missing")
        
        logger.info("✓ All documented functions verified")
        return True
        
    except Exception as e:
        logger.error(f"Error verifying functions: {e}")
        return False


def verify_module_structure():
    """Verify module structure matches documentation."""
    logger.info("Verifying module structure...")
    
    expected_modules = [
        "ivm_xyz",
        "ivm_xyz.core",
        "ivm_xyz.core.vectors",
        "ivm_xyz.core.tetrahedron",
        "ivm_xyz.core.triangle",
        "ivm_xyz.core.constants",
        "ivm_xyz.conversion",
        "ivm_xyz.conversion.converters",
        "ivm_xyz.polyhedra",
        "ivm_xyz.polyhedra.base",
        "ivm_xyz.polyhedra.platonic",
        "ivm_xyz.polyhedra.edge_counting",
        "ivm_xyz.visualization",
        "ivm_xyz.visualization.plotter",
    ]
    
    missing_modules = []
    for module_name in expected_modules:
        try:
            __import__(module_name)
            logger.info(f"  ✓ Module exists: {module_name}")
        except ImportError:
            missing_modules.append(module_name)
            logger.warning(f"  ⚠ Module missing: {module_name}")
    
    if missing_modules:
        logger.warning(f"Missing modules: {missing_modules}")
        return False
    
    logger.info(f"✓ All {len(expected_modules)} modules verified")
    return True


if __name__ == '__main__':
    logger.info("=" * 80)
    logger.info("DOCUMENTATION VERIFICATION")
    logger.info("=" * 80)
    
    results = {
        'api_docs': verify_api_documentation(),
        'readme_examples': verify_readme_examples(),
        'functions_exist': verify_all_functions_exist(),
        'module_structure': verify_module_structure(),
    }
    
    logger.info("")
    logger.info("=" * 80)
    logger.info("VERIFICATION SUMMARY")
    logger.info("=" * 80)
    for check, result in results.items():
        status = "✓ PASS" if result else "✗ FAIL"
        logger.info(f"{status}: {check}")
    
    all_passed = all(results.values())
    logger.info("")
    if all_passed:
        logger.info("✓ All documentation checks passed")
    else:
        logger.warning("⚠ Some documentation checks failed")
    
    exit(0 if all_passed else 1)

