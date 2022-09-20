def update():
    i=1
    while i<=10:
        x=int(input("enter the number"))
        if x%2==0:
            print(x*100)
        else:
            print(x*-1)
        i=i+1
update()