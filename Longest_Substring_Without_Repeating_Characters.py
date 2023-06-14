def c(n):
    x=[]
    n=n.lower()
    for i in n:
        if i not in x:
            x.append(i)
    if len(x)==len(n):
        return True
    else:
        return False
n=input()
x=[]
y=[]
for i  in range(len(n)):
    for j in range(i+1,len(n)+1):
        if c(n[i:j]):
            y.append(len(n[i:j]))
            x.append(n[i:j])
k=y.index(max(y))
if len(x[k])>=3:
    print(x[k])
else:
    print("-1")