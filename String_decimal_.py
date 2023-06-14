for i in range(int(input())):
    n=input()
    c=0
    for i in n:
        if i.isdigit() or i=='':
            c=c+1
    if len(n)==c:
        print("True")
    else:
        print("False")