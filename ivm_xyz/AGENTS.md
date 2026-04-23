# `ivm_xyz` — agent reference

## Public surface

- **Top-level** ([`__init__.py`](__init__.py)): `Vector`, `Qvector`, `Tetrahedron`, `make_tet`, `Triangle`, `make_tri`, `xyz_to_ivm`, `ivm_to_xyz`, `__version__`.
- **Subpackages** re-export broader symbols; see each subfolder `AGENTS.md`.

## Dependencies

- **Required**: `numpy`.
- **Optional**: `matplotlib`, `imageio` (visualization extra in `pyproject.toml`).

## Tests

| Area | Test files |
|------|------------|
| Vectors, tetrahedra, triangles | `tests/test_vectors.py`, `test_vector_advanced.py`, `test_tetrahedron.py`, `test_triangle.py` |
| Conversion | `tests/test_conversion.py` |
| Polyhedra | `tests/test_polyhedra.py` |
| Functional / integration | `tests/test_functional_comprehensive.py`, `test_integration_comprehensive.py` |
| Visualization | `tests/test_visualization*.py` (skipped without matplotlib) |

## Layout

```
core/          # vectors, tetrahedron, triangle, constants
conversion/    # xyz ↔ quadray
polyhedra/     # Polyhedron, platonic solids, edge counts
visualization/ # PolyhedronPlotter (requires matplotlib)
```
