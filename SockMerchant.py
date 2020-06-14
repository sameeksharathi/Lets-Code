'''
John works at a clothing store. He has a large pile of socks that he must pair by color for sale.
Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are n=7 socks with colors ar=[1,2,1,2,1,3,2]. There is one pair of color 1 and one of color 2.
There are three odd socks left, one of each color. The number of pairs is 2.

Input Format:
The first line contains an integer n, the number of socks represented in ar.
The second line contains n space-separated integers describing the colorsar[i]  of the socks in the pile.

Output Format:
Return the total number of matching pairs of socks that John can sell.
'''



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
