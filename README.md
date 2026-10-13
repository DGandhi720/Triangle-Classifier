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
                                                                                    I made the two boundary tests standalone pytest tests and kept the triangle classification tests in a unittest.TestCase class. This separates the validity and boundary checks from classification checks, though the file now uses both testing styles. Both pytest and unittest can discover tests in the file, but unittest runs only the tests in the TestCase class.
test_invalid_nonpositive_sides           Yes                    Kept            
test_invalid_degenerate_boundary         Yes                    Kept                
test_equilateral_triangle                Yes                    Edited
test_isosceles_triangle                  Yes                    Edited
test_scalene_triangle                    Yes                    Edited
test_right_scalene_triangle              Yes                    Edited
test_right_isosceles_with_noninteger_sides Yes                  Edited
test_right_angle_check_uses_tolerance    Yes                    Edited 
test_non_finite_side_is_invalid          Yes                    Edited

```sh
python3 -m pytest
```