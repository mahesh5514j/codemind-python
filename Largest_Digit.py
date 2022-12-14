n=int(input())
b=[]
r=0
while n:
        d=n%10
        n=n//10
        b.append(d)
print(max(b))