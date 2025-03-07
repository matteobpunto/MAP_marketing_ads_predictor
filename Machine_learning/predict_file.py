import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures, StandardScaler


print("Enter the values for TV, Radio, and Newspaper to generate sales predictions.")
tv = float(input("Value for TV: "))
radio = float(input("Value for Radio: "))
newspaper = float(input("Value for Newspaper: "))

scaler = joblib.load('scaler.pkl')
poly = joblib.load('polynomial_transformer.pkl')

input_data = pd.DataFrame([[tv, radio, newspaper]], columns=["TV", "radio", "newspaper"])
input_data_scaled = scaler.transform(input_data)
input_data_poly = poly.transform(input_data_scaled)

lin_model = joblib.load('linear_regression_model.pkl')
poly_model = joblib.load('polynomial_regression_model.pkl')

lin_pred = lin_model.predict(input_data_scaled)
poly_pred = poly_model.predict(input_data_poly)
print(f"\nSales Prediction (Linear Regression): {lin_pred[0]:.2f}")
print(f"Sales Prediction (Polynomial Regression): {poly_pred[0]:.2f}")

