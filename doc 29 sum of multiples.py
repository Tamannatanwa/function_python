def func(limit):
    i=1
    sum=0
    while i<=limit:
        if i%3==0 or i%5==0:
            sum+=i
            print(i,",",end="")
        i=i+1
    print(sum)
func(20)