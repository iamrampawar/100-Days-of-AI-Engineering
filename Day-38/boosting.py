# Day 38 - Boosting Algorithms
# AdaBoost, Gradient Boosting and XGBoost

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier


# 1. Load Dataset
data = load_breast_cancer()

X = data.data
y = data.target


# 2. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 3. AdaBoost
ada_model = AdaBoostClassifier(
    n_estimators=100,
    random_state=42
)

ada_model.fit(X_train, y_train)

ada_predictions = ada_model.predict(X_test)

ada_accuracy = accuracy_score(y_test, ada_predictions)


# 4. Gradient Boosting
gb_model = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    random_state=42
)

gb_model.fit(X_train, y_train)

gb_predictions = gb_model.predict(X_test)

gb_accuracy = accuracy_score(y_test, gb_predictions)


# 5. XGBoost
xgb_model = XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42,
    eval_metric="logloss"
)

xgb_model.fit(X_train, y_train)

xgb_predictions = xgb_model.predict(X_test)

xgb_accuracy = accuracy_score(y_test, xgb_predictions)


# 6. Display Results
print("=" * 50)
print("DAY 38 - BOOSTING ALGORITHMS")
print("=" * 50)

print("\nAdaBoost Accuracy:", round(ada_accuracy, 4))
print("Gradient Boosting Accuracy:", round(gb_accuracy, 4))
print("XGBoost Accuracy:", round(xgb_accuracy, 4))


# 7. Model Comparison
print("\n" + "=" * 50)
print("MODEL COMPARISON")
print("=" * 50)

models = {
    "AdaBoost": ada_accuracy,
    "Gradient Boosting": gb_accuracy,
    "XGBoost": xgb_accuracy
}

for model, accuracy in models.items():
    print(f"{model:20} : {accuracy:.4f}")


# 8. Best Model
best_model = max(models, key=models.get)

print("\nBest Model:", best_model)
print("Best Accuracy:", f"{models[best_model]:.4f}")


# 9. XGBoost Classification Report
print("\n" + "=" * 50)
print("XGBOOST CLASSIFICATION REPORT")
print("=" * 50)

print(classification_report(y_test, xgb_predictions))