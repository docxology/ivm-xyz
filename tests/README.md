# `tests/`

`unittest` discovery against this package. Run from the **repository root**:

```bash
uv run python -m unittest discover tests
uv run pytest tests/
```

- **Optional deps**: `tests/_support/optional_deps.py` — visualization tests **skip** if `matplotlib` is missing.
- **Shared data**: `tests/_support/fixtures.py` (e.g. simplex vertices/faces).

See [AGENTS.md](AGENTS.md).
