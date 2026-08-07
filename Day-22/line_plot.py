import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student.csv")

# Create line plot
plt.figure(figsize=(8,5))

plt.plot(
    df["Name"],
    df["Marks"],
    marker="o",
    linewidth=2
)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)

plt.show()