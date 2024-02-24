from datetime import datetime,date,time,timedelta

current_datetime = datetime.now()
print(current_datetime)
print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)

x = datetime.today()
#print(x)

formatted_datetime = current_datetime.strftime("%d-%m-%Y %I:%M:%S")
print(formatted_datetime)

my_date = date(2024,3,1)
#print(my_date)

my_time = time(23,11,20)
#print(my_time)

date1 = datetime(2023,1,1)
#print(date1)
date2 = datetime(1993,1,1)
#print(date2)

today = datetime.today()
#print(today)
tendays = timedelta(days=10)
future_time = today+tendays
#print(future_time)

# jan 15 2012
# dec 23 1994


#if date1 < date2:
#  print("date 1 is earlier")
#else:
#  print("date 2 is earlier")


def calculate_birthday(birthday):
  today = datetime.today()
  age = today.year - birthday.year
  
  if today.month < birthday.month:
    age = age-1
  elif today.month == birthday.month and today.day < birthday.day:
    age = age -1
    
  return age
  

print("Enter year")
year = int(input())
print("Enter month")
month = int(input())
print("Enter day")
day = int(input())

birthday = datetime(year,month,day)

x = calculate_birthday(birthday)
print(x)
  