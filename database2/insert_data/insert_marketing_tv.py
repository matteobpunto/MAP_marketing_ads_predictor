# Importing the libraries we'll use

import mysql.connector
import random
from marketing_ads_predictor.database2.insert_type import recover_list_data_int

# Connecting to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

# Creating a cursor to navigate our database
cursor = conn.cursor()

# Selecting the right database
cursor.execute("USE marketing_adv")

# Using MySQL syntax to insert marketing values

insertInto = ("INSERT INTO `marketing_tv`(`marketing_id`, `type_id`, `slot_id`, `broadcaster_id`, `target_id`)"
              " VALUES ('[value-2]','[value-3]','[value-4]','[value-5]','[value-6]')")

# Retrieve all marketing IDs from the marketing table and order them by ID
cursor.execute("SELECT marketing_id FROM marketing ORDER BY `marketing`.`marketing_id` ASC")
listMarketing_id = cursor.fetchall()
print(type(listMarketing_id))
print(listMarketing_id)

# Creating dictionaries for age groups and their percentage weights
age_groups = {
    1: "under 18",
    2: "18 - 25",
    3: "25 - 40",
    4: "40 - 60",
    5: "over 60"
}

percentages = {
    1: 30,  # 30% under 18
    2: 5,   # 5% 18-25
    3: 15,  # 15% 25-40
    4: 20,  # 20% 40-60
    5: 30   # 30% over 60
}

# Counting all data from marketing and converting them into percentages
num_samples = 189
weights = [percentages[key] / 100 for key in age_groups]

# Creating a random list using the random function to determine percentages
random_list = random.choices(list(age_groups.keys()), weights=weights, k=num_samples)

print(random_list)
print(len(random_list))

# Creating dictionaries for time slots
time_slots = {
    "18 - 25": ["00:00 - 04:00"],
    "25 - 40": ["04:00 - 08:00"],
    "over 60": ["08:00 - 12:00"],
    "under 18": ["12:00 - 16:00", "16:00 - 20:00"],
    "40 - 60": ["20:00 - 00:00"]
}

slot_dict = {
    "00:00 - 04:00": 1,
    "04:00 - 08:00": 2,
    "08:00 - 12:00": 3,
    "12:00 - 16:00": 4,
    "16:00 - 20:00": 5,
    "20:00 - 00:00": 6
}

valuesInsertInto = ""
row_count = 0
for i, num in enumerate(random_list):
    # ID taken from marketing
    marketingID = i + 1
    # ID from the type table
    typeID = i + 1

    # ID from the target table, taken from the weighted percentage list
    targetID = num
    print(marketingID)
    print(num)
    targetInStr = age_groups.get(targetID)
    slot = time_slots.get(targetInStr)
    slotCorrect = random.choice(slot)
    slotID = slot_dict.get(slotCorrect)
    broadcasterID = random.randint(1, 10)

    valuesInsertInto = f"{marketingID}, {typeID}, {slotID}, {broadcasterID}, {targetID}"

    query = f"""INSERT INTO `marketing_tv`(`marketing_id`, `type_id`, `slot_id`, `broadcaster_id`, `target_id`)
               VALUES ({valuesInsertInto})"""

    cursor.execute(query)
    row_count += 1

# Commit the changes
conn.commit()

print(f"{row_count} rows inserted successfully!")

# Close the connection
cursor.close()
conn.close()
