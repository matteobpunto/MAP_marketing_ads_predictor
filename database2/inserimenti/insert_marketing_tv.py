# importing the libraries we'll use

import mysql.connector
import random


# connecting to the mySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

# creating a cursor to navigate our database
cursor = conn.cursor()

# selecting the right database
cursor.execute("USE marketing_adv")

# using the mySQL language for the insert of marketing values

insertInto = ("INSERT INTO `marketing_tv`(`marketing_id`, `type_id`, `slot_id`, `broadcaster_id`, `target_id`)"
              " VALUES ('[value-2]','[value-3]','[value-4]','[value-5]','[value-6]')")

# take all the marketing ids from marketing and order them by their id
cursor.execute("SELECT marketing_id FROM marketing ORDER BY `marketing`.`marketing_id` ASC")
listaMarketing_id = cursor.fetchall()
print(type(listaMarketing_id))
print(listaMarketing_id)

# creating dictionaries for age groups and percentages of their weight
age_groups = {
    1: "under 18",
    2: "18 - 25",
    3: "25 - 40",
    4: "40 - 60",
    5: "over 60"
}

percentages = {
    1: 30,  # 10% under 18
    2: 5,  # 20% 18-25
    3: 15,  # 25% 25-40
    4: 20,  # 15% 40-60
    5: 30  # 30% over 60
}

# counting all data from marketing and converting them into percentages
num_samples = 189
weights = [percentages[key] / 100 for key in age_groups]

# creating a random list using random function to determine the percentages
random_list = random.choices(list(age_groups.keys()), weights=weights, k=num_samples)

print(random_list)
print(len(random_list))

# creating dictionaries for time slot and a dictionary
time_slots = {
    "18 - 25": ["00:00 - 04:00"],
    "25 - 40": ["04:00 - 08:00"],
    "over 60": ["08:00 - 12:00"],
    "under 18": ["12:00 - 16:00", "16:00 - 20:00"],
    "40 - 60": ["20:00 - 00:00"]
}

dizSlot = {
    "00:00 - 04:00": 1,
    "04:00 - 08:00": 2,
    "08:00 - 12:00": 3,
    "12:00 - 16:00": 4,
    "16:00 - 20:00": 5,
    "20:00 - 00:00": 6
}

valoriInsertInto = ""
row_count = 0
for i, num in enumerate(random_list):
    # id preso da marketing
    marketingID = i + 1
    # id tabella type
    typeID = i + 1

    # id tabella target preso dalla lista creata con i pesi delle percentuali
    targetID = num
    print(marketingID)
    print(num)
    targetinstringa = age_groups.get(targetID)
    slot = time_slots.get(targetinstringa)
    slotgiusto = random.choice(slot)
    slotID = dizSlot.get(slotgiusto)
    broadcasterID = random.randint(1, 10)

    valoriInsertInto = f"{marketingID}, {typeID}, {slotID}, {broadcasterID}, {targetID}"

    query = f"""INSERT INTO `marketing_tv`(`marketing_id`, `type_id`, `slot_id`, `broadcaster_id`, `target_id`)
               VALUES ({valoriInsertInto})"""

    cursor.execute(query)
    row_count += 1

# Commit delle modifiche
conn.commit()

print(f"{row_count} righe inserite con successo!")

# Chiudi la connessione
cursor.close()
conn.close()