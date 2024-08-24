import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('registration.db')
cursor = conn.cursor()

# Create a table for user registration
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL
                )''')

# Sample user registration function
def register_user(username, email, password):
    cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    conn.commit()
    print("User registered successfully!")

# Sample registration data
username = input("Username: ")
email = input("Email: ")
password =input("Password: ")

# Register a user
register_user(username, email, password)

# Close the connection
conn.close()