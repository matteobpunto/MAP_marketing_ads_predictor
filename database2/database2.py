import mysql.connector
import csv

# Connect to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conn.cursor()

# Create SQL database
cursor.execute("CREATE DATABASE IF NOT EXISTS marketing_adv")

cursor.execute("USE marketing_adv")

cursor.execute("""
CREATE TABLE IF NOT EXISTS company (
    company_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    office VARCHAR(50),
    n_employees INT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS marketing (
    marketing_id INT PRIMARY KEY AUTO_INCREMENT,
    tv FLOAT,
    radio FLOAT,
    newspaper FLOAT,
    sales FLOAT,
    company_id INT,
    FOREIGN KEY (company_id) REFERENCES company(company_id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS type (
    type_id INT PRIMARY KEY AUTO_INCREMENT,
    spot BOOL,
    inspot BOOL,
    teleshopping BOOL,
    videoclip BOOL,
    trailer BOOL
    );
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS slot (
    slot_id INT PRIMARY KEY AUTO_INCREMENT,
    slot1_start TIME,
    slot1_end TIME,
    slot2_start TIME,
    slot2_end TIME,
    slot3_start TIME,
    slot3_end TIME,
    slot4_start TIME,
    slot4_end TIME,
    slot5_start TIME,
    slot5_end TIME,
    slot6_start TIME,
    slot6_end TIME
    );
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS broadcaster (
    broadcaster_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    network VARCHAR(50)
    );
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS target (
    target_id INT PRIMARY KEY AUTO_INCREMENT,
    age_range VARCHAR(20) NOT NULL
    );
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS marketing_tv (
    tv_id INT PRIMARY KEY,
    marketing_id INT,
    type_id INT,
    slot_id INT,
    broadcaster_id INT,
    target_id INT,
    FOREIGN KEY (type_id) REFERENCES type(type_id),
    FOREIGN KEY (slot_id) REFERENCES slot(slot_id),
    FOREIGN KEY (broadcaster_id) REFERENCES broadcaster(broadcaster_id),
    FOREIGN KEY (target_id) REFERENCES target(target_id),
    FOREIGN KEY (marketing_id) REFERENCES marketing(marketing_id)
);
""")