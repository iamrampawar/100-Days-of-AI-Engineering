import pandas as pd

df = pd.read_csv("student.csv")

print("=" * 50)
print("STUDENT CSV ANALYSIS")
print("=" * 50)

print("\nComplete Dataset")
print(df)

print("\nTotal Students:")
print(len(df))

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nLowest Marks:")
print(df["Marks"].min())

print("\nAverage CGPA:")
print(df["CGPA"].mean())

print("\nTop Scorer")
print(df[df["Marks"] == df["Marks"].max()])

print("\nStudents Above 85 Marks")
print(df[df["Marks"] > 85])

print("\nIT Students")
print(df[df["Branch"] == "IT"])