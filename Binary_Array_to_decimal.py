n=int(input())
a=list(map(int,input().split()))
c=0
k=0
for i in range(n-1,-1,-1):
    c=c+a[i]*(2**k)
    k=k+1
print(c)
            
        