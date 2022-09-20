def consecutive(n):
    return sorted(n)==list(range(min(n),max(n)+1))
lst=[2,3,1,4,5]
print(consecutive(lst))




# def con(n):
#     b=sorted(n)
#     c=list(range(min(n)))
#     d=list(range(max(n)))
#     if b==c==d:
#         return True
#     else:
#         return False 
# lst=[2,3,1,4,5,6]
# print(con(lst))
    