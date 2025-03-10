from flask import Flask, render_template, request
import mysql
import mysql.connector
import csv

from matplotlib.pyplot import margins
from mysql.connector import Error
from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64
import joblib
import pandas as pd
import os #serve per caricare modelli da un'altra cartella
import numpy as np
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="marketing_adv"
    )

def fetch_data(query):
    try:
        connection = get_db_connection()
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)  # Fetch results as dictionaries
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")
        return None
    finally:
        if connection.is_connected():
            connection.close()

app = Flask(__name__)

# Percorso della cartella dei modelli
model_path = os.path.join("static", "prev_model")

# Caricamento dei modelli
scaler = joblib.load(os.path.join(model_path, "scaler.pkl"))
poly = joblib.load(os.path.join(model_path, "polynomial_transformer.pkl"))
lin_model = joblib.load(os.path.join(model_path, "linear_regression_model.pkl"))
poly_model = joblib.load(os.path.join(model_path, "polynomial_regression_model.pkl"))

@app.route("/")
def landing_page():

    return render_template("index.html")

@app.route("/launch_campaign", methods=['GET', 'POST'])
def launch_campaign():
    if request.method == 'POST':
        company = request.form.get("company")
        tv = request.form.get("tv")
        radio = request.form.get("radio")
        newspaper = request.form.get("newspaper")

        print(f"Company: {company}, TV: {tv}, Radio: {radio}, Newspaper: {newspaper}")

    return render_template("launch_campaign.html")  # ✅ Mostra sempre l'HTML, sia per GET che POST



@app.route("/company/<string:name>")
def visualization_data(name):
    query = """
    SELECT company.company_id, company.name, 
           SUM(marketing.tv) AS total_tv, 
           SUM(marketing.radio) AS total_radio, 
           SUM(marketing.newspaper) AS total_newspaper, 
           SUM(marketing.sales) AS total_sales 
    FROM company 
    INNER JOIN marketing ON company.company_id = marketing.company_id 
    GROUP BY company.company_id, company.name 
    ORDER BY company.company_id ASC
    """

    # Fetch data from the database
    data = fetch_data(query)

    # Find the company data based on the ID
    company_data = None
    for row in data:
        if row['name'].lower() == name:
            company_data = row
            break

    if not company_data:
        return "Company not found", 404

    # Prepare data for the histogram
    labels = ['TV', 'Radio', 'Newspaper']
    values = [
        company_data['total_tv'],
        company_data['total_radio'],
        company_data['total_newspaper']
    ]

    # Create the histogram
    plt.figure(figsize=(8 , 6))
    plt.bar(labels, values, color=['blue', 'green', 'orange'])
    plt.title(f"Marketing Expenses for {company_data['name']}", fontsize=20,pad=15)
    plt.xlabel('Category',fontsize=15,fontweight='bold',labelpad=5)
    plt.ylabel('Amount',fontsize=15,fontweight='bold',labelpad=5)
    plt.xticks(fontsize=15)

    # Save the plot to memory
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    # Pass the plot, company data, and totals to the HTML template
    return render_template(
        "data_visualization.html",
        plot_url=plot_url,
        name=company_data['name'],
        total_tv=company_data['total_tv'],
        total_radio=company_data['total_radio'],
        total_newspaper=company_data['total_newspaper'],
        total_sales=company_data['total_sales']
    )

# Route per gestire l'invio del form
@app.route("/calcola_previsioni", methods=['GET', 'POST'])
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
        return render_template("calcolo_previsioni.html",
                               company=company,
                               tv=tv,
                               radio=radio,
                               newspaper=newspaper,
                               lin_pred=f"{lin_pred[0]:.2f}",
                               poly_pred=f"{poly_pred[0]:.2f}")

    # Se la richiesta è GET, mostra semplicemente il form vuoto
    return render_template("calcolo_previsioni.html")


if __name__ == "__main__":
    app.run(debug=True)
