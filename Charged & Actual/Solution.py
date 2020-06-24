import math
import os
import random
import re
import sys

def bonAppetit(bill, k, b):
    bill.remove(bill[k])
    pay = sum(bill)//2
    if pay==b:
        print('Bon Appetit')
    else:
        print(b-pay)
    
if __name__ == '__main__':
    nk = input().rstrip().split()
    n = int(nk[0])
    k = int(nk[1])
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    bonAppetit(bill, k, b)
