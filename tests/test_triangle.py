import math
import unittest

from triangle import classify_triangle, is_valid_triangle


def test_invalid_nonpositive_sides():
    assert classify_triangle(0, 2, 2) == "Invalid"
    assert classify_triangle(-1, 2, 2) == "Invalid"


def test_invalid_degenerate_boundary():
    assert not is_valid_triangle(1, 2, 3)
    assert classify_triangle(1, 2, 3) == "Invalid"


class TriangleTests(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertEqual(classify_triangle(4, 4, 4), "Equilateral")

    def test_isosceles_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 6), "Isosceles")

    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")

    def test_right_scalene_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Right Scalene")

    def test_right_isosceles_with_noninteger_sides(self):
        self.assertEqual(
            classify_triangle(5, 5, 5 * math.sqrt(2)),
            "Right Isosceles",
        )

    def test_right_angle_check_uses_tolerance(self):
        self.assertEqual(
            classify_triangle(1, 1, math.sqrt(2) * (1 + 1e-10)),
            "Right Isosceles",
        )

    def test_non_finite_side_is_invalid(self):
        self.assertEqual(classify_triangle(float("nan"), 2, 2), "Invalid")
        self.assertEqual(classify_triangle(float("inf"), 2, 2), "Invalid")