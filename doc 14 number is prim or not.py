def prim():
    user=int(input("enter the number"))
    fac=0
    i=1
    while i<=user:
        if user%i==0:
            fac+=1
        i=i+1
    if fac==2:
        print(user,"it is prim number")
    else:
        print(user,"it is not prim number")
prim()
        