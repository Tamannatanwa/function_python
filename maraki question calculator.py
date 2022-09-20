def calculator():
    num1=int(input("enter the  first number.."))
    num2=int(input("enter the  second number.."))
    opration=input("enter the oprator")
    if opration=="+":
        print(num1+num2)
    elif opration=="-":
        print(num1-num2)
    elif opration=="*":
        print(num1*num2)
    elif opration=="/":
        print(num1/num2)
    elif opration=="%":
        print(num1%num2)
    elif opration=="//":
        print(num1//num2)
    else:
        print("invelid request")
calculator()
    
    
        