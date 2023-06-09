for i in range(int(input())):
    a=input()
    x=[]
    y=[]
    c=0
    for i in a:
        if i!='':
            x.append(i)
    for i in range(len(a)-1,-1,-1):
        if a[i]!='':
            y.append(a[i])
    for i in range(len(x)):
        if x[i]==y[i]:
            c=c+1
    if c!=len(x):
        print("NO")
    elif c==len(x) and len(x)%2==0:
        print("YES EVEN")
    else:
        print("YES ODD")