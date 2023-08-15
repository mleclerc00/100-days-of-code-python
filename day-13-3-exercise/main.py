for number in range(1, 101):
    # use and instead of or since it needs to be evenly divisible by 3 and 5
    # also fix logic to use elif statements instead of printing the number
    # as a else to the first if
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
