import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="marketing_adv"
)

cursor = conn.cursor()

# SQL query to insert data into the 'target' table
query = "INSERT INTO target (age_range) VALUES (%s)"
values = [
    ('under 18',),
    ('18 - 25',),
    ('25 - 40',),
    ('40 - 60',),
    ('over 60',)
]


cursor.executemany(query, values)

# Commit the changes to the database
conn.commit()

print("Data entered correctly!")

# Close the cursor and connection
cursor.close()
conn.close()
