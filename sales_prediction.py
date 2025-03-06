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

file_path = "file_clear.csv"
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
    input_data = np.array([[tv, radio, newspaper]])
    input_data_scaled = scaler.transform(input_data)

    lin_pred = lin_model.predict(input_data_scaled)
    input_data_poly = poly.transform(input_data_scaled)
    poly_pred = poly_model.predict(input_data_poly)

    return lin_pred[0], poly_pred[0]

print("Inserisci i valori per TV, Radio e Newspaper per generare le previsioni di vendite.")
tv = float(input("Valore per TV: "))
radio = float(input("Valore per Radio: "))
newspaper = float(input("Valore per Newspaper: "))

lin_pred, poly_pred = predict_sales(tv, radio, newspaper)

print(f"\nPrevisione di vendite (Regressione Lineare): {lin_pred:.2f}")
print(f"Previsione di vendite (Regressione Polinomiale): {poly_pred:.2f}")