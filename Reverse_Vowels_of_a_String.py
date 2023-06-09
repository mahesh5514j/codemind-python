z=input()
n=[i for i in z]
x=[]
a='aeiouAEIOU'
for i in range(len(n)):
    if n[i] in a:
        x.append(n[i])
        n[i]=1
x=x[::-1]
k=0
for i in range(len(n)):
    if n[i]==1:
        n[i]=x[k]
        k+=1
print(''.join(n))