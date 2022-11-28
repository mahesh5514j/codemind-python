i=int(input())
l=list(map(int,input().split()))
for j in range(i-1,-1,-1):
    if l[j]%2==0:
        print(j)
        break