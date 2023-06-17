n=input().lower()
x=[]
y=[]
m='1234567890'
z='qwertyuioplkjhgfdsazxcvbnm'
c=0
for i in n:
    if i in m:
        if int(i)%2==0:
            x.append(i)
        else:
            y.append(i)
    if i not in m and i not in z:
        c=c+1
if c%2==0:
    for k in range((max(len(x),len(y)))):
        if k<len(x):
            print(x[k],end='')
        if k<len(y):
            print(y[k],end='')
else:
    for k in range((max(len(x),len(y)))):
        if k<len(y):
            print(y[k],end='')
        if k<len(x):
            print(x[k],end='')