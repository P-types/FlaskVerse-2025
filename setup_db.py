import sqlite3

# Create / Connect to database
conn = sqlite3.connect("students.db")

cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    marks INTEGER NOT NULL
)
""")

conn.commit()
conn.close()

print("Database and table created successfully.")