'''
John Watson knows of an operation called a right circular rotation on an array of integers. One rotation operation moves the last array element to the first position 
and shifts all remaining elements right one. To test Sherlock's abilities, Watson provides Sherlock with an array of integers. Sherlock is to perform the rotation operation 
a number of times then determine the value of the element at a given position.

For each array, perform a number of right circular rotations and return the value of the element at a given index.

For example, array a = [3,4,5], number of rotations, k=2 and indices to check, m=[1,2].
First we perform the two rotations:
[3,4,5] -> [5,3,4] -> [4,5,3]
Now return the values from the zero-based indices 1 and 2 as indicated in the m array.
a[1] = 5
a[2] = 3

Input Format:
The first line contains 3 space-separated integers, n, ,k and q, the number of elements in the integer array, the rotation count and the number of queries.
The second line contains n space-separated integers, where each integer i describes array element a[i] (where 0 <= i < n).
Each of the q subsequent lines contains a single integer denoting m, the index of the element to return from a.

Output Format:
For each query, print the value of the element at index m of the rotated array on a new line.

Sample Input:
3 2 3
1 2 3
0
1
2

Sample Output:
2
3
1
'''


import math
import os
import random
import re
import sys

def circularArrayRotation(a, k, queries):
    a = a[n-(k%n):]+a[0:n-(k%n)]
    l = [a[x] for x in queries]
    return l
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nkq = input().split()
    n = int(nkq[0])
    k = int(nkq[1])
    q = int(nkq[2])
    a = list(map(int, input().rstrip().split()))
    queries = []
    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)
    result = circularArrayRotation(a, k, queries)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
