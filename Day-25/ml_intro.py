import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("student.csv")

print("Dataset:")
print(df)

# Create target
df["Passed"] = (df["Marks"] >= 40).astype(int)

# Features and target
X = df[["StudyHours", "Attendance"]]
y = df["Passed"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# Create model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)

print("\nPredictions:")
print(y_pred)

print("\nActual:")
print(y_test.values)

print("\nAccuracy:", accuracy)