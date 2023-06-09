n=input()
x=[]
for i in range(len(n)):
    for j in range(i+1,len(n)+1):
        x.append(n[i:j])
y=[]
for i in x:
    for j in i:
        if i.count(j)==len(i):
            y.append(len(i))
print(max(y))