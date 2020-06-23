'''
The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, 
its height increases by 1 meter.
Laura plants a Utopian Tree sapling with a height of 1 meter at the onset of spring. How tall will her tree be after n growth cycles?
For example, if the number of growth cycles is n=5, the calculations are as follows:

Period  Height
0          1
1          2
2          3
3          6
4          7
5          14

Input Format:
The first line contains an integer, t, the number of test cases.
t subsequent lines each contain an integer, n, denoting the number of cycles for that test case.

Output Format:
For each test case, print the height of the Utopian Tree after n cycles. Each height must be printed on a new line.
'''

import math
import os
import random
import re
import sys

def utopianTree(n):
    ans = 1
    for i in range(1,n+1):
        if(i%2!=0):
            ans = ans*2
        else:
            ans = ans+1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = utopianTree(n)
        fptr.write(str(result) + '\n')
    fptr.close()




