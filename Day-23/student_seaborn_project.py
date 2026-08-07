import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load dataset
current_dir = os.path.dirname(__file__)
csv_path = os.path.join(current_dir, "student.csv")

df = pd.read_csv(csv_path)

# -----------------------------
# 1. Scatter Plot
# -----------------------------
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x="Marks", y="CGPA", hue="Branch", s=100)

plt.title("Marks vs CGPA")
plt.show()


# -----------------------------
# 2. Count Plot
# -----------------------------
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Branch")

plt.title("Students in Each Branch")
plt.show()


# -----------------------------
# 3. Box Plot
# -----------------------------
plt.figure(figsize=(6,4))
sns.boxplot(data=df, x="Branch", y="Marks")

plt.title("Marks Distribution by Branch")
plt.show()


# -----------------------------
# 4. Heatmap
# -----------------------------
plt.figure(figsize=(5,4))

numeric_df = df.select_dtypes(include="number")

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()