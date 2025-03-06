# --- IMPORT SECTION --
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
import pickle
from joblib import dump, load
# --- END OF IMPORT SECTION --

# Load the CSV file
file_path = "Advertising_clear.csv"
df = pd.read_csv(file_path)

# Sales Distribution
plt.figure(figsize=(6, 4))
sns.histplot(df["sales"], bins=15, kde=True, color="blue")
plt.title("Distribution of Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# Creating a pair plot to visualize relationships between variables
sns.pairplot(data=df)
# plt.show()

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

# Stampa dei coefficienti
print("Coefficienti del modello:",lin_model.coef_ ) #Feature 1: tv, feature 2: radio, feature 3: newspaper

# Evaluate Linear Regression
rmse_lin = math.sqrt(mean_squared_error(y_test, y_lin_pred))
print(f"Linear Regression RMSE: {rmse_lin:.2f}")
mae_lin = mean_absolute_error(y_test, y_lin_pred)
print(f"Linear Regression MAE: {mae_lin:.2f}")
mse_lin = mean_squared_error(y_test, y_lin_pred)
print(f"Linear Regression MSE: {mse_lin:.2f}")

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
mse_poly = mean_squared_error(y_test, y_poly_pred)
print(f"Polynomial Regression MSE: {mse_poly:.2f}")

# Visualization: Scatter plots of predicted vs actual data
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(16, 6))

# TV vs Sales (test set only)
axes[0].plot(X_test['TV'], y_test, 'o', label='Actual Sales')
axes[0].plot(X_test['TV'], y_lin_pred, 'o', color='red', label='Predicted Sales (Linear)')
axes[0].plot(X_test['TV'], y_poly_pred, 'o', color='green', label='Predicted Sales (Polynomial)')
axes[0].set_ylabel("Sales")
axes[0].set_title("TV Spend")
axes[0].legend()

# Radio vs Sales (test set only)
axes[1].plot(X_test['radio'], y_test, 'o', label='Actual Sales')
axes[1].plot(X_test['radio'], y_lin_pred, 'o', color='red', label='Predicted Sales (Linear)')
axes[1].plot(X_test['radio'], y_poly_pred, 'o', color='green', label='Predicted Sales (Polynomial)')
axes[1].set_title("Radio Spend")
axes[1].set_ylabel("Sales")
axes[1].legend()

# Newspaper vs Sales (test set only)
axes[2].plot(X_test['newspaper'], y_test, 'o', label='Actual Sales')
axes[2].plot(X_test['newspaper'], y_lin_pred, 'o', color='red', label='Predicted Sales (Linear)')
axes[2].plot(X_test['newspaper'], y_poly_pred, 'o', color='green', label='Predicted Sales (Polynomial)')
axes[2].set_title("Newspaper Spend")
axes[2].set_ylabel("Sales")
axes[2].legend()

# show the plot
plt.tight_layout()
plt.show()

# Correlation Matrix
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()


# Load the CSV file
file_path = "file_clear.csv"
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


# Initialize lists to store RMSE errors
train_rmse_errors = []
test_rmse_errors = []

degree = 9

poly_converter = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly_converter.fit_transform(X_train_scaled)  # Apply to training data
X_test_poly = poly_converter.transform(X_test_scaled)       # Apply to test data

# Train the model on the polynomial training data
model = LinearRegression(fit_intercept=True)
model.fit(X_train_poly, y_train)  # Fit the model using the training data

# Predict on the training and test data
train_pred = model.predict(X_train_poly)
test_pred = model.predict(X_test_poly)

# Calculate the RMSE errors
train_rmse = np.sqrt(mean_squared_error(y_train, train_pred))
test_rmse = np.sqrt(mean_squared_error(y_test, test_pred))

# Append RMSE errors to the lists
train_rmse_errors.append(train_rmse)
test_rmse_errors.append(test_rmse)

# Stampa dei coefficienti
print("Coefficienti del modello:",model.coef_ ) #Feature 1: tv, feature 2: radio, feature 3: newspaper
                                                #Feature 1^2: tv^2, feature 2^2: radio^2, feature 3^2: newspaper^2
                                                #Feature 1 x feature 2: tv x radio, feature 1 x feature 3: tv x newspaper,
                                                #feature 2 x feature 3: radio x newspaper

# Loop through degrees 1 to 5 for polynomial regression
for d in range(1, degree):  # Loop from degree 1 to 5
    # Create polynomial features for degree 'd'
    poly_converter = PolynomialFeatures(degree=d, include_bias=False)
    X_train_poly = poly_converter.fit_transform(X_train_scaled)  # Apply to training data
    X_test_poly = poly_converter.transform(X_test_scaled)       # Apply to test data

    # Train the model on the polynomial training data
    model = LinearRegression(fit_intercept=True)
    model.fit(X_train_poly, y_train)  # Fit the model using the training data

    # Predict on the training and test data
    train_pred = model.predict(X_train_poly)
    test_pred = model.predict(X_test_poly)

    # Calculate the RMSE errors
    train_rmse = np.sqrt(mean_squared_error(y_train, train_pred))
    test_rmse = np.sqrt(mean_squared_error(y_test, test_pred))

    # Append RMSE errors to the lists
    train_rmse_errors.append(train_rmse)
    test_rmse_errors.append(test_rmse)

# Plotting RMSE for different polynomial degrees
plt.figure(figsize=(8, 6))
plt.plot(range(1, degree + 1), train_rmse_errors, label='TRAIN', marker='o')
plt.plot(range(1, degree + 1), test_rmse_errors, label='TEST', marker='o')
plt.xlabel("Polynomial Complexity")
plt.ylabel("RMSE")
plt.title("RMSE vs Polynomial Complexity")
plt.legend()
plt.grid(True)
plt.show()


# Salva il modello addestrato in un file .pkl
# with open('regression_model.pkl', 'wb') as file:
#     pickle.dump((scaler, model), file)
#     print("Modello salvato come 'regression_model.pkl'")


