import pandas as pd
import matplotlib.pyplot as plt
import os

# Load CSV
current_dir = os.path.dirname(__file__)
csv_path = os.path.join(current_dir, "student.csv")

df = pd.read_csv(csv_path)

# -----------------------------
# 1. Average Marks by Branch
# -----------------------------
avg_marks = df.groupby("Branch")["Marks"].mean()

plt.figure(figsize=(8,5))
plt.bar(avg_marks.index, avg_marks.values)

plt.title("Average Marks by Branch")
plt.xlabel("Branch")
plt.ylabel("Average Marks")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()


# -----------------------------
# 2. Distribution of Marks
# -----------------------------
plt.figure(figsize=(8,5))
plt.hist(df["Marks"], bins=5, edgecolor="black")

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()


# -----------------------------
# 3. Branch-wise Student Count
# -----------------------------
branch_count = df["Branch"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(branch_count,
        labels=branch_count.index,
        autopct="%1.1f%%",
        startangle=90)

plt.title("Students by Branch")

plt.show()