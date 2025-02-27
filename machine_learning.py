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
#
# # --- MAIN CODE ---
#
# # Importing the dataset
path_to_data = "Advertising_modified.csv"
data = pd.read_csv(path_to_data)
#
# # Visualizing the dataset
print(f"\nHere are the first 5 rows of the dataset: {data.head()}")
#
print(data.describe())