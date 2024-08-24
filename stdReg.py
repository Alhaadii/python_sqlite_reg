import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create a table for student registration
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    grade TEXT NOT NULL
                )''')

# Function to register a student
def register_student():
    name = entry_name.get()
    age = entry_age.get()
    grade = entry_grade.get()

    if name and age and grade:
        cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
        conn.commit()
        messagebox.showinfo("Success", "Student registered successfully!")
        data = cursor.execute("SELECT * FROM students")
        for row in data:
            print(row)
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

# Create the Tkinter GUI
root = tk.Tk()
root.title("Student Registration")

label_name = tk.Label(root, text="Name:")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

label_age = tk.Label(root, text="Age:")
label_age.pack()
entry_age = tk.Entry(root)
entry_age.pack()

label_grade = tk.Label(root, text="Grade:")
label_grade.pack()
entry_grade = tk.Entry(root)
entry_grade.pack()

button_register = tk.Button(root, text="Register", command=register_student)
button_register.pack()

root.mainloop()

# Close the connection
conn.close()