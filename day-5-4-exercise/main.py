for number in range (1,101):
    fizz = ""
    buzz = ""
    if number % 3 == 0:
        fizz = "fizz"
    if number % 5 == 0:
        buzz = "buzz"
    if fizz == "" and buzz == "":
        print(number)
    else:
        print(f"{fizz}{buzz}")


for number in range (1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
