import mysql.connector
from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Database connection configuration
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="marketing_adv"
    )

# Function to retrieve data from the database
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

# Query to fetch data


# Route to display the histogram for a specific company
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
    plt.bar(labels, values, color=['blue', 'green', 'orange', 'red'])
    plt.title(f"Marketing Expenses and Sales for {company_data['name']}")
    plt.xlabel('Category')
    plt.ylabel('Amount')

    # Save the plot to memory
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    # Pass the plot, company data, and TV sum to the HTML template
    return render_template(
        "index.html",
        plot_url=plot_url,
        name=company_data['name'],
        office=company_data['office'],
        total_tv=company_data['total_tv']  # Pass the sum of TV values
    )

if __name__ == "__main__":
    app.run(debug=True)