# Triangle-Classifier

AI DISCLOSURE!!
----------------------
In this program, I used the Github Co-pilot in order to structure the program, and get it started. 
As requested and asked by the rules of the assignment, Copilot was used as an agent and used as assistance for the pytests.
I verified the work of the AI, and if any changes were necessary, they were made to verify all works in order.
Requirements.txt is written fully by human, and the code in test_triangle_acceptance.py was written by my own hand. The AI agent(Copilot, in this case) was not involved. 
All human work requested was done as human work. 





To run the program, 
python3 -m pip install pytest
python3 -m pytest
then python3 -m pytest -v


Question: An equilateral triangle can never also be right — explain why, in one or two sentences, in your README.

An equilateral triangle has three 60° angles. A right triangle has a 90° angle, so because of that, an equilateral is incapable of being a right triangle.



(Note about the review log, the formatting may be messed up, so the cleanest edition of it may be best reviewed in the codespace, or the file itself. Apologies, and please do this for the best coherence)

## Copilot Review Log               Co-pilot Suggested          Kept, Edited, Rejected      Why
                                                                                   
test_invalid_nonpositive_sides           Yes                    Kept            
test_invalid_degenerate_boundary         Yes                    Kept                
test_equilateral_triangle                Yes                    Kept
test_isosceles_triangle                  Yes                    Kept
test_scalene_triangle                    Yes                    Kept
test_right_scalene_triangle              Yes                   Edited      The original followed the "==" format, so this was edited to include checks the Pythagorean theorem with math.isclose()
test_right_isosceles_with_noninteger_sides Yes                 Edited         These follow the above change too. Edited to include checks with math.isclose()
test_right_angle_check_uses_tolerance    Yes                   Edited          This does as well. Edited to include checks with math.isclose()
test_non_finite_side_is_invalid          Yes                    Kept


All that were kept were tested to make sure they worked, and fulfilled what was needed by the triangle classifier. Incase this doesn't remain the case, please let me know.