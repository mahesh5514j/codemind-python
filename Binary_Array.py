n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if i%1==0:
        m=i
        if m==0 or m==1:
            c=c+1
if c==n:
    print("True")
else:
    print("False")