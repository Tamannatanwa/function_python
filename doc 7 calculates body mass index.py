def bmi(user,b):
    bmi=user/b
    if bmi<=18.5:
        return "underweight"
    elif bmi<=25.0:
        return "normal"
    elif bmi<=30.0:
        return "overweight"
    elif bmi>30:
        return "obese"
# sum=cal()
print(bmi(1.6616,57))






