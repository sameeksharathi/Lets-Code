import math
import os
import random
import re
import sys

def plusMinus(arr):
    l = len(arr)
    p,n,z = 0,0,0
    for x in arr:
        if x>0:
            p+=1
        elif x<0:
            n+=1
        elif x==0:
            z+=1
    print(p/l)
    print(n/l)
    print(z/l)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
