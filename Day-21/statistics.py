import pandas as pd

# Load dataset
df = pd.read_csv("student.csv")

print("=" * 50)
print("STATISTICS")
print("=" * 50)

# Mean
print("\nAverage Marks:")
print(df["Marks"].mean())

# Median
print("\nMedian Marks:")
print(df["Marks"].median())

# Mode
print("\nMode Marks:")
print(df["Marks"].mode())

# Maximum
print("\nHighest Marks:")
print(df["Marks"].max())

# Minimum
print("\nLowest Marks:")
print(df["Marks"].min())

# Standard Deviation
print("\nStandard Deviation:")
print(df["Marks"].std())

# Average CGPA
print("\nAverage CGPA:")
print(df["CGPA"].mean())