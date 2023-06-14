def R(n):
    x=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    y=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    i=12
    while n:
        d= n//x[i]
        n%=x[i]
        while d:
            print(y[i],end="")
            d-=1
        i-=1
n=int(input())
for i in range(n):
    if R(n):
        print(R(n))
        break
    break