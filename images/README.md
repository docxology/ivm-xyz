# `images/`

**v0.2.0:** the default [PolyhedronPlotter](../ivm_xyz/visualization/plotter.py) directory is [`outputs/plots`](../outputs/README.md). Use `output_folder="images"` only if you want this legacy path.

**Git note:** [../.gitignore](../.gitignore) still ignores `images/*.png` and `images/*.gif` for projects that write here. The [outputs/](../outputs/) tree is the canonical default for new runs.

Markdown in this directory **is** tracked. New binaries written here are ignored by `.gitignore`; the five `.gif` renders kept from v0.1 (`cube`, `dodecahedron`, `octahedron`, `pyramid`, `tetrahedron`) remain tracked for reference.

See [AGENTS.md](AGENTS.md).
