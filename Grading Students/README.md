<h1>Grading Students</h1>
HackerLand University has the following grading policy:
Every student receives a grade in the inclusive range from 0 to 100.
Any grade less than 40 is a failing grade.
Sam is a professor at the university and likes to round each student's grade according to these rules:
If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
For example,grade=84  will be rounded to 85 but grade=29 will not be rounded because the rounding would result in a number that is less than 40.<br>
Given the initial value of grade for each of Sam's n students, write code to automate the rounding process.

<hr>
<h2>Input Format</h2>
The first line contains a single integer, n, the number of students.<br>
Each line i of the n subsequent lines contains a single integer, garde[i], denoting student i's grade.

<h2>Constraints</h2>
1 <= n <= 60 and 0 <= grade[i] <= 100

<h2>Output Format</h2>
For each grade[i], print the rounded grade on a new line.
