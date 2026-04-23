# `ivm_xyz.core`

## Exports ([`__init__.py`](__init__.py))

- `Vector`, `Qvector` — [`vectors.py`](vectors.py)
- `Tetrahedron`, `make_tet` — [`tetrahedron.py`](tetrahedron.py)
- `Triangle`, `make_tri` — [`triangle.py`](triangle.py)
- `constants` — star-imported from [`constants.py`](constants.py) (see file for names)

## Tests

- `tests/test_vectors.py`, `tests/test_vector_advanced.py`
- `tests/test_tetrahedron.py`, `tests/test_triangle.py`
- Covered indirectly in `tests/test_functional_comprehensive.py`, `test_integration_comprehensive.py`

## Invariants

- `Vector` / `Qvector` operations are numpy-backed where applicable; lengths and conversions should round-trip within documented precision (see tests for `isclose` / `AlmostEqual` usage).
