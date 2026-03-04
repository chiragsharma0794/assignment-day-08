PART B Q1
break stops the loop entirely and execution continues after the loop.
continue skips the remaining code in the current iteration and moves to the next iteration.

for else and while else
else runs only when the loop finishes without break.
Use case is search. If you find the item you break. If you never break then else tells you not found.

O(n) vs O(n squared
O(n) means work grows linearly with input size. One loop over n items.
O(n squared means work grows like n times n. Typical nested loops over the same list.

PART C

Exact prompt used
Write a Python program that prints a diamond pattern of asterisks. The user inputs the number of rows for the upper half. Include proper spacing and use nested loops only, no string multiplication tricks.

AI output summary
The AI generated two halves. First half increases stars from 1 to 2n minus 1 with leading spaces. Second half decreases back to 1.

Critical evaluation
Spacing correctness. Correct if the program prints n minus i spaces before 2i minus 1 stars.
Readability. Acceptable, but can be improved by reducing duplication and handling n equals 0 cleanly.
Edge cases. n equals 0 should print nothing or a blank line and exit without errors. n equals 1 should print a single star.
Nested loops vs string tricks. Must avoid using "*" * count or " " * count. Only loops should print characters.
Time complexity. Total printed characters grow proportional to n squared because each row prints up to O(n) characters and there are O(n) rows.

Improved version
See diamond_pattern.py function diamond_improved. It handles n less than or equal to 0 and uses while loops with explicit counters to satisfy the nested loop rule.