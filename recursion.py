# def myfun():
#     print("geekyshows")
#     myfun()
# myfun()




i=0
def myfun():
    global i
    i=i+1
    print("my function",i)
    myfun()
myfun()