n,m=map(int,input().split())
a=list(map(int,input().split()))
x=[]
for i in range(n):
    for j in range(i+1,n+1):
        x.append(sum(a[i:j]))
c=0
for i in x:
    if i==m:
        c=c+1
print(c)