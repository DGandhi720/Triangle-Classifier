# Triangle-Classifier

`triangle.py` provides `is_valid_triangle(a, b, c)` and `classify_triangle(a, b, c)`.
The classifier returns `Invalid`, `Equilateral`, `Isosceles`, or `Scalene`, and prefixes
right triangles with `Right `. Its right-angle check uses a floating-point tolerance.

An equilateral triangle cannot also be right: if each side is `s`, the Pythagorean
theorem would require `s^2 + s^2 = s^2`, which is impossible for a positive side length.

Run the unit and acceptance tests with:

```sh
python3 -m unittest discover -s tests -v
```