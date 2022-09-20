# def add(y):
#     x=10
#     c=x+y
#     print(c)
# add(50)





a=int(input("enter the number"))
while a<=200:
    sum=0
    n=a
    v=len(str(a))
    while a>0:
        c=a%10
        b=c**v
        sum+=b
        a=a//10
    if sum==n:
        print(sum,"its armstrong number")
    else:
        print(sum,"its not armstrong number")
    a=a+1
    
    
    
