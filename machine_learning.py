# # --- IMPORT SECTION --
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,Ridge
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics  import mean_absolute_error
import math
# # --- END OF IMPORT SECTION --


# Load the CSV file
file_path = "Advertising_clear.csv"
df = pd.read_csv(file_path)

# Separate independent and dependent variables
X = df[["TV", "radio", "newspaper"]]
y = df["sales"]

# Split the dataset into training and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Linear Regression Model
lin_model = LinearRegression()
lin_model.fit(X_train_scaled, y_train)
y_lin_pred = lin_model.predict(X_test_scaled)

# Define y_hat for Linear Regression predictions
y_hat = y_lin_pred

# Evaluate Linear Regression
rmse_lin = math.sqrt(mean_squared_error(y_test, y_lin_pred))
print(f"Linear Regression RMSE: {rmse_lin:.2f}")
mae_lin = mean_absolute_error(y_test, y_lin_pred)
print(f"Linear Regression MAE: {mae_lin:.2f}")

# Polynomial Regression (Degree = 2)
poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)
y_poly_pred = poly_model.predict(X_test_poly)

# Evaluate Polynomial Regression
rmse_poly = math.sqrt(mean_squared_error(y_test, y_poly_pred))
print(f"Polynomial Regression RMSE: {rmse_poly:.2f}")
mae_poly = mean_absolute_error(y_test, y_poly_pred)
print(f"Polynomial Regression MAE: {mae_poly:.2f}")

# Visualization: Scatter plots with regression line
fig, axes = plt.subplots(1, 3, figsize=(16, 6))

# TV vs Sales
axes[0].plot(df['TV'],df['sales'], 'o')
axes[0].plot(df['TV'],y_hat, 'o', color = 'red')
axes[0].set_ylabel("Sales")
axes[0].set_title("TV sspend")

# Radio vs Sales
axes[1].plot(df['radio'],df['sales'], 'o')
axes[1].plot(df['radio'],y_hat, 'o', color = 'red')
axes[1].set_title("Radio Spend")
axes[1].set_ylabel("Sales")

# Newspapers vs Sales
axes[2].plot(df['newspaper'],df['sales'], 'o')
axes[2].plot(df['newspaper'],y_hat, 'o', color = 'red')
axes[2].set_title("Newspaper spend")
axes[2].set_ylabel("Sales")


# Show plots
plt.tight_layout()
plt.show()

# Correlation Matrix
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

# Sales Distribution
plt.figure(figsize=(6,4))
sns.histplot(df["sales"], bins=15, kde=True, color="blue")
plt.title("Distribution of Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()
