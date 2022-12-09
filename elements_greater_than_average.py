n=int(input())
a=list(map(int,input().split()))
b=0
x=0
for i in a:
    if i%1==0:
        d=i
        b=b+d
c=b//n
for j in a:
    if j%1==0:
        z=j
        if z>=c:
            x=x+1
print(x)