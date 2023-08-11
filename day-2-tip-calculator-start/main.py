#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

welcome_message = "Welcome to the tip calculator!"
print(welcome_message)

# Total bill
bill_prompt = "What was the total bill? $"
bill = float(input(bill_prompt))

# Percent tip
tip_prompt = "How much tip would you like to give? e.g. 10, 12, or 15? "
percent_tip = float(input(tip_prompt)) / 100

# Number of people
person_count_prompt = "How many people to split the bill? "
num_people = int(input(person_count_prompt))

# Calulate tip and add to total
total_tip = bill * percent_tip
total_bill = total_tip + bill

# Split between number of people
bill_per_person = "{:.2f}".format((total_bill / num_people))

print(f"Each person should pay: ${bill_per_person}")