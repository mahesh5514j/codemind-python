n=input()
a='1234567890'
c=0
for i in n:
    if i in a:
        c+=1
if c!=0:
    print("Contains {} digit".format(c))
else:
    print("Doesn't contain digit")