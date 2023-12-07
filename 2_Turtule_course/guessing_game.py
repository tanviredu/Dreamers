import random

secret_number = random.randint(1,10)
attempts = 0
max_attempts = 5
print("Welcome To the Game!!!")
print("I Have secleted a number between 1 and 10 guess it")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("you guessed the right number")
        break
    elif guess < secret_number:
        print("Too low, try again with a bigger number")
    else:
        print("Too high, Try again with a lower number")
    
    attempts +=1

