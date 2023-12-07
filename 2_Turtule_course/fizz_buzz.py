def fizzbuzz(n):
    for item in range(1,n+1):
        if item % 3 == 0 and item % 5 == 0:
            print("Fizz Buzz")
        elif item % 3 == 0:
            print("Fizz")
        elif item % 5 == 0:
            print("Buzz")
        else:
            print(item)

fizzbuzz(20)