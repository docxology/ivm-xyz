# `examples/`

Runnable scripts demonstrating the public API. Run from the **repository root** with the package on `PYTHONPATH` (e.g. `uv run` after `uv sync`).

| Entry | What it is |
|-------|------------|
| [basic_usage.py](basic_usage.py) | One file covering vectors, conversion, `make_tet` / `make_tri`, and polyhedra (used by integration tests) |
| [visualization_examples.py](visualization_examples.py) | `PolyhedronPlotter` to the default `outputs/plots/` — requires **`[visualization]`** (matplotlib, imageio for GIF) |
| [orchestrators/](orchestrators/) | **Thin orchestrator scripts** — one small workflow per file ([index](orchestrators/README.md)) |

## Commands

```bash
uv run python examples/basic_usage.py
uv run python examples/visualization_examples.py
uv run python examples/orchestrators/orch_constants.py
uv run python examples/orchestrators/orch_triangle_class.py
# … see orchestrators/README.md for the full list
```

## Tests

`tests/test_integration_comprehensive.py` runs [basic_usage.py](basic_usage.py) with `PYTHONPATH=.` only. Other examples are not part of the default test gate.

See [AGENTS.md](AGENTS.md).
