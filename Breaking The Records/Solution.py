import math
import os
import random
import re
import sys

def breakingRecords(scores):
    min, max = scores[0], scores[0]
    mn,mx=0,0
    for i in scores[1:]:
        if(i<min and i<max):
            min=i
            mn+=1
        elif (i>min and i<max):
            continue
        elif (i>min and i>max):
            max=i
            mx+=1
        elif (i==min or i==max):
            continue
    return [mx,mn]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
    
