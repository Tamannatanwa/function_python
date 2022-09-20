def fizz_buzz():
    user=int(input("enter the number"))
    if user%3==0 and user%5==0:
        print("fizzbuzz")
    elif user%3==0:
        print("fizz")
    elif user%5==0 :
        print("buzz")
    else:
        print(user)
fizz_buzz()
        