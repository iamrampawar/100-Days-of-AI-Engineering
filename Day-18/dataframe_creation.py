import pandas as pd

student_data = {
    "Name": ["Ram", "Krishna", "Shyam"],
    "Branch": ["IT", "AI", "AIML"],
    "Marks": [90, 76, 95],
    "CGPA": [7.19, 8.50, 9.10]
}

df = pd.DataFrame(student_data)

print("Student DataFrame")
print(df)

print("\nNames")
print(df["Name"])

print("\nNames and Marks")
print(df[["Name", "Marks"]])