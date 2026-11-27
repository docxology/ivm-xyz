# `tests/`

Run the full suite from the **repository root** with the `dev` extra. The
coverage-gap tests import `pytest` during discovery with either runner.

```bash
uv run --extra dev pytest tests/
uv run --extra dev python -m unittest discover tests
```

To run an individual `unittest` module without extras:

```bash
uv run python -m unittest tests.test_conversion
```

- **Optional deps**: `tests/_support/optional_deps.py` — visualization tests **skip** if `matplotlib` is missing.
- **Shared data**: `tests/_support/fixtures.py` (e.g. simplex vertices/faces).

See [AGENTS.md](AGENTS.md).
