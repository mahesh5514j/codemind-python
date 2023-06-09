n=input()
x=[]
for i in range(len(n)):
    for j in range(i+1,len(n)+1):
        x.append(n[i:j])
y=[]
for i in x:
    z=i.count("a")+i.count("e")+i.count("i")+i.count("o")+i.count('u')
    if z==len(i):
        y.append(z)
print(max(y))