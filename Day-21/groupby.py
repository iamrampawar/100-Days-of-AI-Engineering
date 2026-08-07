import pandas as pd

# Load dataset
df = pd.read_csv("student.csv")

print("=" * 50)
print("AVERAGE MARKS OF EACH BRANCH")
print("=" * 50)

print(df.groupby("Branch")["Marks"].mean())

print("\n" + "=" * 50)
print("AVERAGE CGPA OF EACH BRANCH")
print("=" * 50)

print(df.groupby("Branch")["CGPA"].mean())

print("\n" + "=" * 50)
print("HIGHEST MARKS OF EACH BRANCH")
print("=" * 50)

print(df.groupby("Branch")["Marks"].max())

print("\n" + "=" * 50)
print("TOTAL STUDENTS IN EACH BRANCH")
print("=" * 50)

print(df.groupby("Branch").size())