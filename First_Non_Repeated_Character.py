for i in range(int(input())):
    n=int(input())
    a=input()
    x=[]
    for i in a:
        if a.count(i)==1 and i!='':
            x.append(i)
            break
    if len(x)==1:
        print(x[0])
    else:
        print("-1")