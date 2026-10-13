import math


def is_valid_triangle(a: float, b: float, c: float) -> bool:
    sides = (a, b, c)
    if not all(math.isfinite(side) and side > 0 for side in sides):
        return False

    smallest, middle, largest = sorted(sides)
    return smallest + middle > largest


def classify_triangle(a: float, b: float, c: float) -> str:
    if not is_valid_triangle(a, b, c):
        return "Invalid"
    if a == b == c:
        classification = "Equilateral"
    elif a == b or b == c or a == c:
        classification = "Isosceles"
    else:
        classification = "Scalene"
    smallest, middle, largest = sorted((a, b, c))
    normalized_square_sum = (smallest / largest) ** 2 + (middle / largest) ** 2
    if math.isclose(normalized_square_sum, 1.0, rel_tol=1e-9, abs_tol=1e-12):
        return f"Right {classification}"

    return classification