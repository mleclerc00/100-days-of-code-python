for number in range(1, 101):
    # use and instead of or since it needs to be evenly divisible by 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        print([number])
