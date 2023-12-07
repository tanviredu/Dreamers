def calculate_speed(distance,time):
    speed = distance/time 
    return speed

while True:
    print("Enter the Distance")
    distance = int(input("=>"))
    print("Enter the Time")
    time = int(input("=>"))
    speed = calculate_speed(distance,time)
    print(f"The speed is {speed}")