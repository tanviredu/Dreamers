# A year is a leap year if it is divisible by 4.
# However, if the year is divisible by 100, it is not a leap year, unless...
# the year is also divisible by 400. In that case, it is a leap year.

def is_leap_year(year):
    if year % 400 == 0:
        return True 
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False 

print("Give a year")
year = int(input("=>"))
if is_leap_year(year):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap year")