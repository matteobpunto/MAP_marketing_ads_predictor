#code for the database creation using SQL from pyhton

import mysql.connector
import csv

#Connessione al server MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conn.cursor()

# create db SQL
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
# #...........................................
#create table on SQL
with open('Advertising_modified.csv', "r", encoding='utf-8') as f:
    reader = csv.DictReader(f)
    lista_marketing = []  # Lista per contenere i dati puliti

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database = "db_marketing_adv"
    )

    cursor = conn.cursor()

    for row in reader:
        try:
            # Convertire le colonne in float e pulire i dati
            row['TV'] = float(row['TV']) if row['TV'].strip() else None
            row['radio'] = float(row['radio']) if row['radio'].strip() else None
            row['newspaper'] = float(row['newspaper']) if row['newspaper'].strip() else None
            row['sales'] = float(row['sales']) if row['sales'].strip() else None

            lista_marketing.append(row)  # Aggiungere il dizionario pulito alla lista
            cursor.execute(f"""INSERT INTO `marketing_adv`(`tv`, `radio`, `newspaper`, `sales`) VALUES
                ('{row['TV']}','{row['radio']}','{row['newspaper']}','{row['sales']}')""")

        except ValueError as e:
            print(f"Riga ignorata a causa di errore di conversione: {row}. Errore: {e}")
    print("Dati inseriti con successo")

conn.commit()
conn.close()

