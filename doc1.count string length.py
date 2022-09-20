def count():
    list=['abc','xyz','aba','1221']
    i=0
    while i<len(list):
        j=0
        count=0
        while j<len(list[i]):
            if list[i][j]==list[i][-j]:
                count+=1
            j=j+1
        i=i+1
    print(count)
count()
            
        
    