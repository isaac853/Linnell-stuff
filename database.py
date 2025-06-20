import sqlite3

db_name = "minibus_booking.db"

#connect to sqlite database and create the database if it doesn't exist

conn = sqlite3.connect(db_name)

#control structure via a cursor

cursor = conn.cursor()

#create the database and it's fields - field name data type ad rules of the column / field

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT UNIQUE
        
                ); 

""")

#create mini_buses table

cursor.execute("""
    CREATE TABLE IF NOT EXISTS mini_buses(
        bus_id INTEGER PRIMARY KEY AUTOINCREMENT,
        plate_number TEXT UNIQUE NOT NULL,
        capacity INTEGER NOT NULL
                );

""")

#create bookings table

cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS bookings (
        booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        bus_id INTEGER NOT NULL,
        booking_date TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
        FOREIGN KEY (bus_id) REFERENCES mini_buses (bus_id)
               
               );

""")

conn.commit()
conn.close() # commits changes and closes the database

# open database to insert data into it

conn = sqlite3.connect(db_name)
cursor = conn.cursor()

#creates a tuple inside a list
users = [
    ("Alice Smith", "alice@example.com","079621231234"),
    ("Bob Jones","bob@example.com","078457582344"),
    ("Charlie Lee", "charlie@bobmail.com","075959595404")

]

buses = [
    ("VU27QYT", 12),
    ("HU21ABC", 15),
    ("KV23OPW", 10)
]

bookings = [
    (1, 1, "25-03-25"),
    (2, 2, "27-24-25"),
    (3, 1, "23-01-25")
]

#insert the data from the lists into the data structure

cursor.executemany("INSERT INTO users (name, email, phone) VALUES (?,?,?)", users)
cursor.executemany("INSERT INTO mini_buses (plate_number, capacity) VALUES (?,?)", buses)
cursor.executemany("INSERT INTO bookings (user_id, bus_id, booking_date) VALUES (?,?,?)", bookings)

conn.commit()
conn.close()