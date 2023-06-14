n=int(input())
a=list(map(int,input().split()))
x=[]
y=[]
for i in range(n):
    for j in range(i+1,n+1):
        x.append(sum(a[i:j]))
print(max(x))