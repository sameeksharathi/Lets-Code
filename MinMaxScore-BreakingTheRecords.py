'''Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. 
She tabulates the number of times she breaks her season record for most points and least points in a game. 
Points scored in the first game establish her record for the season, and she begins counting from there.

For example, assume her scores for the season are represented in the array scores=[12,24,10,24]. 
Scores are in the same order as the games played. She would tabulate her results as follows:

                                 Count
Game  Score  Minimum  Maximum   Min Max
 0      12     12       12       0   0
 1      24     12       24       0   1
 2      10     10       24       1   1
 3      24     10       24       1   1
 
Given Maria's scores for a season, find and print the number of times she breaks her records for most and least points scored during the season.

Input Format:
The first line contains an integer n, the number of games.
The second line contains n space-separated integers describing the respective values of score0, score1, score2-------,score(n-1).'''

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
