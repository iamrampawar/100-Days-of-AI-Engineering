import pandas as pd

df = pd.read_csv("dierty_student.csv")

print("Original Data:\n")
print(df)

print("\nMissing Values in Each Column:\n")
print(df.isnull().sum())

print("\nRows Containing Missing Values:\n")
print(df[df.isnull().any(axis=1)])