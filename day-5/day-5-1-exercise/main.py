
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

student_heights_sum = 0
count = 0
for height in student_heights:
  student_heights_sum += height
  count += 1

print(round(student_heights_sum / count))
