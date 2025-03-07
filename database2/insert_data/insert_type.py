import csv
import mysql.connector
import random
from mysql.connector import Error

def recover_list_data_int(query):
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
        print(f"Error while executing the query: {e}")
        return None
    finally:
        if connection.is_connected():
            connection.close()

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="marketing_adv"
)

cursor = conn.cursor()

type_list = ["spot", "inspot", "teleshopping", "videoclip", "trailer"]
columns = recover_list_data_int("SELECT COUNT(*) FROM marketing")

if columns is None:
    print("Error retrieving data.")
else:
    for _ in range(189):  # Loop to insert 189 rows
        # Generate random boolean values for each column
        boolean_values = [random.choice([True, False]) for _ in type_list]

        # Prepare the SQL query
        query = "INSERT INTO `type` (`spot`, `inspot`, `teleshopping`, `videoclip`, `trailer`) VALUES (%s, %s, %s, %s, %s)"

        # Execute the insertion with random values
        cursor.execute(query, boolean_values)
        conn.commit()
        print("Data inserted successfully!")

cursor.close()
conn.close()
