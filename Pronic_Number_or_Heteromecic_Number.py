def p(n):
    for i in range(1,n):
        if i*(i+1)==n:
            return True
        if i*(i+1)>n:
            return False
n=int(input())
if p(n):
    print("YES")
else:
    print("NO")
