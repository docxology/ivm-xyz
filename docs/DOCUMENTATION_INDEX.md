# Documentation Index

Complete guide to all documentation in the IVM-XYZ package.

## Quick Navigation

### For Users

1. **[README.md](../README.md)** - Start here! Quick start guide and overview
2. **[API.md](API.md)** - Complete API reference with all methods and signatures
3. **[MODULES.md](MODULES.md)** - Detailed module-by-module documentation
4. **[BACKGROUND.md](BACKGROUND.md)** - Mathematical background and theory

### For Developers

1. **[AGENTS.md](AGENTS.md)** - Development workflows and agent documentation
2. **[TECHNICAL_REFERENCE.md](TECHNICAL_REFERENCE.md)** - Technical implementation details
3. **[STRUCTURE.md](STRUCTURE.md)** - Package structure and organization
4. **[TESTING_SUMMARY.md](TESTING_SUMMARY.md)** - Testing overview and results
5. **[.cursorrules](.cursorrules)** - Development rules and guidelines

## Documentation Files

### Core Documentation

#### [API.md](API.md)
**Purpose**: Complete technical API reference  
**Audience**: All users (beginners to advanced)  
**Contents**:
- Complete method signatures
- Parameter descriptions
- Return types
- Mathematical formulas
- Code examples
- Technical notes

**Key Sections**:
- Vector class (all 20+ methods)
- Qvector class (all methods)
- Svector class
- Tetrahedron class
- Triangle class
- Conversion functions
- Polyhedra classes
- Visualization class

#### [MODULES.md](MODULES.md)
**Purpose**: Module-by-module documentation  
**Audience**: Developers and users wanting detailed module information  
**Contents**:
- Module purposes
- Class descriptions
- Method listings
- Usage examples
- Technical details

**Key Sections**:
- Core modules (vectors, tetrahedron, triangle, constants)
- Conversion module
- Polyhedra modules
- Visualization module

#### [BACKGROUND.md](BACKGROUND.md)
**Purpose**: Mathematical and theoretical background  
**Audience**: Users wanting to understand the mathematics  
**Contents**:
- Synergetics introduction
- IVM coordinate system
- Tetrahedral coordination
- Technical implementation details

#### [TECHNICAL_REFERENCE.md](TECHNICAL_REFERENCE.md)
**Purpose**: Deep technical reference for developers  
**Audience**: Advanced developers  
**Contents**:
- Method signatures
- Algorithm details
- Performance considerations
- Error handling
- Precision information
- Implementation details

### Development Documentation

#### [AGENTS.md](AGENTS.md)
**Purpose**: Development workflows and agent guidance  
**Audience**: Developers and AI agents  
**Contents**:
- Module structure overview
- Common workflows
- Testing procedures
- Utility scripts
- Extension points

#### [STRUCTURE.md](STRUCTURE.md)
**Purpose**: Package organization and structure  
**Audience**: Developers  
**Contents**:
- Directory structure
- Module responsibilities
- Import structure
- Test organization
- Statistics

#### [TESTING_SUMMARY.md](TESTING_SUMMARY.md)
**Purpose**: Testing overview and results  
**Audience**: Developers and QA  
**Contents**:
- Test execution results
- Test coverage
- Test files
- Verification status

#### [.cursorrules](.cursorrules)
**Purpose**: Development rules and guidelines  
**Audience**: Developers and AI agents  
**Contents**:
- Code style standards
- Testing requirements
- Module organization
- Documentation standards
- Code quality guidelines

## Documentation Coverage

### Complete Coverage ✅

All methods and classes are fully documented:

- ✅ **Vector Class**: 20+ methods documented with signatures, parameters, examples
- ✅ **Qvector Class**: All methods documented
- ✅ **Svector Class**: Documented with inheritance details
- ✅ **Tetrahedron Class**: All methods and internal calculations documented
- ✅ **Triangle Class**: All methods documented
- ✅ **Conversion Functions**: All 4 functions documented
- ✅ **Polyhedra Classes**: All 5 polyhedra documented
- ✅ **Polyhedron Base Class**: All methods documented
- ✅ **Edge Class**: Documented
- ✅ **Edge Counting Functions**: All 8 functions documented
- ✅ **Visualization Class**: All methods documented
- ✅ **Module-Level Functions**: All convenience functions documented

### Technical Details Included

