n=int(input())
a=list(map(int,input().split()))
x=[]
for i in range(0,n,2):
    for j in range(a[i]):
        x.append(a[i+1])
for i in x:
    print(i,end=' ')