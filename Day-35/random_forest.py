import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)


# Load dataset
data = pd.read_csv("student.csv")

print("Dataset:")
print(data)


# Create target variable
data["Passed"] = (data["Marks"] >= 40).astype(int)

print("\nTarget Variable:")
print(data[["Name", "Marks", "Passed"]])


# Select features
X = data[["StudyHours", "Attendance"]]

# Select target
Y = data["Passed"]

print("\nFeatures:")
print(X)

print("\nTarget:")
print(Y)


# Split dataset into training and testing data
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.25,
    random_state=42
)


# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train the model
model.fit(X_train, Y_train)


# Make predictions
Y_pred = model.predict(X_test)

print("\nPredictions:")
print(Y_pred)

print("\nActual:")
print(Y_test.values)


# Calculate accuracy
accuracy = accuracy_score(Y_test, Y_pred)

print("\nAccuracy:")
print(accuracy)


# Confusion Matrix
cm = confusion_matrix(Y_test, Y_pred)

print("\nConfusion Matrix:")
print(cm)


# Classification Report
report = classification_report(Y_test, Y_pred)

print("\nClassification Report:")
print(report)


# Test a new student
new_student = pd.DataFrame(
    [[7, 90]],
    columns=["StudyHours", "Attendance"]
)

prediction = model.predict(new_student)

print("\nNew Student:")
print("Study Hours:", new_student.iloc[0]["StudyHours"])
print("Attendance:", new_student.iloc[0]["Attendance"])

if prediction[0] == 1:
    print("Prediction: Passed")
else:
    print("Prediction: Failed")