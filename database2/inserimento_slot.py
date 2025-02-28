import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="marketing_adv"
)

cursor = conn.cursor()

# Define time slots
time_slots = [
    ('00:00', '04:00', '04:00', '08:00', '08:00', '12:00', '12:00', '16:00', '16:00', '20:00', '20:00', '00:00')
]

# SQL query to insert data
query = """
INSERT INTO slot (slot1_start, slot1_end, slot2_start, slot2_end, 
                  slot3_start, slot3_end, slot4_start, slot4_end, 
                  slot5_start, slot5_end, slot6_start, slot6_end) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Execute the query
cursor.executemany(query, time_slots)

# Commit the transaction
conn.commit()

print("Time slots inserted successfully!")

# Close the cursor and connection
cursor.close()
conn.close()
