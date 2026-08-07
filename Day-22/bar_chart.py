import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student.csv")

# Create figure
plt.figure(figsize=(8,5))

# Bar Chart
plt.bar(df["Name"], df["Marks"])

# Title
plt.title("Student Marks")

# Axis Labels
plt.xlabel("Students")
plt.ylabel("Marks")

# Show graph
plt.show()