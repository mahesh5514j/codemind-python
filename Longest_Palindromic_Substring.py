def r(n):
    m=n[::-1]
    if m==n:
        return True
    else:
        return False
n=input()
x=[]
y=[]
for i  in range(len(n)):
    for j in range(i+1,len(n)+1):
        if r(n[i:j]):
            x.append(n[i:j])
            y.append(len(n[i:j]))
k=y.index(max(y))
print(x[k])