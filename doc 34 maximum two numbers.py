def max_two():
    a=[10,14,2,23,19]
    i=0
    max=0
    secondmax=0
    while i<len(a):
        num=a[i]
        if num>max:
            max=num
        elif num>secondmax:
            secondmax=num
        i=i+1
    sum=max+secondmax
    print(sum)
max_two()




        
