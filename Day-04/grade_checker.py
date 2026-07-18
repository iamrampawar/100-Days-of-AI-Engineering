# Day 4 Mini Project - Grade Checker

marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")

elif marks >= 90:
    print("Grade: A+")

elif marks >= 75:
    print("Grade: A")

elif marks >= 60:
    print("Grade: B")

elif marks >= 35:
    print("Grade: C")

else:
    print("Result: Fail")