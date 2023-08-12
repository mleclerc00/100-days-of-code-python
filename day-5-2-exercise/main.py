# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

current_max = 0
for score in student_scores:
  if current_max < score:
    current_max = score

print(f"The highest score in the class is: {current_max}")
