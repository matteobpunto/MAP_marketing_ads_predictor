#code for the database creation using SQL from pyhton

import mysql.connector

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

import pymongo

myclient = pymongo.MongoClient('mongodb+srv://annaoccoffer:generation123@cluster0.kqbdd.mongodb.net/')

database_name = "db_marketing_adv"
collection_name = "marketing_adv"



