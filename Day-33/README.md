# Day 33 - AdaBoost Classification

## 📚 Topic

Today I learned about **AdaBoost (Adaptive Boosting)** and implemented an AdaBoost classification model using Python and Scikit-learn.

---

## 🧠 What is AdaBoost?

AdaBoost stands for **Adaptive Boosting**.

It is an ensemble machine learning algorithm that combines multiple weak learners to create a stronger model.

AdaBoost trains weak learners sequentially and gives more importance to the examples that previous learners classified incorrectly.

### Basic Process

```text
Training Data
      ↓
Weak Learner 1
      ↓
Find Incorrect Predictions
      ↓
Increase Importance of Mistakes
      ↓
Weak Learner 2
      ↓
Repeat
      ↓
Combine Weak Learners
      ↓
Strong Model