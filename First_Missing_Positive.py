n=int(input())
a=list(map(int,input().split()))
a.sort()
x=[]
for i in range(1,n+1):
    x.append(i)
for i in x:
    if i not in a and i!=0:
        print(i)
        break
else:
    print(1)
        