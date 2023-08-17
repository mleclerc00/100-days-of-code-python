# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / height ** 2)
message = f"Your BMI is {bmi}, you "

if bmi < 18.5:
    condition = "are underweight."
    print(message + condition)
elif bmi < 25:
    condition = "have a normal weight."
    print(message + condition)
elif bmi < 30:
    condition = "are slightly overweight."
    print(message + condition)
elif bmi < 35:
    condition = "are obese."
    print(message + condition)
else:
    condition = "are clinically obese."
    print(message + condition)
