for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    x=[]
    for i in a:
        if i not in x:
            x.append(i)
    for i in b:
        if i not in x:
            x.append(i)
    if len(x)==n:
        print("YES")
    else:
        print("NO")