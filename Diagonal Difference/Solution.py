import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    sum1=0
    sum2=0
    j = len(arr[0])-1
    for i in range(len(arr[0])):
        sum1+=arr[i][i]
    for i in range(len(arr[0])):
        sum2+=arr[i][j]
        j-=1
    return abs(sum2-sum1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
