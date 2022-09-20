def calculator(num1,opration,num2):
    n=[]
    if opration=="+":
        for i in range (len(num1)):
            mul=num1[i]+num2[i]
            n.append(mul)
        print(n)
    elif opration=="-":
        for i in range (len(num1)):
            mul=num1[i]-num2[i]
            n.append(mul)
        print(n)
    elif opration=="/":
        for i in range (len(num1)):
            mul=num1[i]/num2[i]
            n.append(mul)
        print(n)
    elif opration=="%":
        for i in range (len(num1)):
            mul=num1[i]%num2[i]
            n.append(mul)
        print(n)
    elif opration=="//":
        for i in range (len(num1)):
            mul=num1[i]//num2[i]
            n.append(mul)
        print(n)
    elif opration=="*":
        for i in range (len(num1)):
            mul=num1[i]*num2[i]
            n.append(mul)
        print(n)
    else:
        print("invelid request")
list1=[10,20,30,40]
list2=[50,60,70,80]
calculator(list1,"*",list2)
    
    
        