def calculate_result(marks):

    total = sum(marks)

    average = total / len(marks)

    return total, average

print("===== Student Result Analyzer =====")

name = input("Enter Student Name: ")

marks = []

for i in range(1, 6):

    mark = float(input(f"Enter Marks of Subject {i}: "))

    marks.append(mark)

total, average = calculate_result(marks)

print("\n===== RESULT =====")

print("Name :", name)

print("Total :", total)

print("Average :", round(average, 2))

if average >= 90:

    grade = "A+"

elif average >= 80:

    grade = "A"

elif average >= 70:

    grade = "B"

elif average >= 60:

    grade = "C"

else:

    grade = "Fail"

print("Grade :", grade)