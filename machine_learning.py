# # --- IMPORT SECTION --
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,Ridge
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.metrics import mean_squared_error
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

# Evaluate Linear Regression
rmse_lin = math.sqrt(mean_squared_error(y_test, y_lin_pred))
print(f"Linear Regression RMSE: {rmse_lin:.2f}")

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

# Visualization: Scatter plots with regression line
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# TV vs Sales
sns.regplot(x=df["TV"], y=df["sales"], ax=axes[0], scatter_kws={"alpha":0.5}, line_kws={"color":"blue"})
axes[0].set_title("TV vs Sales")
axes[0].set_xlabel("TV Advertising Budget")
axes[0].set_ylabel("Sales")

# Radio vs Sales
sns.regplot(x=df["radio"], y=df["sales"], ax=axes[1], scatter_kws={"alpha":0.5}, line_kws={"color":"red"})
axes[1].set_title("Radio vs Sales")
axes[1].set_xlabel("Radio Advertising Budget")
axes[1].set_ylabel("Sales")

# Newspapers vs Sales
sns.regplot(x=df["newspaper"], y=df["sales"], ax=axes[2], scatter_kws={"alpha":0.5}, line_kws={"color":"green"})
axes[2].set_title("Newspaper vs Sales")
axes[2].set_xlabel("Newspaper Advertising Budget")
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
