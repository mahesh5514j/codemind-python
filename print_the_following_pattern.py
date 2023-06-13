n=int(input())
a=65
for i in range(n):
    for j in range(n):
        print(chr(a+i),end=' ')
    print()