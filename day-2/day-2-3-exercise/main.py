# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

end_age = 90
current_age = int(age)

months_in_year = 12
weeks_in_year = 52
days_in_year = 365

years_remaining  = end_age - current_age

months_remaining = years_remaining * months_in_year
weeks_remaining = years_remaining * weeks_in_year
days_remaining = years_remaining * days_in_year

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left"
print(message)
