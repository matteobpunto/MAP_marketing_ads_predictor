from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

app = Flask(__name__)

# Carica i modelli e gli scaler
scaler = joblib.load('scaler.pkl')
poly = joblib.load('polynomial_transformer.pkl')
lin_model = joblib.load('linear_regression_model.pkl')
poly_model = joblib.load('polynomial_regression_model.pkl')

# Route principale
@app.route("/")
def landing_page():
    return render_template("prova.html")

# Route per gestire l'invio del form
@app.route("/calcola_previsioni", methods=['POST'])
def calcola_previsioni():
    if request.method == 'POST':
        # Recupera i dati dal form
        company = request.form['company']
        tv = float(request.form['tv'])
        radio = float(request.form['radio'])
        newspaper = float(request.form['newspaper'])

        # Prepara i dati per la previsione
        input_data = pd.DataFrame([[tv, radio, newspaper]], columns=["TV", "radio", "newspaper"])
        input_data_scaled = scaler.transform(input_data)
        input_data_poly = poly.transform(input_data_scaled)

        # Calcola le previsioni di vendita
        lin_pred = lin_model.predict(input_data_scaled)
        poly_pred = poly_model.predict(input_data_poly)

        # Mostra i risultati delle previsioni
        return render_template("prova.html",
                              company=company,
                              tv=tv,
                              radio=radio,
                              newspaper=newspaper,
                              lin_pred=f"{lin_pred[0]:.2f}",
                              poly_pred=f"{poly_pred[0]:.2f}")

if __name__ == "__main__":
    app.run(debug=True)