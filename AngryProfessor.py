'''
A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline,
he decides to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time 
(arrivalTime<=0) to arrived late (arrivalTime>0).

Given the arrival time of each student and a threshhold number of attendees, determine if the class is canceled.

Input Format:
The first line of input contains t, the number of test cases.
Each test case consists of two lines.
The first line has two space-separated integers, n and k, the number of students (size of a) and the cancellation threshold.
The second line contains n space-separated integers (a[1],a[2],....,a[n]) describing the arrival times for each student.

Output Format:
For each test case, print the word YES if the class is canceled or NO if it is not.
'''



import math
import os
import random
import re
import sys

def angryProfessor(k, a):
    c = 0
    for i in a:
        if i<=0:
            c+=1
    if c>=k:
        return 'NO'
    else:
        return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        a = list(map(int, input().rstrip().split()))
        result = angryProfessor(k, a)
        fptr.write(result + '\n')
    fptr.close()
