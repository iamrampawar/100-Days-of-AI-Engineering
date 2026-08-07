import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student.csv")

# Count plot of Branch
sns.countplot(x="Branch", data=df)

# Add title
plt.title("Number of Students in Each Branch")

# Show graph
plt.show()