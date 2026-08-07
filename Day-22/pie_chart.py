import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student.csv")

# Count students in each branch
branch_count = df["Branch"].value_counts()

# Create Pie Chart
plt.figure(figsize=(7,7))

plt.pie(
    branch_count,
    labels=branch_count.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Student Branch Distribution")

plt.show()