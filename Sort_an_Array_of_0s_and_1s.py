n=int(input())
l=list(map(int,input().split()))
for i in l:
    if i==0:
        print("0",end=" ")
for j in l:
    if j==1:
        print("1",end=" ")