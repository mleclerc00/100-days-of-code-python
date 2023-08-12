# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#random_choice = random.randint(0, len(names) - 1)
#print(f"{names[random_choice]} is going to buy the meal today!")

random_choice = random.choice(names)
print(f"{random_choice} is going to buy the meal today!")