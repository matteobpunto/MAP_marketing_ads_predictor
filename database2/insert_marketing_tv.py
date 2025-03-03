import mysql.connector

# Connessione al database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="marketing_adv"
)

cursor = conn.cursor()

# Estrazione dei dati validi
cursor.execute("""
    SELECT m.marketing_id, t.type_id, s.slot_id, b.broadcaster_id, tg.target_id
    FROM marketing_tv AS m
    JOIN type AS t ON m.type_id = t.type_id
    JOIN slot AS s ON m.slot_id = s.slot_id
    JOIN broadcaster AS b ON m.broadcaster_id = b.broadcaster_id
    JOIN target AS tg ON m.target_id = tg.target_id
""")

dati = cursor.fetchall()
lista_prova = []

for riga in dati:
    id_marketing, id_type, id_slot, id_broadcaster, id_target = riga

    print(f"Verificando: {id_marketing}, {id_type}, {id_slot}, {id_broadcaster}, {id_target}")

    # Verifica se la riga è già presente in marketing_tv
    cursor.execute("""
        SELECT 1 FROM marketing_tv
        WHERE marketing_id = %s AND type_id = %s AND slot_id = %s 
        AND broadcaster_id = %s AND target_id = %s
    """, (id_marketing, id_type, id_slot, id_broadcaster, id_target))

    if cursor.fetchone():
        print(f"Record già presente: {riga}")
        continue

    # Inserimento nel database
    query = """
        INSERT INTO marketing_tv (marketing_id, type_id, slot_id, broadcaster_id, target_id) 
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (id_marketing, id_type, id_slot, id_broadcaster, id_target)

    cursor.execute(query, values)
    lista_prova.append(values)

conn.commit()

print("Data inserted successfully!")
print(f"{lista_prova = }")

cursor.close()
conn.close()
