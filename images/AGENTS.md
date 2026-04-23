# `images/` — agent reference

- Treat as **artifact output**, not source code.
- **v0.2.0+** default plot output is under [`../outputs/plots`](../outputs/README.md); this folder is for explicit `output_folder="images"`.
- For plot verification, use `tests/test_visualization*.py` with a temporary directory (tests already use `tempfile`).
