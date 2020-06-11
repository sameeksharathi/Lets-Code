''' Question:
When you select a contiguous block of text in a PDF viewer, the selection is highlighted with a blue rectangle.
In this PDF viewer, each word is highlighted independently.

In this challenge, you will be given a list of letter heights in the alphabet and a string.
Using the letter heights given, determine the area of the rectangle highlight in mm^2 assuming all letters are 1mm wide.

For example, the highlighted word = torn. Assume the heights of the letters are t=2,o=1,r=1 and n=1. The tallest letter is 2 high and there
are 4 letters.The hightlighted area will be 2*4=8 mm^2 so the answer is 8.

Function Description:
Complete the designerPdfViewer function in the editor below. It should return an integer representing the size of the highlighted area.
designerPdfViewer has the following parameter(s):
h: an array of integers representing the heights of each letter
word: a string

Input Format:
The first line contains 26 space-separated integers describing the respective heights of each consecutive lowercase English letter, 
ascii[a-z].
The second line contains a single word, consisting of lowercase English alphabetic letters.

Output Format:
Print a single integer denoting the area in mm^2 of highlighted rectangle when the given word is selected. Do not print units of measure.

Sample Input 1:
1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7
zaba
Sample Output 1: 
28
'''

import math
import os
import random
import re
import sys

def designerPdfViewer(h, word):
    w = sorted(word)
    index = [ord(w[i])-97 for i in range(len(w))]
    v = []
    for i in index:
        v.append(h[i])
    m = max(v)
    ans = m* len(w)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    h = list(map(int, input().rstrip().split()))
    word = input()
    result = designerPdfViewer(h, word)
    fptr.write(str(result) + '\n')
    fptr.close()









