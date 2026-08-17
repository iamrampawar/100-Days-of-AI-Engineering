import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score


# Load dataset
data = pd.read_csv("student.csv")

print("Dataset:")
print(data)


# Features
X = data[["StudyHours", "Attendance"]]

print("\nFeatures:")
print(X)


# Target
y = data["Passed"]

print("\nTarget:")
print(y)


# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# 5-Fold Cross-Validation
scores = cross_val_score(
    model,
    X,
    y,
    cv=5
)


# Display scores
print("\nCross-Validation Scores:")
print(scores)


# Mean score
print("\nMean Cross-Validation Score:")
print(scores.mean())


# Standard deviation
print("\nStandard Deviation:")
print(scores.std())