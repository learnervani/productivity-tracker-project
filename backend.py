import sqlite3
import csv

# ---------------------- DATABASE CONNECTION ---------------------- #
def connect():
    """Establish connection and create table if not exists."""
    conn = sqlite3.connect("routine.db")
    cur = conn.cursor()
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

connect()  # Ensures the table exists on startup

# ---------------------- DATABASE OPERATIONS ---------------------- #
def insert(date, earning, exercise, study, diet, expense):
    """Insert new record into the database."""
    conn = sqlite3.connect("routine.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL,?,?,?,?,?,?)", 
                (date, earning, exercise, study, diet, expense))
    conn.commit()
    conn.close()

def view():
    """Retrieve all records from the database."""
    conn = sqlite3.connect("routine.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(date="", earning="", exercise="", study="", diet="", expense=""):
    """Search records based on given criteria."""
    conn = sqlite3.connect("routine.db")
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM routine 
        WHERE date=? OR earning=? OR exercise=? OR study=? OR diet=? OR expense=?
    """, (date, earning, exercise, study, diet, expense))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    """Delete a record by ID."""
    conn = sqlite3.connect("routine.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, date, earning, exercise, study, diet, expense):
    """Update an existing record."""
    conn = sqlite3.connect("routine.db")
    cur = conn.cursor()
    cur.execute("""
        UPDATE routine 
        SET date=?, earning=?, exercise=?, study=?, diet=?, expense=? 
        WHERE id=?
    """, (date, earning, exercise, study, diet, expense, id))
    conn.commit()
    conn.close()

# ---------------------- EXPORT FUNCTION ---------------------- #
def export_to_csv(filename="routine_data.csv"):
    """Export all records to a CSV file."""
    conn = sqlite3.connect("routine.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows = cur.fetchall()
    conn.close()

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Date", "Earning", "Exercise", "Study", "Diet", "Expense"])
        writer.writerows(rows)
    print(f"Data exported to {filename} successfully.")

# ---------------------- TESTING ---------------------- #
if __name__ == "__main__":
    # Insert sample data (Uncomment for testing)
    # insert("2025-03-19", 50, "Running", "Python", "Healthy", 20)
    
    print("All Entries:", view())  
    print("Search Example:", search(date="2025-03-19"))
    export_to_csv()  # Generates "routine_data.csv"
