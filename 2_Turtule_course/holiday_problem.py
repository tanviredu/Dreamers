def is_holiday(day):
    holiday = ["friday","Friday","Saturday","saturday"]
    if day in holiday:
        print("Yes !!! its holiday")
    else:
        print("No Not Holiday")

while True:
    print("Enter Day")
    day = input("=>")
    is_holiday(day)