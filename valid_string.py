n=input()
x=[]
for i in n:
    if i not in x:
        x.append(i)
y=[]
for i in x:
    y.append(n.count(i))
z=[]
for i in y:
    if y.count(i) not in z:
        z.append(y.count(i))
if max(z)==len(y) or max(z)+1==len(y):
    print("Valid String")
else:
    print("Not Valid")