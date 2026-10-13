import math
import unittest

from triangle import classify_triangle, is_valid_triangle


class IsValidTriangleTests(unittest.TestCase):
    def test_rejects_nonpositive_sides(self):
        self.assertFalse(is_valid_triangle(0, 2, 2))
        self.assertFalse(is_valid_triangle(-1, 2, 2))

    def test_rejects_degenerate_triangle(self):
        self.assertFalse(is_valid_triangle(1, 2, 3))

    def test_rejects_non_finite_sides(self):
        self.assertFalse(is_valid_triangle(float("nan"), 2, 2))
        self.assertFalse(is_valid_triangle(float("inf"), 2, 2))

    def test_accepts_valid_triangle(self):
        self.assertTrue(is_valid_triangle(3, 4, 5))


class ClassifyTriangleTests(unittest.TestCase):
    def test_classifies_invalid_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "Invalid")

    def test_classifies_equilateral_triangle(self):
        self.assertEqual(classify_triangle(4, 4, 4), "Equilateral")

    def test_classifies_isosceles_triangle(self):
        self.assertEqual(classify_triangle(5, 5, 6), "Isosceles")

    def test_classifies_scalene_triangle(self):
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")

    def test_prefixes_right_triangle_classification(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Right Scalene")
        self.assertEqual(classify_triangle(1, 1, math.sqrt(2)), "Right Isosceles")

    def test_right_angle_check_uses_tolerance(self):
        self.assertEqual(
            classify_triangle(1, 1, math.sqrt(2) * (1 + 1e-10)),
            "Right Isosceles",
        )


if __name__ == "__main__":
    unittest.main()