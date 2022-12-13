n=int(input())
a=0
print(a,end=' ')
b=1
print(b,end=' ')
for i in range(0,n-2):
        c=a+b
        if c>0:
            a=b
            b=c
            print(c,end=' ')