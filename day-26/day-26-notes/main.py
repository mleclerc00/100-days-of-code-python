import pandas
from random import randint


numbers = [1, 2, 3]
new_list = []
for number in numbers:
    add_1 = number + 1
    new_list.append(add_1)
print(new_list)

new_list_comprehension = [number + 1 for number in numbers]
print(new_list_comprehension)

name = "Eleanor"
name_list = [letter for letter in name]
print(name_list)

range_list = [number * 2 for number in range(1, 5)]
print(range_list)

names = ["Ian", "Connor", "Alexander", "Mollie", "Beth", "Nelle"]
conditional_list = [name.upper() for name in names if len(name) > 4]
print(conditional_list)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
numbers_squared = [number**2 for number in numbers]
print(numbers_squared)


even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)


def file_to_list(file):
    with open(file, mode='r') as file:
        return file.readlines()


list1 = file_to_list("./file1.txt")
list2 = file_to_list("./file2.txt")
result = [int(number) for number in list1 if number in list2]
print(result)

student_scores = {}
names = ["Ian", "Connor", "Alexander", "Mollie", "Beth", "Nelle"]
student_scores = {student: randint(0, 100) for student in names}
print(student_scores)

passed_scores = {student: score for (student, score) in student_scores.items() if score > 60}
print(passed_scores)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
results = {word: len(word) for word in sentence.split()}
print(results)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)


student_dict = {
    "student": ["Erik", "Victoria", "Jackson"],
    "score": [94, 8, 97]
}
student_df = pandas.DataFrame(student_dict)
for (index, row) in student_df.iterrows():
    print(row.student)
    print(row.score)
