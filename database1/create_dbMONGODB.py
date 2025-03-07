import pymongo
import csv

# Code for database creation using MongoDB

# ..................................................
# Create MongoDB database and table
# Connecting to MongoDB
myclient = pymongo.MongoClient('mongodb+srv://annaoccoffer:generation123@cluster0.kqbdd.mongodb.net/')
database = myclient["marketing_adv_db"]
collection_name = database["marketing_adv"]

# Open and read the CSV file
with open('file_clear.csv', "r", encoding='utf-8') as f:
    reader = csv.DictReader(f)
    marketing_adv = []  # List to store cleaned data

    for row in reader:
        try:
            # Convert columns to float and clean data
            row['TV'] = float(row['TV']) if row['TV'].strip() else None
            row['radio'] = float(row['radio']) if row['radio'].strip() else None
            row['newspaper'] = float(row['newspaper']) if row['newspaper'].strip() else None
            row['sales'] = float(row['sales']) if row['sales'].strip() else None

            marketing_adv.append(row)  # Add cleaned dictionary to the list
        except ValueError as e:
            print(f"Row skipped due to conversion error: {row}. Error: {e}")

# Insert data into MongoDB
    if marketing_adv:
        collection_name.insert_many(marketing_adv)  # Insert cleaned data in a single operation
        print(f"{len(marketing_adv)} records inserted!")
    else:
        print("No valid data to insert.")

    print(marketing_adv)