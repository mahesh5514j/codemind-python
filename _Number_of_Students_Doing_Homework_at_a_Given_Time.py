n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
x=int(input())
c=0
for i in range(n):
    if a[i]<=x and b[i]>=x:
        c=c+1
print(c)