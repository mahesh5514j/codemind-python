n=int(input())
a=int(input())
x=[]
while n:
    c=n%a
    n=n//a
    x.append(c)
z=[]
z.append(-1)
for i in range(len(x)-1):
    for j in range(i+1,len(x)):
        p=x[i:j]
        if len(p)==p.count(0):
            z.append(len(p))
print(max(z))
        