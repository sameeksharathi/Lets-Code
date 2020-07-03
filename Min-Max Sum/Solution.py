import math
import os
import random
import re
import sys
from itertools import combinations

def miniMaxSum(arr):
    l = list(combinations(arr,4))
    s = [sum(x) for x in l]
    print(min(s),max(s))
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
