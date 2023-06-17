n=int(input())
a=list(map(int,input().split()))
m=int(input())
x=[]
y=[]
for i in range(m):
    x.append(a[i])
for j in range(n):
    if j>=m:
        y.append(a[j])
for i in range(len(x)):
    print(x[i],end=' ')
    print(y[i],end=' ')