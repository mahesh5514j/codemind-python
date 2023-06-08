n=input()
a='123456789'
c=0
for i in n:
    if i in a:
        c=c+int(i)
print(c)