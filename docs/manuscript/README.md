# Reproduce the IVM-XYZ geometry manuscript

The manuscript checks coordinate conversion across the Cartesian octants and
measures a regular tetrahedron using the public APIs. The replay writes a
numerical receipt and a native plot.

Install Git, uv, Pandoc with matching pandoc-crossref, and XeLaTeX. From the
IVM-XYZ checkout, use a separate Template checkout.

```sh
template_dir=/absolute/path/to/template
project_dir="$template_dir/projects/working/ivm-xyz"
git -C "$template_dir" switch --detach 87704feae0a4490ef7dad9c931d268e8c30273c2
mkdir -p "$template_dir/projects/working"
git worktree add --detach "$project_dir" HEAD
cd "$template_dir"
uv sync --locked --python 3.14 --no-dev
(cd "$project_dir" && MPLBACKEND=Agg "$template_dir/.venv/bin/python" -m docs.reproduce_geometry)
uv run --no-sync python scripts/pipeline/stage_03_render.py --project working/ivm-xyz
uv run --no-sync python scripts/pipeline/stage_04_validate.py --project working/ivm-xyz
```

The PDF, HTML, plot, numerical receipt, and validator reports are under
`projects/working/ivm-xyz/output/`. [Template prerequisites](https://github.com/docxology/template/blob/87704feae0a4490ef7dad9c931d268e8c30273c2/docs/RUN_GUIDE.md)
