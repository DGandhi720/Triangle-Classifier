from triangle import classify_triangle

#Acceptance test for the requirements.txt
def test_customer_requirements_for_invalid_and_right_triangles():
    "If a piece is invalid, an invalid text will be returned. If it is right, the program will pass a test for it to be approved for reinforcement."
    assert classify_triangle(1, 2, 3) == "Invalid"
    assert classify_triangle(3, 4, 5) == "Right Scalene"
#If all works well(and from my testing) this should return as such requested by the customer's requirements, from the txt file. 