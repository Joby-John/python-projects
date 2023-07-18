
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


sum = 0
count = 0
for x in (student_heights):
    sum += student_heights[count]
    count += 1

avg = round(sum/(count))
print(avg)