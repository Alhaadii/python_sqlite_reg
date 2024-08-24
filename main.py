import mysql.connector

# Establishing a connection to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="expense"
)

# Creating a cursor object to interact with the database
mycursor = mydb.cursor()

# Executing a sample query
mycursor.execute("SELECT * FROM tblexpense")

# Fetching the results
result = mycursor.fetchall()
for row in result:
    print(row)

# Closing the cursor and the connection
mycursor.close()
mydb.close()