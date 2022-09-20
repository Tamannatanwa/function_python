def pos_neg():
    list1=[2,-7,5,-64,-14]
    i=0
    count=0
    num=0
    while i<len(list1):
        if list1[i]>0:
            count+=1
        else:
            num+=1
        i=i+1
    print(count,"positive")
    print(num,"negative")
pos_neg()