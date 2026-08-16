# Day 35 - Random Forest 🌲🌲🌲

## 📚 What I Learned

Today I learned about the Random Forest algorithm.

Random Forest is a supervised machine learning algorithm that combines multiple Decision Trees to make better predictions.

Instead of relying on a single Decision Tree, Random Forest creates many trees and combines their predictions using voting.

---

## 🧠 Key Concepts

- Random Forest
- Decision Trees
- Ensemble Learning
- Multiple Decision Trees
- Majority Voting
- Classification
- Training and Testing
- Accuracy
- Confusion Matrix
- Classification Report

---

## 🔍 Dataset

The dataset contains student information:

- Name
- Study Hours
- Attendance
- Marks

The target variable is:

`Passed`

Where:

- `1` = Passed
- `0` = Failed

A student is considered passed when Marks >= 40.

---

## ⚙️ Features

The model uses:

- StudyHours
- Attendance

to predict whether a student will pass.

---

## 🌲 Random Forest

Random Forest consists of multiple Decision Trees.

Each tree makes its own prediction and the final prediction is determined through majority voting.

Example:

```text
Tree 1 → Passed
Tree 2 → Passed
Tree 3 → Failed
Tree 4 → Passed
Tree 5 → Passed

Final Prediction → Passed