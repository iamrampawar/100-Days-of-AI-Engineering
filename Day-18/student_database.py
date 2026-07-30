import pandas as pd

# Student Database
student_data = {
    "Name": ["Ram", "Krishna", "Shyam", "Rahul", "Priya"],
    "Branch": ["IT", "AI", "AIML", "CS", "IT"],
    "Marks": [90, 76, 95, 88, 82],
    "CGPA": [7.19, 8.50, 9.10, 8.20, 8.75]
}

# Create DataFrame
df = pd.DataFrame(student_data)

print("=" * 50)
print("STUDENT DATABASE")
print("=" * 50)

print("\nComplete Database")
print(df)

print("\nFirst 3 Students")
print(df.head(3))

print("\nLast 2 Students")
print(df.tail(2))

print("\nDatabase Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nDatabase Information")
df.info()

print("\nStatistics")
print(df.describe())

print("\nHighest Marks")
print(df["Marks"].max())

print("\nLowest Marks")
print(df["Marks"].min())

print("\nAverage Marks")
print(df["Marks"].mean())

print("\nTop Scorer")
print(df[df["Marks"] == df["Marks"].max()])

print("\nStudents with Marks Above 85")
print(df[df["Marks"] > 85])