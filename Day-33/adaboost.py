import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)


# --------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------

data = pd.read_csv("student.csv")

print("Dataset:")
print(data)


# --------------------------------------------------
# 2. Create Target Variable
# --------------------------------------------------

data["Passed"] = (data["Marks"] >= 40).astype(int)

print("\nTarget Variable:")
print(data[["Name", "Marks", "Passed"]])


# --------------------------------------------------
# 3. Select Features
# --------------------------------------------------

X = data[["StudyHours", "Attendance"]]

Y = data["Passed"]

print("\nFeatures:")
print(X)

print("\nTarget:")
print(Y)


# --------------------------------------------------
# 4. Split Dataset
# --------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.25,
    random_state=42,
    stratify=Y
)


# --------------------------------------------------
# 5. Create Weak Learner
# --------------------------------------------------

weak_learner = DecisionTreeClassifier(
    max_depth=1,
    random_state=42
)


# --------------------------------------------------
# 6. Create AdaBoost Model
# --------------------------------------------------

model = AdaBoostClassifier(
    estimator=weak_learner,
    n_estimators=50,
    random_state=42
)


# --------------------------------------------------
# 7. Train Model
# --------------------------------------------------

model.fit(X_train, Y_train)


# --------------------------------------------------
# 8. Make Predictions
# --------------------------------------------------

Y_pred = model.predict(X_test)

print("\nPredictions:")
print(Y_pred)

print("\nActual:")
print(Y_test.to_numpy())


# --------------------------------------------------
# 9. Calculate Accuracy
# --------------------------------------------------

accuracy = accuracy_score(Y_test, Y_pred)

print("\nAccuracy:", accuracy)


# --------------------------------------------------
# 10. Confusion Matrix
# --------------------------------------------------

cm = confusion_matrix(Y_test, Y_pred)

print("\nConfusion Matrix:")
print(cm)


# --------------------------------------------------
# 11. Classification Report
# --------------------------------------------------

report = classification_report(Y_test, Y_pred)

print("\nClassification Report:")
print(report)


# --------------------------------------------------
# 12. Predict New Student
# --------------------------------------------------

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