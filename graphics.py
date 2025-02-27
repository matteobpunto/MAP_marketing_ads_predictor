#---IMPORT SECTION---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import math
#---END OF IMPORT SECTION---

#Load the CSV file
file_path = "Advertising_clear.csv"
df = pd.read_csv(file_path)

#Separate independent and dependent variables
X = df[["TV", "radio", "newspaper"]]
y = df["sales"]

#Split the dataset into training and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

#Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#Create and train the linear regression model
model = LinearRegression()
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)

#Evaluate the model
rmse = math.sqrt(mean_squared_error(y_test, y_pred))
print(f"Model RMSE: {rmse:.2f}")

#Create scatter plots with regression line
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

#TV vs Sales
sns.regplot(x=df["TV"], y=df["sales"], ax=axes[0], scatter_kws={"alpha":0.5}, line_kws={"color":"blue"})
axes[0].set_title("TV vs Sales")
axes[0].set_xlabel("TV Advertising Budget")
axes[0].set_ylabel("Sales")

#Radio vs Sales
sns.regplot(x=df["radio"], y=df["sales"], ax=axes[1], scatter_kws={"alpha":0.5}, line_kws={"color":"red"})
axes[1].set_title("Radio vs Sales")
axes[1].set_xlabel("Radio Advertising Budget")
axes[1].set_ylabel("Sales")

#Newspapers vs Sales
sns.regplot(x=df["newspaper"], y=df["sales"], ax=axes[2], scatter_kws={"alpha":0.5}, line_kws={"color":"green"})
axes[2].set_title("Newspaper vs Sales")
axes[2].set_xlabel("Newspaper Advertising Budget")
axes[2].set_ylabel("Sales")

#Show plots
plt.tight_layout()
plt.show()

#La parte successiva era il codice che abbiamo scritto noi, tuttavia non riuscivamo a stampare tre titoli distinti
#per i tre grafici, quindi abbiamo chiesto a chatgpt
# #TV vs Sales
# sns.regplot(x=df["TV"], y=df["sales"], ax=axes[0], scatter_kws={"alpha":0.5}, line_kws={"color":"blue"})
# plt.xlabel("TV Advertising Budget")
# plt.ylabel("Sales")
#
# #Radio vs Sales
# sns.regplot(x=df["radio"], y=df["sales"], ax=axes[1], scatter_kws={"alpha":0.5}, line_kws={"color":"red"})
# plt.xlabel("Radio Advertising Budget")
# plt.ylabel("Sales")
#
# #Newspapers vs Sales
# sns.regplot(x=df["newspaper"], y=df["sales"], ax=axes[2], scatter_kws={"alpha":0.5}, line_kws={"color":"green"})
# plt.title("Newspaper vs Sales")
# plt.xlabel("Newspaper Advertising Budget")
# plt.ylabel("Sales(u)")
#
# #Show plots
# plt.tight_layout()
# plt.show()