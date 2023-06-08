n=input()
m=input()
c=n+m
x=[]
for i in c:
    if i!='':
        x.append(i)
x.sort()
for i in x:
    print(i,end='')