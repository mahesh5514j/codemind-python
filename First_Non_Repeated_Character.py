for i in range(int(input())):
    n=int(input())
    a=input()
    for i in a:
        if a.count(i)==1 and i!='':
            print(i)
            break
    else:
        print("-1")