def menu(day):
    if day=="monday":
        food ="butter chicken"
    elif day=="tuesday":
        food="mutton chaap"
    elif day=="wednesday":
        food="kadi rice"
    elif day=="thursday":
        food="khichadi"
    elif day=="friday":
        food="tomato shup"
    elif day=="sturday":
        food="gulab jamun"
    elif day=="sunday":
        food="sabji puri"
    else:
        print("enter valid day")
    return food
print(menu("tuesday"))
    