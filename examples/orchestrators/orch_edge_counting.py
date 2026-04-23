"""
Edge / contact counts for frequency f (synergetics-style ball packing).

Run from repo root: uv run python examples/orchestrators/orch_edge_counting.py
"""

from ivm_xyz.polyhedra import (
    tet_edges,
    half_oct_edges,
    oct_edges,
    cubocta_edges,
    cubocta_layer,
)


def main() -> None:
    print("=== Edge counting (sample frequencies f = 1..4) ===")
    for f in (1, 2, 3, 4):
        print(f"  f={f}")
        print(f"    tet_edges        = {tet_edges(f)}")
        print(f"    half_oct_edges   = {half_oct_edges(f)}")
        print(f"    oct_edges        = {oct_edges(f)}")
        print(f"    cubocta_edges    = {cubocta_edges(f)}")
        print(f"    cubocta_layer    = {cubocta_layer(f)}")


if __name__ == "__main__":
    main()
