n=int(input())
a=input().split('0')
x=[]
for i in a:
    x.append(i.count('1'))
print(max(x))