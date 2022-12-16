n=int(input())
a=list(map(int,input().split()))
c=0
l=[]
l.append(a[-1])
for i in a:
    l.append(i)
l.append(a[0])
for i in range(1,n+1):
    if (l[i-1]%2==0 and l[i+1]%2!=0) or (l[i-1]%2!=0 and l[i+1]%2==0):
        c=c+1
print(c)