from triangle import classify_triangle

def test_customer_triangle_classification_requirements():
    cases = (
        ((0, 4, 5), "Invalid"),
        ((1, 2, 3), "Invalid"),
        ((6, 6, 6), "Equilateral"),
        ((5, 5, 6), "Isosceles"),
        ((4, 5, 6), "Scalene"),
    )
#This will label each triangle, minus the ones that were specified by the customer, in this case, right triangles.
    for sides, expected in cases:
        assert classify_triangle(*sides) == expected, f"Unacceptable amount for {sides}"
#In this part of the program, the program tests for right triangles. 
def test_right_triangle_flagged_for_reinforcement():
    """This triangle is a right triangle. It requries reinforced corners."""
    assert classify_triangle(3, 4, 5) == "Right Scalene"

def test_non_right_triangle_flagged_reinforcement():
    assert classify_triangle(4, 5, 6) == "Scalene"
    #This one is under the case that the triangle isn't right.

    #If all is correct, all tests should pass, and it should match the text that I wrote down in requirements.txt