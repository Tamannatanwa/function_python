# def num():
#     i=1
#     b=[]
#     while i<=5:
#         if i**2>=1 and i**2<=30:
#             b.append(i**2)
#         i=i+1
#     print(b)
# num()



def num():
    n=list()
    for i in range(1,31):
        n.append(i**2)
    v=n[0:5],n[-5:-1]
    print(tuple(v))
num()