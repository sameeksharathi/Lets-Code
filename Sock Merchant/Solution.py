import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    s = list(set(ar))
    cnt = [ar.count(i) for i in s]
    ans=0
    for i in cnt:
        if i%2==0:
            ans+=i//2
        elif (i-1)%2==0 and (i-1)!=0:
            ans+=(i-1)//2
    return ans 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
