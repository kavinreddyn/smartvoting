import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ---------- DATABASE ----------
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    usn TEXT UNIQUE NOT NULL,
    marks INTEGER
)
""")
conn.commit()

# ---------- FUNCTIONS ----------

def add_student():
    name = name_var.get()
    usn = usn_var.get()
    marks = marks_var.get()

    if name == "" or usn == "" or marks == "":
        messagebox.showwarning("Input Error", "All fields required")
        return

    try:
        cursor.execute(
            "INSERT INTO students (name, usn, marks) VALUES (?, ?, ?)",
            (name, usn, int(marks))
        )
        conn.commit()
        messagebox.showinfo("Success", "Student Added Successfully")
        clear_fields()
        view_students()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "USN already exists")


def view_students():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)


def update_student():
    name = name_var.get()
    usn = usn_var.get()
    marks = marks_var.get()

    if name == "" or usn == "" or marks == "":
        messagebox.showwarning("Input Error", "Select a student first")
        return

    cursor.execute(
        "UPDATE students SET name=?, marks=? WHERE usn=?",
        (name, int(marks), usn)
    )
    conn.commit()

    if cursor.rowcount == 0:
        messagebox.showerror("Error", "USN not found")
    else:
        messagebox.showinfo("Success", "Updated Successfully")
        view_students()


def delete_student():
    usn = usn_var.get()

    if usn == "":
        messagebox.showwarning("Input Error", "Select a student first")
        return

    cursor.execute("DELETE FROM students WHERE usn=?", (usn,))
    conn.commit()

    if cursor.rowcount == 0:
        messagebox.showerror("Error", "USN not found")
    else:
        messagebox.showinfo("Success", "Deleted Successfully")
        clear_fields()
        view_students()


def clear_fields():
    name_var.set("")
    usn_var.set("")
    marks_var.set("")


def select_record(event):
    selected = tree.focus()
    if selected:
        values = tree.item(selected, "values")

        name_var.set(values[1])
        usn_var.set(values[2])
        marks_var.set(values[3])


# ---------- GUI WINDOW ----------
root = tk.Tk()
root.title("Student Management System")
root.geometry("700x500")
root.resizable(False, False)

# ---------- VARIABLES ----------
name_var = tk.StringVar()
usn_var = tk.StringVar()
marks_var = tk.StringVar()

# ---------- LABELS & ENTRIES ----------
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=name_var).grid(row=0, column=1)

tk.Label(root, text="USN").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=usn_var).grid(row=1, column=1)

tk.Label(root, text="Marks").grid(row=2, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=marks_var).grid(row=2, column=1)

# ---------- BUTTONS ----------
tk.Button(root, text="Add", width=12, command=add_student).grid(row=0, column=3)
tk.Button(root, text="Update", width=12, command=update_student).grid(row=1, column=3)
tk.Button(root, text="Delete", width=12, command=delete_student).grid(row=2, column=3)
tk.Button(root, text="Clear", width=12, command=clear_fields).grid(row=3, column=3, pady=10)

# ---------- TABLE ----------
columns = ("ID", "Name", "USN", "Marks")

tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.grid(row=5, column=0, columnspan=4, padx=10, pady=20)

# Scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(row=5, column=4, sticky="ns")

# Bind select
tree.bind("<ButtonRelease-1>", select_record)

view_students()

root.mainloop()

conn.close()
