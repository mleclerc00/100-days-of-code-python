# num_char = len(input("What is your name?"))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")
# print(type(num_char))

a = float(123)
print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))

# Mathematical Operations
print(3 + 5)
print(7 - 4)
print(3 * 2)
print(6 / 3)
print(2 ** 3)

# PEMDAS (left to right)
# ()
# **
# * /
# + -
print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)

print(round(8 / 3, 2))
print(8 // 3)

result = 4 / 2
result /= 2
print(result)

# f-strings
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
