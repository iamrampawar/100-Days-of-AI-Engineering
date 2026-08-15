import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)


# 1. Load dataset
data = pd.read_csv("student.csv")

print("Dataset:")
print(data)


# 2. Create target variable
data["Passed"] = (data["Marks"] >= 40).astype(int)

print("\nTarget Variable:")
print(data[["Name", "Marks", "Passed"]])


# 3. Select features
X = data[["StudyHours", "Attendance"]]

print("\nFeatures:")
print(X)


# 4. Select target
y = data["Passed"]

print("\nTarget:")
print(y)


# 5. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)


# 6. Create Gradient Boosting model
model = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)


# 7. Train model
model.fit(X_train, y_train)


# 8. Make predictions
y_pred = model.predict(X_test)

print("\nPredictions:")
print(y_pred)

print("\nActual:")
print(y_test.values)


# 9. Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)


# 10. Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)


# 11. Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# 12. Predict a new student
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