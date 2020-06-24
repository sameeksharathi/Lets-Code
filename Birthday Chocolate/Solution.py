import math
import os
import random
import re
import sys
from itertools import combinations

def birthday(s, d, m):
    count = 0
    currentSum = 0

    for i in range(0, len(s)):
        currentSum += s[i]

        if i >= m-1:
            if currentSum == d:
                count += 1
            currentSum -= s[i-(m-1)]
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
