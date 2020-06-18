'''
Monica wants to buy a keyboard and a USB drive from her favorite electronics store. The store has several models of each.
Monica wants to spend as much as possible for the 2 items, given her budget.
Given the price lists for the store's keyboards and USB drives, and Monica's budget, find and print the amount of money Monica will spend.
If she doesn't have enough money to both a keyboard and a USB drive, print -1 instead. She will buy only the two required items.
For example, suppose she has b=60 to spend. Three types of keyboards cost keyboards=[40,50,60]. Two USB drives cost drives=[5,8,12].
She could purchase a 40keyboard + 12USB drive = 52, or a 50keyboard + 8USB drive = 58.She chooses the latter. She can't buy more than 
2 items so she can't spend exactly 60.

Input Format:
The first line contains three space-separated integers b, n, and m, her budget, the number of keyboard models and the number of USB drive models.
The second line contains n space-separated integers keyborad[i], the prices of each keyboard model.
The third line contains m space-separated integers drives, the prices of the USB drives.

Output Format:
Print a single integer denoting the amount of money Monica will spend. If she doesn't have enough money to buy one keyboard and
one USB drive, print -1 instead.
'''


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
