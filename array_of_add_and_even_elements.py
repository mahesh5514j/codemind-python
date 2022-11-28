i=int(input())
a=list(map(int,input().split()))
for j in a:
    if j%2==1:
        print(j,end=" ")
for m in a:
    if m%2==0:
        print(m,end=" ")