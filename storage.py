import sqlite3
import os
database = os.path.join(
    os.path.expanduser("~"),
    "Desktop",
    "expenses",
    "expenses.db"
)

def start_db():
    connect = sqlite3.connect(database)
    cursor = connect.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS expenses 
                   (
                   id INTEGER PRIMARY KEY,
                   date TEXT,
                   category TEXT,
                   amount REAL,
                   note TEXT
                   )
                   """)
    connect.commit()
    connect.close()

def save_expense(expense):
    connect = sqlite3.connect(database)
    cursor = connect.cursor()

    cursor.execute("""
                   INSERT INTO expenses (id,date,category,amount,note)
                   VALUES (?,?,?,?,?)
                   """, 
                   (
                       expense["id"],
                       expense["date"],
                       expense["category"],
                       expense["amount"],
                       expense["note"],
                   )
                  )
    connect.commit()
    connect.close()

def load_expenses():
    connect = sqlite3.connect(database)
    cursor = connect.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    expenses = []
    for r in rows:
        expenses.append({
            "id":r[0],
            "date":r[1],
            "category":r[2],
            "amount":r[3],
            "note":r[4]
        })

    next_id = max([e["id"] for e in expenses], default=0)+1

    connect.close()
    return expenses, next_id