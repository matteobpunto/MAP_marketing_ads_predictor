import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics  import mean_absolute_error
import math
import joblib
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

file_path = "../data_cleaning/file_clear.csv"
df = pd.read_csv(file_path)

X = df[["TV", "radio", "newspaper"]]
y = df["sales"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

lin_model = LinearRegression()
lin_model.fit(X_train_scaled, y_train)

poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

def predict_sales(tv, radio, newspaper):
    # Create a numpy array with the input values
    input_data = pd.DataFrame([[tv, radio, newspaper]], columns=["TV", "radio", "newspaper"])
    input_data_scaled = scaler.transform(input_data)

    lin_pred = lin_model.predict(input_data_scaled)
    input_data_poly = poly.transform(input_data_scaled)
    poly_pred = poly_model.predict(input_data_poly)

    return lin_pred[0], poly_pred[0]


joblib.dump(lin_model, 'linear_regression_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(poly_model, 'polynomial_regression_model.pkl')
joblib.dump(poly, 'polynomial_transformer.pkl')

lin_test_pred = lin_model.predict(X_test_scaled)
poly_test_pred = poly_model.predict(X_test_poly)

#=== LINEAR MODEL METRICS ===
print("\n--- Linear Regression Metrics ---")
print(f"R² (accuracy): {r2_score(y_test, lin_test_pred):.4f}")
print(f"MAE: {mean_absolute_error(y_test, lin_test_pred):.4f}")
print(f"MSE: {mean_squared_error(y_test, lin_test_pred):.4f}")
print(f"RMSE: {math.sqrt(mean_squared_error(y_test, lin_test_pred)):.4f}")

#=== POLYNOMIAL MODEL METRICS ===
print("\n--- Polynomial Regression Metrics ---")
print(f"R² (accuracy): {r2_score(y_test, poly_test_pred):.4f}")
print(f"MAE: {mean_absolute_error(y_test, poly_test_pred):.4f}")
print(f"MSE: {mean_squared_error(y_test, poly_test_pred):.4f}")
print(f"RMSE: {math.sqrt(mean_squared_error(y_test, poly_test_pred)):.4f}")