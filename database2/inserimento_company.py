import csv
import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conn.cursor()

cursor.execute("USE marketing_adv")


with open('Aziende_Italiane.csv', encoding='utf-8') as f:
    lettore = csv.reader(f, delimiter=',')
    f.readline()

    lista_prova = []
    for riga in lettore:

        query = f"INSERT INTO company (name, office, n_employees) VALUES ('{riga[0]}','{riga[1]}', {riga[2]})"
        print(query)

        cursor.execute(query)

        lista_prova.append(query)


conn.commit()

print("Data inserted successfully!")
print(lista_prova)

cursor.close()
conn.close()