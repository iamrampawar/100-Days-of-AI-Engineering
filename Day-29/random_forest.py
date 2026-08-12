import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)


# -----------------------------------
# 1. Load Dataset
# -----------------------------------

df = pd.read_csv("student.csv")

print("Dataset:")
print(df)


# -----------------------------------
# 2. Create Target Variable
# -----------------------------------

df["Passed"] = (df["Marks"] >= 40).astype(int)

print("\nTarget Variable:")
print(df[["Name", "Marks", "Passed"]])


# -----------------------------------
# 3. Select Features
# -----------------------------------

X = df[["StudyHours", "Attendance"]]

y = df["Passed"]

print("\nFeatures:")
print(X)

print("\nTarget:")
print(y)


# -----------------------------------
# 4. Split Dataset
# -----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)


# -----------------------------------
# 5. Create Random Forest Model
# -----------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# -----------------------------------
# 6. Train Model
# -----------------------------------

model.fit(X_train, y_train)


# -----------------------------------
# 7. Make Predictions
# -----------------------------------

y_pred = model.predict(X_test)

print("\nPredictions:")
print(y_pred)

print("\nActual:")
print(y_test.values)


# -----------------------------------
# 8. Accuracy
# -----------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)


# -----------------------------------
# 9. Confusion Matrix
# -----------------------------------

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)


# -----------------------------------
# 10. Classification Report
# -----------------------------------

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# -----------------------------------
# 11. Predict New Student
# -----------------------------------

study_hours = 7
attendance = 90

new_student = pd.DataFrame({
    "StudyHours": [study_hours],
    "Attendance": [attendance]
})

prediction = model.predict(new_student)

print("\nNew Student:")
print("Study Hours:", study_hours)
print("Attendance:", attendance)

if prediction[0] == 1:
    print("Prediction: Passed")
else:
    print("Prediction: Failed")