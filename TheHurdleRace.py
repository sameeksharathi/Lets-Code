'''
Dan is playing a video game in which his character competes in a hurdle race. Hurdles are of varying heights, and Dan has a
maximum height he can jump. There is a magic potion he can take that will increase his maximum height by 1 unit for each dose. 
How many doses of the potion must he take to be able to jump all of the hurdles.
Given an array of hurdle heights height, and an initial maximum height Dan can jump, k, determine the minimum number of doses Dan must
take to be able to clear all the hurdles in the race.
For example, if height = [1,2,3,3,2] and Dan can jump 1 unit high naturally, he must take 3-1=2 doses of potion to be able to jump all
of the hurdles.

Input Format:
The first line contains two space-separated integers n and k, the number of hurdles and the maximum height Dan can jump naturally.
The second line contains n space-separated integers height[i] where 0 <= i < n.

Output Format:
Print an integer denoting the minimum doses of magic potion Dan must drink to complete the hurdle race.
'''


import math
import os
import random
import re
import sys

def hurdleRace(k, height):
    m = max(height)
    if (m<k):
        return 0
    else:
        return m-k

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    height = list(map(int, input().rstrip().split()))
    result = hurdleRace(k, height)
    fptr.write(str(result) + '\n')
    fptr.close()
