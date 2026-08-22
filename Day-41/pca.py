import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# --------------------------------
# 1. Load Dataset
# --------------------------------

data = pd.read_csv("student.csv")

print("Dataset:")
print(data)


# --------------------------------
# 2. Select Features
# --------------------------------

features = [
    "StudyHours",
    "Attendance",
    "Assignments",
    "PreviousMarks",
    "PracticeHours"
]

X = data[features]

y = data["Passed"]

print("\nFeatures:")
print(X)

print("\nTarget:")
print(y)


# --------------------------------
# 3. Scale the Features
# --------------------------------

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("\nScaled Features:")
print(X_scaled)


# --------------------------------
# 4. Apply PCA
# --------------------------------

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)


# --------------------------------
# 5. Create PCA DataFrame
# --------------------------------

pca_data = pd.DataFrame(
    X_pca,
    columns=["PC1", "PC2"]
)

pca_data["Passed"] = y.values

print("\nPCA Result:")
print(pca_data)


# --------------------------------
# 6. Explained Variance
# --------------------------------

print("\nExplained Variance Ratio:")

print(pca.explained_variance_ratio_)

print("\nTotal Explained Variance:")

print(pca.explained_variance_ratio_.sum())


# --------------------------------
# 7. Visualize PCA
# --------------------------------

plt.figure(figsize=(8, 6))

for label in [0, 1]:

    subset = pca_data[pca_data["Passed"] == label]

    plt.scatter(
        subset["PC1"],
        subset["PC2"],
        label=f"Passed = {label}"
    )


plt.xlabel("Principal Component 1")

plt.ylabel("Principal Component 2")

plt.title("PCA - Student Performance")

plt.legend()

plt.grid(True)

plt.show()