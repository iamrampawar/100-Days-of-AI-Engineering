# ============================================
# Day 14 - Data Exploration with Pandas
# 100 Days of AI Engineering
# Author: Ram Pawar
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------
# Load the dataset
# --------------------------------------------
df = pd.read_csv("dataset/students.csv")

print("=" * 50)
print("STUDENT DATASET")
print("=" * 50)

# --------------------------------------------
# Display first and last rows
# --------------------------------------------
print("\n1. First 5 Rows")
print(df.head())

print("\n2. Last 5 Rows")
print(df.tail())

# --------------------------------------------
# Dataset information
# --------------------------------------------
print("\n3. Dataset Information")
df.info()

# --------------------------------------------
# Shape of dataset
# --------------------------------------------
print("\n4. Dataset Shape")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

# --------------------------------------------
# Column names
# --------------------------------------------
print("\n5. Column Names")
print(df.columns.tolist())

# --------------------------------------------
# Statistical summary
# --------------------------------------------
print("\n6. Statistical Summary")
print(df.describe())

# --------------------------------------------
# Missing values
# --------------------------------------------
print("\n7. Missing Values")
print(df.isnull().sum())

# --------------------------------------------
# Check duplicate rows
# --------------------------------------------
print("\n8. Duplicate Rows")
print(df.duplicated().sum())

# --------------------------------------------
# Unique values
# --------------------------------------------
print("\n9. Unique Genders")
print(df["Gender"].unique())

# --------------------------------------------
# Value counts
# --------------------------------------------
print("\n10. Gender Count")
print(df["Gender"].value_counts())

# --------------------------------------------
# Create a new column
# --------------------------------------------
df["Average"] = (
    df["Math"] +
    df["Science"] +
    df["English"]
) / 3

print("\n11. Dataset with Average Marks")
print(df)

# --------------------------------------------
# Highest scorer
# --------------------------------------------
print("\n12. Top Performer")

top_student = df.loc[df["Average"].idxmax()]

print(top_student)

# --------------------------------------------
# Lowest scorer
# --------------------------------------------
print("\n13. Lowest Performer")

lowest_student = df.loc[df["Average"].idxmin()]

print(lowest_student)

# --------------------------------------------
# Sort by Average
# --------------------------------------------
print("\n14. Ranking Students")

ranking = df.sort_values(
    by="Average",
    ascending=False
)

print(ranking[["Name", "Average"]])

# --------------------------------------------
# Filter students scoring above 85
# --------------------------------------------
print("\n15. Students with Average > 85")

high_scorers = df[df["Average"] > 85]

print(high_scorers[["Name", "Average"]])

# --------------------------------------------
# Average Attendance
# --------------------------------------------
print("\n16. Average Attendance")

print(df["Attendance"].mean())

# --------------------------------------------
# Correlation
# --------------------------------------------
print("\n17. Correlation Matrix")

print(df.corr(numeric_only=True))

# --------------------------------------------
# Save updated dataset
# --------------------------------------------
df.to_csv(
    "dataset/students_updated.csv",
    index=False
)

print("\nUpdated dataset saved successfully!")

# ============================================
# VISUALIZATION
# ============================================

# Bar Chart

plt.figure(figsize=(8,5))

plt.bar(
    df["Name"],
    df["Average"]
)

plt.title("Average Marks of Students")
plt.xlabel("Students")
plt.ylabel("Average Marks")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

# Scatter Plot

plt.figure(figsize=(8,5))

plt.scatter(
    df["Attendance"],
    df["Average"]
)

plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Average Marks")

plt.tight_layout()

plt.show()

# Histogram

plt.figure(figsize=(8,5))

plt.hist(df["Average"], bins=5)

plt.title("Distribution of Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")

plt.tight_layout()

plt.show()

print("\nProject Completed Successfully!")