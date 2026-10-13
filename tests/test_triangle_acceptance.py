import unittest

from triangle import classify_triangle


class CustomerRequirementsAcceptanceTests(unittest.TestCase):
    def test_customer_triangle_classification_requirements(self):
        cases = (
            ((0, 4, 5), "Invalid"),
            ((1, 2, 3), "Invalid"),
            ((6, 6, 6), "Equilateral"),
            ((5, 5, 6), "Isosceles"),
            ((4, 5, 6), "Scalene"),
            ((3, 4, 5), "Right Scalene"),
        )

        for sides, expected in cases:
            with self.subTest(sides=sides):
                self.assertEqual(classify_triangle(*sides), expected)


if __name__ == "__main__":
    unittest.main()