import pandas as pd

# Load dataset
df = pd.read_csv("student.csv")

print("=" * 50)
print("STUDENTS WITH MARKS GREATER THAN 90")
print("=" * 50)

print(df[df["Marks"] > 90])

print("\n" + "=" * 50)
print("IT STUDENTS")
print("=" * 50)

print(df[df["Branch"] == "IT"])

print("\n" + "=" * 50)
print("CGPA GREATER THAN 8.5")
print("=" * 50)

print(df[df["CGPA"] > 8.5])

print("\n" + "=" * 50)
print("AI STUDENTS WITH MARKS ABOVE 85")
print("=" * 50)

print(df[(df["Branch"] == "AI") & (df["Marks"] > 85)])