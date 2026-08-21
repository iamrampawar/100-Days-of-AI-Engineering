# Day 40 - Feature Selection
# 100 Days of AI/ML Engineering

import pandas as pd

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, f_regression, RFE
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# --------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------

data = load_diabetes()

X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name="target")

print("Original Features:")
print(X.columns.tolist())


# --------------------------------------------------
# 2. Correlation Analysis
# --------------------------------------------------

correlation = X.corrwith(y).abs().sort_values(ascending=False)

print("\nFeature Correlation with Target:")
print(correlation)


# Select top 5 correlated features
top_features = correlation.head(5).index

X_corr = X[top_features]

print("\nTop 5 Features using Correlation:")
print(top_features.tolist())


# --------------------------------------------------
# 3. SelectKBest
# --------------------------------------------------

selector = SelectKBest(score_func=f_regression, k=5)

X_selected = selector.fit_transform(X, y)

selected_features = X.columns[selector.get_support()]

print("\nTop 5 Features using SelectKBest:")
print(selected_features.tolist())


# --------------------------------------------------
# 4. Train-Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X_selected,
    y,
    test_size=0.2,
    random_state=42
)


# --------------------------------------------------
# 5. Train Model
# --------------------------------------------------

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)


# --------------------------------------------------
# 6. Evaluate Model
# --------------------------------------------------

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print("Mean Squared Error:", mse)
print("R2 Score:", r2)


# --------------------------------------------------
# 7. Recursive Feature Elimination (RFE)
# --------------------------------------------------

rfe_model = LinearRegression()

rfe = RFE(
    estimator=rfe_model,
    n_features_to_select=5
)

rfe.fit(X, y)

rfe_features = X.columns[rfe.support_]

print("\nTop 5 Features using RFE:")
print(rfe_features.tolist())


# --------------------------------------------------
# Final Summary
# --------------------------------------------------

print("\nFeature Selection Completed Successfully!")