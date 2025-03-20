import sqlite3


def connect():
    conn = sqlite3.connect("routine.db")
    cur = conn.cursor()
    # Create the 'routine' table if it doesn't exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS routine (
            id INTEGER PRIMARY KEY,
            date TEXT,
            earning REAL,
            exercise TEXT,
            study TEXT,
            diet TEXT,
            expense REAL
        )
    """)
    conn.commit()
    conn.close()

# Call the connect function to ensure the table is created
connect()

def insert(date, earning, exercise, study, diet, expense):
    conn = sqlite3.connect("routine.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL,?,?,?,?,?,?)", (date, earning, exercise, study, diet, expense))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("routine.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows  # Return rows instead of printing them

def delete(id):
    conn = sqlite3.connect("routine.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=?", (id,))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    

def search(date="", earning="", exercise="", study="", diet="", expense=""):
    conn = sqlite3.connect("routine.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=? OR earning=? OR exercise=? OR study=? OR diet=? OR expense=?", (date, earning, exercise, study, diet, expense))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return(rows) 



# insert("1/1/2020", 10000, "done", "done", "yes", 30)
# insert("11/1/2020", 40000, "done", "done", "yes", 40)
# insert("12/1/2020", 50000, "done", "done", "yes", 50)
# insert("15/1/2020", 80000, "done", "done", "yes", 60)

