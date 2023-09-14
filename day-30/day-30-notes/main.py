# file not found error
with open("./data.txt", "r") as file:
    file.read()

# key error
a_dictionary = {"key": "value"}
value = a_dictionary["non_existent_key"]

# index error
fruit_list = ["Apple", "Banana", "Pear"]
fruit = fruit_list[3]

# type error
text = "abc"
print(text + 5)

# attribute error
import random

random_integer = random.randint(1, 10)


# name error
print(non_existent_variable)


# try except
try:
    file = open("./data.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("./data.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
    raise TypeError("This is an error that I made up.")


# raise error
height = float(input("Height: "))
weight = int(input("Weight: "))

bmi = round(weight / height**2)

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")


# IndexError
fruits = ["Apple", "Pear", "Orange"]

# TODO: Catch the exception and make sure the code runs without crashing.


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)


# KeyError
facebook_posts = [
    {"Likes": 21, "Comments": 2},
    {"Likes": 13, "Comments": 2, "Shares": 1},
    {"Likes": 33, "Comments": 8, "Shares": 3},
    {"Comments": 4, "Shares": 2},
    {"Comments": 1, "Shares": 1},
    {"Likes": 19, "Comments": 3},
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post["Likes"]
    except KeyError:
        pass


print(total_likes)
