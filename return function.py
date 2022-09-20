from tkinter import Y


def add(y):
    x=10
    c=x+y
    return c
sum=add(20)
print(sum)




def add_sub(y):
    x=10
    c=x+y
    d=y-x
    return c,d
sum,sub=add_sub(20)
print(sum)
print(sub)