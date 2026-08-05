import pandas as pd

student_data = {
    "Name": ["Ram", "Krishna", "Shyam"],
    "Marks": [90, 76, 95],
    "CGPA": [7.19, 8.50, 9.10]
}

df = pd.DataFrame(student_data)

df.to_csv("output.csv", index=False)

print("CSV file created successfully!")