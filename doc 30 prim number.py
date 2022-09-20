def function(limit):
    n=0
    while n<=limit:
        count=0
        i=1
        while i<=n:
            if n%i==0:
                count+=1
            i=i+1
        if count==2:
            print(n,"primt number")
        else:
            print(n,"not prim number")
        n+=1
function(100)
            
    