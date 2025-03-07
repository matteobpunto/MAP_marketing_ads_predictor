from flask import Flask, render_template, request
import mysql
import mysql.connector
import csv
from mysql.connector import Error
from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64

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


@app.route("/")
def landing_page():

    return render_template("index.html")


@app.route("/company/<int:id>")
@app.route("/company/<int:id>")
def index(id):
    query = """
    SELECT company.company_id, company.name, company.office, 
           SUM(marketing.tv) AS total_tv, 
           SUM(marketing.radio) AS total_radio, 
           SUM(marketing.newspaper) AS total_newspaper, 
           SUM(marketing.sales) AS total_sales 
    FROM company 
    INNER JOIN marketing ON company.company_id = marketing.company_id 
    GROUP BY company.company_id, company.name, company.office 
    ORDER BY company.company_id ASC
    """

    # Fetch data from the database
    data = fetch_data(query)

    # Find the company data based on the ID
    company_data = None
    for row in data:
        if row['company_id'] == id:
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
    plt.figure(figsize=(8, 4))
    plt.bar(labels, values, color=['blue', 'green', 'orange'])
    plt.title(f"Marketing Expenses for {company_data['name']}")
    plt.xlabel('Category')
    plt.ylabel('Amount')

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
        office=company_data['office'],
        total_tv=company_data['total_tv'],
        total_radio=company_data['total_radio'],
        total_newspaper=company_data['total_newspaper'],
        total_sales=company_data['total_sales']
    )
if __name__ == "__main__":
    app.run(debug=True)
