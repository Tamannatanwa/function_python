def generate_range(min,max,step):
    b=[]
    while min<=max:
        b.append(min)
        min+=step
    print(b)
generate_range(1,10,3)
    