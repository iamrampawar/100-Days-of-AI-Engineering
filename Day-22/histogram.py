import pandas as pd
import matplotlib.pyplot as plt
import os

# Load CSV file
current_dir = os.path.dirname(__file__)
csv_path = os.path.join(current_dir, "student.csv")

df = pd.read_csv(csv_path)

# Histogram of Marks
plt.figure(figsize=(8, 5))
plt.hist(df["Marks"], bins=5, edgecolor="black")

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()