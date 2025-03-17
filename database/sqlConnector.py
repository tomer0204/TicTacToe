import mysql.connector

# Connect to the MySQL database – update your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tedy237878!",
    database="users"  # Replace with your actual database name
)

# Create a cursor object to execute SQL queries
cursor = mydb.cursor()

# Create the table "players" with the required columns if it doesn't already exist
create_table_query = """
CREATE TABLE IF NOT EXISTS players (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    player_id INT,
    phone VARCHAR(15),
    email VARCHAR(100),
    score INT,
    game_date DATE,
    game_time TIME
)
"""
cursor.execute(create_table_query)
mydb.commit()

# SQL query for inserting records into the players table
insert_query = """
INSERT INTO players (first_name, last_name, age, player_id, phone, email, score, game_date, game_time)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# List of 20 user records to insert into the table
players_data = [
    ("Yossi", "Cohen", 25, 101, "0501234567", "yossi@example.com", 95, "2025-03-01", "14:30:00"),
    ("Dana", "Levi", 30, 102, "0502345678", "dana@example.com", 85, "2025-03-02", "15:00:00"),
    ("Or", "Mizrahi", 28, 103, "0503456789", "or@example.com", 90, "2025-03-03", "16:00:00"),
    ("Ronit", "Fried", 27, 104, "0504567890", "ronit@example.com", 88, "2025-03-04", "17:00:00"),
    ("Moshe", "Israel", 32, 105, "0505678901", "moshe@example.com", 92, "2025-03-05", "18:00:00"),
    ("Sara", "Cohen", 24, 106, "0506789012", "sara@example.com", 87, "2025-03-06", "19:00:00"),
    ("Yaakov", "Levi", 29, 107, "0507890123", "yaakov@example.com", 93, "2025-03-07", "20:00:00"),
    ("Ella", "Barak", 26, 108, "0508901234", "ella@example.com", 89, "2025-03-08", "21:00:00"),
    ("Avi", "Mizrahi", 31, 109, "0509012345", "avi@example.com", 91, "2025-03-09", "22:00:00"),
    ("Noa", "Cohen", 23, 110, "0510123456", "noa@example.com", 86, "2025-03-10", "13:00:00"),
    ("Dan", "Levi", 30, 111, "0511234567", "dan@example.com", 94, "2025-03-11", "12:00:00"),
    ("Lian", "Mizrahi", 25, 112, "0512345678", "lian@example.com", 88, "2025-03-12", "11:00:00"),
    ("Noa2", "Fried", 27, 113, "0513456789", "noa2@example.com", 90, "2025-03-13", "10:00:00"),
    ("Gadi", "Israel", 28, 114, "0514567890", "gadi@example.com", 85, "2025-03-14", "09:00:00"),
    ("Dana2", "Cohen", 26, 115, "0515678901", "dana2@example.com", 92, "2025-03-15", "08:00:00"),
    ("Ran", "Levi", 32, 116, "0516789012", "ran@example.com", 87, "2025-03-16", "07:00:00"),
    ("Noa3", "Barak", 24, 117, "0517890123", "noa3@example.com", 93, "2025-03-17", "06:00:00"),
    ("Or2", "Mizrahi", 29, 118, "0518901234", "or2@example.com", 89, "2025-03-18", "05:00:00"),
    ("Rut", "Fried", 31, 119, "0519012345", "rut@example.com", 91, "2025-03-19", "04:00:00"),
    ("Yoval", "Israel", 27, 120, "0520123456", "yoval@example.com", 90, "2025-03-20", "03:00:00")
]

# Execute the insert query for all 20 records
cursor.executemany(insert_query, players_data)
mydb.commit()

print("The table has been successfully updated with 20 users!")
