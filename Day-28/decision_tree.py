import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# Load dataset
df = pd.read_csv("student.csv")

print("Dataset:")
print(df)


# Create target variable
df["Passed"] = (df["Marks"] >= 40).astype(int)

print("\nTarget Variable:")
print(df[["Name", "Marks", "Passed"]])


# Select features and target
X = df[["StudyHours", "Attendance"]]
y = df["Passed"]


print("\nFeatures:")
print(X)

print("\nTarget:")
print(y)


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)


# Create Decision Tree model
model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)


# Train model
model.fit(X_train, y_train)


# Make predictions
y_pred = model.predict(X_test)


print("\nPredictions:")
print(y_pred)

print("\nActual:")
print(y_test.values)


# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)


# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# Predict for a new student
new_student = pd.DataFrame({
    "StudyHours": [7],
    "Attendance": [90]
})

prediction = model.predict(new_student)

print("\nNew Student:")
print("Study Hours:", new_student["StudyHours"].iloc[0])
print("Attendance:", new_student["Attendance"].iloc[0])

if prediction[0] == 1:
    print("Prediction: Passed")
else:
    print("Prediction: Failed")