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


cursor.execute("""
    SELECT m.marketing_id, t.type_id, s.slot_id, b.broadcaster_id, tg.target_id
    FROM marketing AS m
    JOIN type AS t ON m.type_id = t.type_id
    JOIN slot AS s ON m.slot_id = s.slot_id
    JOIN broadcaster AS b ON m.broadcaster_id = b.broadcaster_id
    JOIN target AS tg ON m.target_id = tg.target_id
""")
dati = cursor.fetchall()

lista_prova = []

for riga in dati:
    id_marketing, id_type, id_slot, id_broadcaster, id_target = riga

    cursor.execute("SELECT id FROM marketing WHERE marketing_id = %s", (id_marketing,))
    marketing_id = cursor.fetchone()

    cursor.execute("SELECT id FROM type WHERE type_id = %s", (id_type,))
    type_id = cursor.fetchone()

    cursor.execute("SELECT id FROM slot WHERE slot_id = %s", (id_slot,))
    slot_id = cursor.fetchone()

    cursor.execute("SELECT id FROM broadcaster WHERE broadcaster_id = %s", (id_broadcaster,))
    broadcaster_id = cursor.fetchone()

    cursor.execute("SELECT id FROM target WHERE target_id = %s", (id_target,))
    target_id = cursor.fetchone()

    # Verifica che tutti gli ID siano stati trovati
    if None in (marketing_id, type_id, slot_id, broadcaster_id, target_id):
        print(f"Errore: {riga}")
        continue

    # Creare la query di inserimento
    query = "INSERT INTO marketing_tv (marketing_id, type_id, slot_id, broadcaster_id, target_id) VALUES (%s, %s, %s, %s, %s)"
    values = (marketing_id[0], type_id[0], slot_id[0], broadcaster_id[0], target_id[0])

    cursor.execute(query, values)
    lista_prova.append(values)

conn.commit()

print("Data inserted successfully!")
print(lista_prova)

cursor.close()
conn.close()
