import pandas as pd

# Load dataset
df = pd.read_csv("student.csv")

print("Original Dataset:")
print(df)

# First 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Dataset shape
print("\nDataset Shape:")
print(df.shape)

# Create target variable
df["Passed"] = (df["Marks"] >= 40).astype(int)

print("\nTarget Variable:")
print(df[["Name", "Marks", "Passed"]])

# Feature Engineering
df["StudyEfficiency"] = df["Marks"] / df["StudyHours"]

print("\nAfter Feature Engineering:")
print(df)

# Separate features and target
X = df.drop(columns=["Name", "Passed"])
y = df["Passed"]

print("\nFeatures (X):")
print(X)

print("\nTarget (y):")
print(y)

# Display shapes
print("\nX Shape:", X.shape)
print("y Shape:", y.shape)