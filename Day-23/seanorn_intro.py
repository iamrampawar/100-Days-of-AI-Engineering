import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student.csv")

# Display first 5 rows
print(df.head())

# Create a scatter plot
sns.scatterplot(x="Marks", y="CGPA", data=df)

# Title
plt.title("Marks vs CGPA")

# Show graph
plt.show()