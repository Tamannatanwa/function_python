def cal(user,b):
    bmi=user/b
    if bmi>30:
        return "obese"
    if bmi<=18.5:
        return "underweight"
    if bmi<=25.0:
        return "normal"
    if bmi<=30.0:
        return "overweight"
sum=cal()
print(sum)
    