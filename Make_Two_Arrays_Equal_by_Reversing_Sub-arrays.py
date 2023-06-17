n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
x=[]
for i in a:
    if i in b:
        x.append(i)
if len(x)==len(b):
    print("True")
else:
    print("False")