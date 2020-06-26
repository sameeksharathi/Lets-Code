import math
import os
import random
import re
import sys

def gradingStudents(grades):
    x = []
    for grade in grades:
        g = str(grade)
        if int(g[-1])>=3 and int(g[-1])<=5 and int(g)>=38:
            x.append(g[:-1]+'5')
        elif int(g[-1])>7 and int(g[-1])<10 and int(g)>=38:
            x.append(str(int(g[:-1])+1)+'0')
        else:
            x.append(g)
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

