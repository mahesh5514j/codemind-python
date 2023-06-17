n=int(input())
a=list(map(int,input().split()))
a.sort()
x=[]
x.append(a[-2])
x.append(a[-1])
for i in range(n-3,-1,-2):
    if i not in x :
        if a[i-1] not in x:
            x.append(a[i-1])
        if a[i] not in x:
            x.append(a[i])
print(*x)