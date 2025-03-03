import csv
import mysql.connector
import random
from mysql.connector import Error

def recupera_dati_lista_int(query):
    try:
        # Creazione connessione
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="marketing_adv"
        )
        if connection.is_connected():
            cursor = connection.cursor()  # Restituisce risultati come dizionari

            # Eseguiamo la query
            cursor.execute(query)

            # Recupero dei dati
            result = [elem[0] for elem in cursor.fetchall()]

            cursor.close()
            return result
    except Error as e:
        print(f"Errore durante l'esecuzione della query: {e}")
        return None
    finally:
        if connection.is_connected():
            connection.close()

# Connect to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conn.cursor()

cursor.execute("USE marketing_adv")

lista_bool = [True, False]
lista_tipi = ["spot", "inspot", "teleshopping", "videoclip", "trailer"]

tipo_scelto = random.choice(lista_tipi)
indice = lista_tipi.index(tipo_scelto)

colonne = recupera_dati_lista_int("SELECT COUNT(*) FROM marketing")

for _ in range(189):
    stringa = ''

    for x in range(len(lista_tipi)):
        if x == indice:
            stringa += 'TRUE'
        else:
            stringa += 'FALSE'

        if x != len(lista_tipi) - 1:
            stringa += ', '

    query = (f"INSERT INTO type(`spot`, `inspot`, `teleshopping`, `videoclip`, `trailer`)"
             f" VALUES ({stringa})")

    cursor.execute(query)
    conn.commit()

    print("Data inserted successfully!")


cursor.close()
conn.close()