# Code for the database creation using SQL from Python
import mysql.connector
import csv

# Connect to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conn.cursor()

# Create SQL database
cursor.execute("CREATE DATABASE IF NOT EXISTS db_marketing_adv")

cursor.execute("USE db_marketing_adv")

cursor.execute("""
CREATE TABLE IF NOT EXISTS marketing_adv (
    tv FLOAT,
    radio FLOAT,
    newspaper FLOAT,
    sales FLOAT
)
""")

# ...........................................
# Create table in SQL and insert data
with open('../file_clear.csv', "r", encoding='utf-8') as f:
    reader = csv.DictReader(f)
    marketing_list = []  # List to store cleaned data

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_marketing_adv"
    )

    cursor = conn.cursor()

    for row in reader:
        try:
            # Convert columns to float and clean data
            row['TV'] = float(row['TV']) if row['TV'].strip() else None
            row['radio'] = float(row['radio']) if row['radio'].strip() else None
            row['newspaper'] = float(row['newspaper']) if row['newspaper'].strip() else None
            row['sales'] = float(row['sales']) if row['sales'].strip() else None

            marketing_list.append(row)  # Add cleaned dictionary to the list
            cursor.execute(f"""INSERT INTO `marketing_adv`(`tv`, `radio`, `newspaper`, `sales`) VALUES
                ('{row['TV']}', '{row['radio']}', '{row['newspaper']}', '{row['sales']}')""")

        except ValueError as e:
            print(f"Row skipped due to conversion error: {row}. Error: {e}")

    print("Data successfully inserted")

conn.commit()
conn.close()
