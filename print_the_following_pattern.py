n=int(input())
a=65
for i in range(n):
    for j in range(n-i):
        print(chr(a+n-i-1),end=' ')
    print()