for i in range(int(input())):
    n=input()
    m='1234567890'
    c=0
    for i in n:
        if i in m:
            c=c+1
    if c==0:
        print("No")
    else:
        print('Yes')