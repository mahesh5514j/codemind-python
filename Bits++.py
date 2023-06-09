c=0
for i in range(int(input())):
    a=input()
    if  a[1]=='+' and( a[0]=='+' or a[2]=='+'):
        c=c+1
    elif a[1]=='-' and( a[0]=='-' or a[2]=='-'):
        c=c-1
print(c)
    