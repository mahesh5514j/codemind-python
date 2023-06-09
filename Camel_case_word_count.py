def c(n):
    c=1
    for i in range(1,len(n)-1):
        if n[i].isupper():
            c=c+1
    return(c)
n=input()
print(c(n))