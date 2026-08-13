import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (

    accuracy_score,
    confusion_matrix,
    classification_report

)

df = pd.read_csv("student.csv")

print("Dataset:")
print(df)

df["Passed"] = (df["Marks"] >= 40).astype(int)

print("\nTarget Variable:")
print(df[["Name", "Marks", "Passed"]])

X = df[["StudyHours" , "Attendance"]]

Y = df["Passed"]

print("\nFeatures:")
print(X)

print("\nTarget")
print(Y)

#split dataset
X_train, X_test , Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size = 0.25,
    random_state=42,
    stratify=Y
)

#create Native Bayes model
model = GaussianNB()

#Train model 
model.fit(X_train, Y_train)

#Make predictions
Y_pred = model.predict(X_test)

print("\nPredictions:")
print(Y_pred)

print("\nActual:")
print(Y_test.values)

#Calculate accuracy
accuracy = accuracy_score(Y_test , Y_pred)

print("\nAccuracy:", accuracy)


#Confusion Matrix
cm = confusion_matrix(Y_test, Y_pred)

print("\nClassification Report:")
print(classification_report(Y_test,Y_pred))

#Predict a new student
new_student = pd.DataFrame (
    [[7, 90]],
    columns = ["StudyHours", "Attendance"]

)

prediction = model.predict(new_student)

print("\nNew Student:")
print("Study Hours: 7")
print("Attendance: 90")

if prediction[0] == 1:
    print("Prediction: Passed")
else:
    print("Prediction: Failed")