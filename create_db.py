#code for the database creation using SQL from pyhton

import mysql.connector
import pymongo
from pymongo import mongo_client
import csv

# Connessione al server MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conn.cursor()

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

conn.commit()
conn.close()

#code for the database creation using MongoDB

# ..................................................


myclient = pymongo.MongoClient('mongodb+srv://annaoccoffer:generation123@cluster0.kqbdd.mongodb.net/')

database_name = myclient["db_marketing_adv"]
collection_name = database_name["marketing_adv"]

print(f"database name: {database_name.name}")
print(myclient.list_database_names())

with open('Advertising_modified.csv',"r", encoding='utf-8') as f:
    reader = csv.DictReader(f)
    marketing_adv = []
    date = list(reader)

    if date:
        collection_name.insert_many(date)
        print("Dati inseriti con successo!")
    else:
        print("Il file CSV è vuoto, nessun dato inserito.")