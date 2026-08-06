import pandas as pd

# Load CSV file
df = pd.read_csv("dierty_student.csv")

print("Original Data:\n")
print(df)

print("\nNumber of Rows Before Removing Duplicates:")
print(len(df))

# Remove duplicate rows
df = df.drop_duplicates()

print("\nData After Removing Duplicates:\n")
print(df)

print("\nNumber of Rows After Removing Duplicates:")
print(len(df))