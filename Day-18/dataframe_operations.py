import pandas as pd

student_data = {
    "Name": ["Ram", "Krishna", "Shyam", "Rahul", "Priya"],
    "Branch": ["IT", "AI", "AIML", "CS", "IT"],
    "Marks": [90, 76, 95, 88, 82],
    "CGPA": [7.19, 8.50, 9.10, 8.20, 8.75]
}

df = pd.DataFrame(student_data)

print("Complete DataFrame")
print(df)

print("\nFirst 3 Rows")
print(df.head(3))

print("\nLast 2 Rows")
print(df.tail(2))

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nInfo")
df.info()

print("\nStatistics")
print(df.describe())