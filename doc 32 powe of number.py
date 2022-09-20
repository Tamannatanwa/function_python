def num(inclusive):
    i=0
    c=[]
    while i<=inclusive:
        n=2**i
        c.append(n)
        i=i+1
    print(c)
num(2)