import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv("student.csv")

print("Dataset:")
print(df)

# Features
X = df[["StudyHours", "Attendance"]]

# Target
y = df["Marks"]

print("\nFeatures:")
print(X)

print("\nTarget:")
print(y)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

print("\nPredictions:")
print(predictions)

print("\nActual:")
print(y_test.values)

# Evaluation
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nMean Absolute Error:", mae)
print("R2 Score:", r2)

# Predict marks for a new student
new_student = [[7, 90]]

predicted_marks = model.predict(new_student)

print("\nNew Student:")
print("Study Hours: 7")
print("Attendance: 90")

print("\nPredicted Marks:", predicted_marks[0])