- ✅ Method signatures with parameter types
- ✅ Return types
- ✅ Mathematical formulas
- ✅ Algorithm descriptions
- ✅ Performance considerations
- ✅ Error handling
- ✅ Precision information
- ✅ Code examples
- ✅ Edge cases

### Test Coverage

- ✅ **83+ tests** covering all functionality
- ✅ **11 test files** with comprehensive coverage
- ✅ All methods tested
- ✅ Edge cases tested
- ✅ Integration tests
- ✅ Visualization tests

## Finding Documentation

### By Topic

**Vector Operations**:
- Basic operations: [API.md](API.md#vector-class) - Vector Class
- Advanced operations: [API.md](API.md#vector-class) - Rotations, Spherical
- Module details: [MODULES.md](MODULES.md#vectorspy)

**Coordinate Conversion**:
- API Reference: [API.md](API.md#conversion-module)
- Technical Details: [TECHNICAL_REFERENCE.md](TECHNICAL_REFERENCE.md#algorithm-details)
- Module Details: [MODULES.md](MODULES.md#converterspy)

**Volume Calculations**:
- API Reference: [API.md](API.md#tetrahedron-class)
- Mathematical Background: [BACKGROUND.md](BACKGROUND.md)
- Technical Details: [TECHNICAL_REFERENCE.md](TECHNICAL_REFERENCE.md#algorithm-details)

**Polyhedra**:
- API Reference: [API.md](API.md#polyhedra-module)
- Module Details: [MODULES.md](MODULES.md#polyhedra-modules)
- Usage: [AGENTS.md](AGENTS.md#common-workflows)

**Visualization**:
- API Reference: [API.md](API.md#visualization-module)
- Module Details: [MODULES.md](MODULES.md#plotterpy)
- Examples: [AGENTS.md](AGENTS.md#visualization-module)

### By Use Case

**Getting Started**:
1. Read [README.md](../README.md)
2. Try examples from [MODULES.md](MODULES.md)
3. Reference [API.md](API.md) for specific methods

**Understanding the Math**:
1. Read [BACKGROUND.md](BACKGROUND.md)
2. Check [TECHNICAL_REFERENCE.md](TECHNICAL_REFERENCE.md) for formulas
3. See [API.md](API.md) for implementation details

**Development**:
1. Read [AGENTS.md](AGENTS.md) for workflows
2. Check [STRUCTURE.md](STRUCTURE.md) for organization
3. Review [.cursorrules](.cursorrules) for standards
4. See [TESTING_SUMMARY.md](TESTING_SUMMARY.md) for testing

**Advanced Usage**:
1. Read [TECHNICAL_REFERENCE.md](TECHNICAL_REFERENCE.md)
2. Check [API.md](API.md) for method signatures
3. Review [MODULES.md](MODULES.md) for module details

## Documentation Maintenance

### When to Update Documentation

- ✅ When adding new public methods or classes
- ✅ When changing method signatures
- ✅ When adding new features
- ✅ When fixing bugs that affect behavior
- ✅ When updating test coverage
- ✅ When changing package structure

### Documentation Standards

All documentation should:
- Include method signatures with types
- Provide code examples
- Explain mathematical background
- Document edge cases
- Include error conditions
- Show usage patterns

See [.cursorrules](.cursorrules) for detailed documentation standards.

## Quick Reference

### Common Tasks

**Create a Vector**:
```python
from ivm_xyz import Vector
v = Vector((1, 2, 3))
```
See: [API.md](API.md#vector-class) - `__init__`

**Convert Coordinates**:
```python
from ivm_xyz.conversion import xyz_to_ivm, ivm_to_xyz
quadray = xyz_to_ivm(1.0, 2.0, 3.0)
```
See: [API.md](API.md#conversion-module)

**Calculate Volume**:
```python
from ivm_xyz import Tetrahedron
tet = Tetrahedron(1, 1, 1, 1, 1, 1)
vol = tet.ivm_volume()
```
See: [API.md](API.md#tetrahedron-class)

**Visualize Polyhedron**:
```python
from ivm_xyz.visualization import PolyhedronPlotter
plotter = PolyhedronPlotter()
plotter.plot_polyhedron(vertices, faces, save=True)
```
See: [API.md](API.md#polyhedronplotter-class)

---

**Last Updated**: Documentation comprehensively reviewed and expanded  
**Status**: ✅ All methods, classes, and functions fully documented  
**Test Coverage**: 83+ tests, all passing

