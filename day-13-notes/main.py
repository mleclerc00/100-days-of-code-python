# ############DEBUGGING#####################


# # Describe Problem
# # 20 isn't included in range(1,20)
# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")


# my_function()


# # Reproduce the Bug
# # list index starts at 0, therefore if int is 6 results in out of range
# # 0 would also never get chosen with randint(1,6)
# from random import randint

# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# # Debug
# # dice_num = 6
# print(dice_imgs[dice_num])


# # Play Computer
# # value 1994 will not print anything with the given conditionals
# year = int(input("What's your year of birth?"))
# # if year > 1980 and year < 1994:
# if year > 1980:
#     print("You are a millennial.")
# elif year >= 1994:
#     print("You are a Gen Z.")


# # Fix the Errors
# # use f-string, indent the print statement, convert input to int
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")


# # Print is Your Friend
# # set value with = instead of comparison operator ==
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)


# Use a Debugger
# Indent append in order to add each item to the list
# instead of just the last item
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
