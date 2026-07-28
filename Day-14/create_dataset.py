import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit"],
    "Age": [20,19,21],
    "Gender": ["Male","Female","Male"],
    "Math": [85,92,70],
    "Science": [90,88,75],
    "English": [78,95,68],
    "Attendance": [92,96,80]
}

df = pd.DataFrame(data)

df.to_csv("students.csv", index=False)

print("CSV file created successfully!")