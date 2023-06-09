n=input()
x=[]
y=[]
for i in n:
    if i not in x and n.count(i) not in y:
        x.append(i)
        y.append(n.count(i))
if len(y)<2:
    print("-1")
elif len(y)>=2:
    c=[]
    for i in y:
        c.append(i)
    c.sort()
    d=y.index(c[-2])
    print(x[d])
