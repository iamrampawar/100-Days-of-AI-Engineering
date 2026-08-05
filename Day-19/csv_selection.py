import pandas as pd

df = pd.read_csv("student.csv")

print("Names")
print(df["Name"])

print("\nMarks")
print(df["Marks"])

print("\nName and CGPA")
print(df[["Name", "CGPA"]])