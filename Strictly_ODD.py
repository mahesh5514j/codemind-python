n=int(input())
a=list(map(int,input().split()))
c=0
d=[]
for i in a:
    if i%2!=0:
        m=i
        x=a.index(m)
        d.append(x)
for j in d:
    if j%2!=0:
        c=c+1
if c==len(d):
    print("True")
else:
    print("False")