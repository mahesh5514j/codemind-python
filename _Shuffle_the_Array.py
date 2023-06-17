n=int(input())
a=list(map(int,input().split()))
m=int(input())
x=[]
y=[]
for j in range(n):
    if j>=m:
        y.append(a[j])
    else:
        x.append(a[j])
for i in range(len(x)):
    print(x[i],end=' ')
    print(y[i],end=' ')