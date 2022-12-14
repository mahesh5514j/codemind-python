n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
d=0
e=[]
for i in a:
    if i%1==0:
        m=i
        if m>c or m<b:
            x=m
            d=d+1
            e.append(x)
if d!=0:
    print(max(e))
else:
    print("-1")