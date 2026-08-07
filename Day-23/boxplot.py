import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student.csv")

# Create box plot
sns.boxplot(x=df["Marks"])

# Title
plt.title("Box Plot of Student Marks")

# Show graph
plt.show()