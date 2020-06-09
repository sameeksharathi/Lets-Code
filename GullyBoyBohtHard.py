'''
Gully Boy for his new rap, creating a list of characters, so that list can be arranged in different manners, as per the mood of crowd.
They seek help from GLA students because they feel this is "Boht Hard" to create. Your task is to keep a linked list of characters for
creating rap, but do not keep "white space" character in linked list

-Whenever anyone from the crowd gave gully boy a position of node they have to sing all the linked character N times to create a rap.

for example charsequence is "hello world", int position is 6, N is 1.
we have to store each character in node except white-space, so node position 6 will have 'w' stored in it. And we have to print all characters once so the output will be:
w o r l d h e l l o

Input Format:
first line contains an sequence of characters to be stored as linked list of characters
Second line contains an int node position
Third line contains an integer N denoting how many times you have to sing all characters from given node.

Output Format:
print space seprated characters from given position, print them N times
'''



s = input()
l = list(s)
p = int(input())
n = int(input())
e=[]
for m in range(0,len(l)):
    if l[m]!=' ':
        e.append(l[m])
for k in range(0,n):
    for i in range(p-1,len(e)):
        print(e[i],end=" ")
    for j in range(0,p-1):
        print(e[j],end=" ")
