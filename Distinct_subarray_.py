n=int(input())
m=int(input())
a=[i for i in range(n,m+1)]
x=[]
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        x.append(sum(a[i:j]))
c=0
for i in x:
    if i%2!=0:
        c=c+1
print(c)