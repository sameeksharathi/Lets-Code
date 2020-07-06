import math
import os
import random
import re
import sys

def permutationEquation(p):
    n = len(p)
    l = []
    for x in range(1,n+1):
        i = p.index(x)+1
        for z in range(1,n+1):
            y = p.index(i)+1
        l.append(y)
    return l
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    p = list(map(int, input().rstrip().split()))
    result = permutationEquation(p)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
