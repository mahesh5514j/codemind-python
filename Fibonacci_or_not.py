n=int(input())
m=[]
a=0
b=1
x=0
m.append(a)
m.append(b)
for i in range(1,n-1):
    if i%1==0:
        c=a+b
        a=b
        b=c
        m.append(c)
for j in m:
    if j/n==1:
        x=x+1
if x==1:
    print("True")
else:
    print("False")