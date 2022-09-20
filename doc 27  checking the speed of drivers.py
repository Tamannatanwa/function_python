def fun(speed):
    if speed<=70:
        print("okk")
    elif speed>70:
        a=speed-70
        point=a//5
        print(point)
        if point>=12:
            print("your license suspended")
fun(80)
        