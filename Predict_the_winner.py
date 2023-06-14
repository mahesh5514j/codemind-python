n=int(input())
a=list(map(int,input().split()))
x=0
y=0
for i in range(n):
    if i%2==0:
        x=x+a[i]
    else:
        y=y+a[i]
if abs(x-y)%4==0:
    print("X")
else:
    print("Y")