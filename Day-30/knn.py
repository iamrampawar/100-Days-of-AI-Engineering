import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)
from sklearn.preprocessing import StandardScaler


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
# 5. Feature Scaling
# -----------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

X_test_scaled = scaler.transform(X_test)


# -----------------------------------
# 6. Create KNN Model
# -----------------------------------

model = KNeighborsClassifier(n_neighbors=3)


# -----------------------------------
# 7. Train Model
# -----------------------------------

model.fit(X_train_scaled, y_train)


# -----------------------------------
# 8. Make Predictions
# -----------------------------------

y_pred = model.predict(X_test_scaled)

print("\nPredictions:")
print(y_pred)

print("\nActual:")
print(y_test.values)


# -----------------------------------
# 9. Accuracy
# -----------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)


# -----------------------------------
# 10. Confusion Matrix
# -----------------------------------

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)


# -----------------------------------
# 11. Classification Report
# -----------------------------------

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# -----------------------------------
# 12. Predict New Student
# -----------------------------------

study_hours = 7
attendance = 90

new_student = pd.DataFrame({
    "StudyHours": [study_hours],
    "Attendance": [attendance]
})

new_student_scaled = scaler.transform(new_student)

prediction = model.predict(new_student_scaled)

print("\nNew Student:")
print("Study Hours:", study_hours)
print("Attendance:", attendance)

if prediction[0] == 1:
    print("Prediction: Passed")
else:
    print("Prediction: Failed")