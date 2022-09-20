from curses.ascii import islower


def upper_lower():
    a='The quick Brow Fox'
    count=0
    co=0
    for i in a:
        for j in i:
            if j.isupper()==True:
                count+=1
            elif j.islower()==True:
                co+=1
    print(count)
    print(co)
upper_lower()