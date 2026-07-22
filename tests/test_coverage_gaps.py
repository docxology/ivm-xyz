"""
Targeted tests for public APIs that the broader suite did not exercise.

Covers the module-level vector helpers, Qvector comparison/normalisation,
the Svector spherical subclass, ``Vector.spherical`` sign branches, the
closed-form edge-counting formulas, and ``Edge`` representation.
"""

import math

import pytest

from ivm_xyz.core.vectors import (
    IVM,
    Qvector,
    Svector,
    Vector,
    angle,
    cross,
    dot,
    length,
)
from ivm_xyz.polyhedra import edge_counting
from ivm_xyz.polyhedra.base import Edge


# --- module-level convenience functions -------------------------------------
def test_module_dot():
    assert dot(Vector((1, 0, 0)), Vector((1, 0, 0))) == pytest.approx(1.0)
    assert dot(Vector((1, 0, 0)), Vector((0, 1, 0))) == pytest.approx(0.0)


def test_module_cross():
    result = cross(Vector((1, 0, 0)), Vector((0, 1, 0)))
    assert (result.x, result.y, result.z) == pytest.approx((0.0, 0.0, 1.0))


def test_module_length():
    assert length(Vector((3, 4, 0))) == pytest.approx(5.0)


def test_module_angle():
    assert angle(Vector((1, 0, 0)), Vector((0, 1, 0))) == pytest.approx(90.0)


def test_vector_repr():
    assert repr(Vector((1, 2, 3))) == "XYZ(x=1.0, y=2.0, z=3.0)"


def test_vector_truediv():
    result = Vector((2, 4, 6)) / 2
    assert (result.x, result.y, result.z) == pytest.approx((1.0, 2.0, 3.0))


def test_qvector_angle():
    q1 = Vector((1, 0, 0)).quadray()
    q2 = Vector((0, 1, 0)).quadray()
    assert q1.angle(q2) == pytest.approx(90.0)


# --- Qvector comparison / hashing / normalisation ---------------------------
def test_qvector_ordering_and_equality():
    q1 = Qvector((1, 0, 0, 0))
    q2 = Qvector((0, 1, 0, 0))
    assert q1 == Qvector((1, 0, 0, 0))
    assert q1 > q2
    assert q2 < q1
    assert q1 != q2


def test_qvector_eq_with_non_qvector_is_false():
    assert (Qvector((1, 0, 0, 0)) == "not a qvector") is False


def test_qvector_hashable():
    members = {Qvector((1, 0, 0, 0)), Qvector((1, 0, 0, 0)), Qvector((0, 1, 0, 0))}
    assert len(members) == 2


def test_qvector_norm0_sums_to_zero():
    q = Qvector((3, 1, 0, 0))
    assert sum(q.norm0()) == pytest.approx(0.0)


def test_qvector_length_nonnegative():
    assert Qvector((2, 1, 0, 0)).length() >= 0.0


def test_vector_quadray_roundtrip():
    v = Vector((0.5, 0.25, -0.75))
    back = v.quadray().xyz()
    assert (back.x, back.y, back.z) == pytest.approx((v.x, v.y, v.z))


def test_ivm_namedtuple_fields():
    coords = IVM(1.0, 2.0, 3.0, 4.0)
    assert (coords.a, coords.b, coords.c, coords.d) == (1.0, 2.0, 3.0, 4.0)


# --- Svector -----------------------------------------------------------------
def test_svector_repr_and_roundtrip():
    s = Svector((1.0, 0.0, 0.0))
    assert repr(s).startswith("Svector")
    # A vector along +x has unit length preserved through spherical conversion.
    assert s.length() == pytest.approx(1.0)


# --- Vector.spherical sign branches -----------------------------------------
@pytest.mark.parametrize(
    "vec",
    [
        (0, 0, 0),  # r == 0 -> phi == 0, theta == 0
        (0, 1, 0),  # x == 0, y > 0 -> theta == 90
        (0, -1, 0),  # x == 0, y < 0 -> theta == -90
        (-1, 0, 0),  # x < 0, y == 0 -> theta == 180
        (-1, -1, 0),  # x < 0, y < 0
        (-1, 1, 0),  # x < 0, y > 0
    ],
)
def test_spherical_branches_return_three_values(vec):
    r, phi, theta = Vector(vec).spherical()
    assert all(math.isfinite(component) for component in (r, phi, theta))


def test_spherical_origin_is_zero():
    r, phi, theta = Vector((0, 0, 0)).spherical()
    assert (r, phi, theta) == (0.0, 0.0, 0.0)


# --- edge_counting closed forms match iterative implementations -------------
@pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
def test_closed_form_edge_formulas(n):
    assert edge_counting.a007531(n) == edge_counting.tet_edges(n)
    assert edge_counting.a035006(n) == edge_counting.half_oct_edges(n)
    assert edge_counting.a300758(n) == edge_counting.oct_edges(n)


# --- Edge representation -----------------------------------------------------
def test_edge_repr():
    edge = Edge(Qvector((1, 0, 0, 0)), Qvector((0, 1, 0, 0)))
    text = repr(edge)
    assert text.startswith("Edge from")
