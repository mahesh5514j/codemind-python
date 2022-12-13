n=int(input())
m=n//2
c=0
for i in range(1,m+1):
    if n%i==0:
       c=c+i
if c>n:
    print("True")
else:
    print("False")