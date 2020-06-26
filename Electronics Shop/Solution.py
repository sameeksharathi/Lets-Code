import os
import sys
from itertools import product

def getMoneySpent(keyboards, drives, b):
    l = list(product(keyboards,drives))
    lis = [sum(i) for i in l]
    f = []
    for i in lis:
        if(i<=b):
            f.append(i)
    if f==[]:
        return -1
    else:
        return max(f)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #
    
    moneySpent = getMoneySpent(keyboards, drives, b)
    fptr.write(str(moneySpent) + '\n')
    fptr.close()
