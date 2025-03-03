import csv
import mysql.connector
import random
from mysql.connector import Error

def recupera_dati_lista_int(query):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="marketing_adv"
        )
        cursor = connection.cursor()
        cursor.execute(query)
        result = [elem[0] for elem in cursor.fetchall()]
        return result[0] if result else None
    except Error as e:
        print(f"Errore durante l'esecuzione della query: {e}")
        return None
    finally:
        if connection.is_connected():
            connection.close()

# Connessione al database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="marketing_adv"
)

cursor = conn.cursor()

lista_tipi = ["spot", "inspot", "teleshopping", "videoclip", "trailer"]
colonne = recupera_dati_lista_int("SELECT COUNT(*) FROM marketing")

if colonne is None:
    print("Errore nel recupero dei dati.")
else:
    for _ in range(189):  # Loop per inserire 189 righe
        # Genera valori booleani casuali per ogni colonna
        valori_booleani = [random.choice([True, False]) for _ in lista_tipi]

        # Prepara la query SQL
        query = "INSERT INTO `type` (`spot`, `inspot`, `teleshopping`, `videoclip`, `trailer`) VALUES (%s, %s, %s, %s, %s)"

        # Esegui l'inserimento con i valori casuali
        cursor.execute(query, valori_booleani)
        conn.commit()
        print("Data inserted successfully!")

cursor.close()
conn.close()
