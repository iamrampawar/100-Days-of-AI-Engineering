import pandas as pd

# Load dataset
df = pd.read_csv("student.csv")

print("=" * 50)
print("STUDENT BRANCH COUNT")
print("=" * 50)

print(df["Branch"].value_counts())

print("\n" + "=" * 50)
print("ATTENDANCE COUNT")
print("=" * 50)

print(df["Attendance"].value_counts())

print("\n" + "=" * 50)
print("BRANCH PERCENTAGE")
print("=" * 50)

print(df["Branch"].value_counts(normalize=True) * 100)