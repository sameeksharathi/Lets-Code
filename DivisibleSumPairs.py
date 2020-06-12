'''
You are given an array of n integers, ar=[ar[0],ar[1],.......,ar[n-1]], and a positive integer, k. Find and print the number of (i,j) pairs
where i<j and ar[i] + ar[j] is divisible by k.
For example, ar=[1,2,3,4,5,6] and k=5. Our three pairs meeting the criteria are [1,4],[2,3] and [4,6].

Input Format:
The first line contains 2 space-separated integers, n and k.
The second line contains n space-separated integers describing the values of ar[0],ar[1],..,ar[n-1].

Output Format:
Print the number of (i,j) pairs where i<j and ar[i] + ar[j] is evenly divisible by k.
'''



import math
import os
import random
import re
import sys
from itertools import combinations

def divisibleSumPairs(n, k, ar):
    l = list(combinations(ar,2))
    ans=0
    for i,j in l:
        if (i+j)%k==0:
            ans+=1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    ar = list(map(int, input().rstrip().split()))
    result = divisibleSumPairs(n, k, ar)
    fptr.write(str(result) + '\n')
    fptr.close()

