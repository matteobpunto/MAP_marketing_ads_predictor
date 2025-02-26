import pymongo
import csv
#code for the database creation using MongoDB

# ..................................................
# create db MongoDB and create table
# Connessione a MongoDB
myclient = pymongo.MongoClient('mongodb+srv://annaoccoffer:generation123@cluster0.kqbdd.mongodb.net/')
database = myclient["marketing_adv_db"]
collection_name = database["marketing_adv"]

# Aprire e leggere il file CSV
with open('Advertising_modified.csv', "r", encoding='utf-8') as f:
    reader = csv.DictReader(f)
    marketing_adv = []  # Lista per contenere i dati puliti

    for row in reader:
        try:
            # Convertire le colonne in float e pulire i dati
            row['TV'] = float(row['TV']) if row['TV'].strip() else None
            row['radio'] = float(row['radio']) if row['radio'].strip() else None
            row['newspaper'] = float(row['newspaper']) if row['newspaper'].strip() else None
            row['sales'] = float(row['sales']) if row['sales'].strip() else None

            marketing_adv.append(row)  # Aggiungere il dizionario pulito alla lista
        except ValueError as e:
            print(f"Riga ignorata a causa di errore di conversione: {row}. Errore: {e}")

# Inserire i dati in MongoDB
    if marketing_adv:
        collection_name.insert_many(marketing_adv)  # Inserire i dati puliti in un'unica operazione
        print(f"{len(marketing_adv)} dati inseriti!")
    else:
        print("Nessun dato valido da inserire.")

    print(marketing_adv)