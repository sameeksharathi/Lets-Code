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
