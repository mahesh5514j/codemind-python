n =int(input())
l =map(int,input().split())
l1=[]
for i in l:
    if i not in l1 and i%2==0:
        l1.append(i)
print(sum(l1))        
  