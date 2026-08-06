import pandas as pd

# Read CSV
df = pd.read_csv("dierty_student.csv")

print("=" * 50)
print("ORIGINAL DATA")
print("=" * 50)
print(df)

# -----------------------------
# Missing Values
# -----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# Fill Missing Values
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["CGPA"] = df["CGPA"].fillna(df["CGPA"].mean())

# -----------------------------
# Remove Duplicates
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Student Performance
# -----------------------------
df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

# -----------------------------
# Statistics
# -----------------------------
print("\nAverage Marks:", round(df["Marks"].mean(), 2))
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

print("\nAverage CGPA:", round(df["CGPA"].mean(), 2))
print("Highest CGPA:", df["CGPA"].max())

# -----------------------------
# Final Clean Data
# -----------------------------
print("\n" + "=" * 50)
print("CLEANED DATA")
print("=" * 50)
print(df)

# -----------------------------
# Save Clean Dataset
# -----------------------------
df.to_csv("clean_student.csv", index=False)

print("\n✅ Clean dataset saved as clean_student.csv")