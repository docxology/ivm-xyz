# `ivm_xyz.conversion`

## API ([`converters.py`](converters.py))

| Function | Purpose |
|----------|---------|
| `xyz_to_ivm(x, y, z)` | Cartesian → quadray (4-tuple) |
| `ivm_to_xyz(a, b, c, d)` | Quadray → Cartesian (3-tuple) |
| `vector_to_qvector(vector)` | `Vector` → `Qvector` |
| `qvector_to_vector(qvector)` | `Qvector` → `Vector` |

Package [`__init__.py`](__init__.py) exports `xyz_to_ivm`, `ivm_to_xyz` only; import `converters` directly for vector helpers.

## Tests

- `tests/test_conversion.py`
- `tests/test_functional_comprehensive.py`, `tests/test_integration_comprehensive.py`
