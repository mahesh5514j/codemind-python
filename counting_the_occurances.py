n=input().lower()
a=input().lower()
c=0
for i in n:
    if i==a:
        c=c+1
if c==0:
    print("-1")
else:
    print(c)