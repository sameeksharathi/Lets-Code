import math
import os
import random
import re
import sys

def dayOfProgrammer(year):
    if year<=1917:
        if year%4==0:
            feb = 29
        else:
            feb=28
        day = 256 - (31*5 + 30*2 +feb)
        return str(day)+'.09.'+str(year)
    elif year>=1919:
        if year%400==0 or (year%4==0 and year%100!=0):
            feb = 29
        else:
            feb=28
        day = 256 - (31*5 + 30*2 +feb)
        return str(day)+'.09.'+str(year)
    else:
        day = 256 - (31*5+28-13+30*2)
        return str(day)+'.09.'+str(year)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    year = int(input().strip())
    result = dayOfProgrammer(year)
    fptr.write(result + '\n')
    fptr.close()
    
