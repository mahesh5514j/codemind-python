n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if i not in a:
        a.append(i)
for j in a:
    if j%1==0:
        print(j,end=' ')