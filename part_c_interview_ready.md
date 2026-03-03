# Part C: Interview Ready

## Q1: Difference between elif and multiple if

elif chain:
Only one matching branch runs. Once a condition is true, the rest are skipped.

multiple if statements:
Each condition is checked independently. More than one block can run.

Example where outputs differ

Input:
x = 15

Code using multiple if:
if x > 0:
    print("positive")
if x > 10:
    print("large")

Output:
positive
large

Code using elif:
if x > 0:
    print("positive")
elif x > 10:
    print("large")

Output:
positive

Why:
In elif, the second condition is not checked if the first one is true.

## Q2: classify_triangle(a, b, c)

Edge cases handled:
Zero values, negative values, invalid triangle condition.

Python code:

def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a triangle"
    x, y, z = sorted([a, b, c])
    if z >= x + y:
        return "Not a triangle"
    if a == b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        return "Isosceles"
    return "Scalene"

## Q3: Debug / Analyze

Given code:
score = 85

if score >= 60:
    grade = 'D'
if score >= 70:
    grade = 'C'
if score >= 80:
    grade = 'B'
if score >= 90:
    grade = 'A'

print(grade)

Bug:
grade is not defined if score is below 60. That causes an error.
Also, the logic is fragile because grade is overwritten multiple times.

Why wrong:
For score < 60, the print statement fails because grade never gets assigned.

Correct fix:
Use a proper if elif else ladder from highest to lowest and include an else.

Example fix:
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"