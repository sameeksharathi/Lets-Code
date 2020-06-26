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

