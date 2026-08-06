import pandas as pd

# Read CSV file
df = pd.read_csv("dierty_student.csv")

print("Original Data:\n")
print(df)

# Fill missing Marks with the average
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Fill missing CGPA with the average
df["CGPA"] = df["CGPA"].fillna(df["CGPA"].mean())

print("\nData After Filling Missing Values:\n")
print(df)