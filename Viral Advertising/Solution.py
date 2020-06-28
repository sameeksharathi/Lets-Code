import math
import os
import random
import re
import sys

def viralAdvertising(n):
    l = [5]
    for i in range(n-1):
        x = (l[i]//2)*3
        l.append(x)
    f = [y//2 for y in l]
    return sum(f)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    result = viralAdvertising(n)
    fptr.write(str(result) + '\n')
    fptr.close()
