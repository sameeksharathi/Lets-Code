import math
import os
import random
import re
import sys

def staircase(n):
    for j in range(1,n+1):
        print(' '*(n-j)+'#'*j)


if __name__ == '__main__':
    n = int(input())
    staircase(n)
