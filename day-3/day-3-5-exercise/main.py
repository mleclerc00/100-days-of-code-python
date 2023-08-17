# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

true_score = 0
love_score = 0
combined_names = (name1 + name2).lower()

for char in "true":
    true_score += combined_names.count(char)

for char in "love":
    love_score += combined_names.count(char)

total_score = int(str(true_score) + str(love_score))

if (total_score < 10) or (total_score > 90):
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif (total_score > 40) and (total_score < 50):
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")
