def unique():
    list=[1,2,3,3,3,3,4,5]
    i=0
    b=[]
    while i<len(list):
        if list[i] not in b:
            b.append(list[i])
        i=i+1
    print(b)
unique()