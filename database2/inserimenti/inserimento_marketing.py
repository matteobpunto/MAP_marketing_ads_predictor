import csv
import mysql.connector
import random

# Connect to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="marketing_adv"  # Set the database directly in the connection
)

cursor = conn.cursor()

# Get all available company_id values from the company table
cursor.execute("SELECT company_id FROM company")
company_ids = cursor.fetchall()
for row in company_ids:
    company_id = row[0]


# Open the CSV file
with open('Advertising_clear.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    f.readline()

    query = """
    INSERT INTO marketing (tv, radio, newspaper, sales, company_id) 
    VALUES (%s, %s, %s, %s, %s)
    """
    contgiri = 0
    data_to_insert = []
    for row in reader:
        tv = float(row[0])
        radio = float(row[1])
        newspaper = float(row[2])
        sales = float(row[3])
        company_id = random.choice(company_ids)[0]

        data_to_insert.append((tv, radio, newspaper, sales, company_id))
        contgiri +=1

    cursor.executemany(query, data_to_insert)
    conn.commit()
print(f"Marketing data inserted successfully! inserite righe {contgiri}")

# Close the cursor and connection
cursor.close()
conn.close()
