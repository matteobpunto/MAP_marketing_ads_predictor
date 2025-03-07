import csv
import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conn.cursor()

# Select the database
cursor.execute("USE marketing_adv")

# Open the CSV file and read its contents
with open('Italian_companies.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    f.readline()  # Skip the header row

    query_list = []
    for row in reader:
        query = f"INSERT INTO company (name, office, n_employees) VALUES ('{row[0]}','{row[1]}', {row[2]})"
        print(query)

        cursor.execute(query)

        query_list.append(query)

# Commit the changes to the database
conn.commit()

print("Data inserted successfully!")
print(query_list)

# Close the connection
cursor.close()
conn.close()
