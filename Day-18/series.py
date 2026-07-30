import pandas as pd

marks = pd.Series(
    [85, 90, 76],
    index=["Ram", "Krishna", "Shyam"]
)

print("Student Marks")
print(marks)

print("\nRam's Marks:")
print(marks["Ram"])

print("\nKrishna's Marks:")
print(marks["Krishna"])

print("\nShyam's Marks:")
print(marks["Shyam"])