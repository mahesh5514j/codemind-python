n=int(input())
if n>=3:
    for i in range(n):
        for j in range(0,i+1):
            print("*",end='')
        print()
    for i in range(1,n):
        for j in range(i+1,n+1):
            if i<j:
                print("*",end='')
        print()
else:
    print("The pattern is not possible")