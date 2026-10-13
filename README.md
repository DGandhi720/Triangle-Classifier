# Triangle-Classifier

AI DISCLOSURE!!
----------------------
In this program, I used the Github Co-pilot in order to structure the program, and get it started. 
As requested and asked by the rules of the assignment, Copilot was used as an agent and used as assistance for the first 5 pytests.
I verified the work of the AI, and if any changes were necessary, they were made to verify all works in order.
All human work requested was done as human work.



Question: An equilateral triangle can never also be right — explain why, in one or two sentences, in your README.

An equilateral triangle can never be right, because a right angle will always contain one 90 degree angle, and as a result, all sides will not be proper to equal 180. An equilateral triangle will always have 3 sides equal to 180 degrees, with a 3x60 format.

## Copilot Review Log               Co-pilot Suggested          Kept, Edited, Rejected      Why
                                                                                   
test_invalid_nonpositive_sides           Yes                    Kept            
test_invalid_degenerate_boundary         Yes                    Kept                
test_equilateral_triangle                Yes                    Kept
test_isosceles_triangle                  Yes                    Kept
test_scalene_triangle                    Yes                    Kept
test_right_scalene_triangle              Yes                   Edited          Edited to include checks the Pythagorean theorem with math.isclose()
test_right_isosceles_with_noninteger_sides Yes                 Edited          Edited to include checks with math.isclose()
test_right_angle_check_uses_tolerance    Yes                   Edited          Edited to include checks with math.isclose()
test_non_finite_side_is_invalid          Yes                    Kept







```sh
python3 -m pytest
```