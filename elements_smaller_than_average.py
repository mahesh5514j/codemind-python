n=int(input())
a=list(map(int,input().split()))
c=0
m=0
for i in a:
    if i%1==0:
        c=c+i
b=c//n
for j in a:
    if j%1==0:
        x=j
        if x<=b:
            m=m+1
print(m)