import sqlite3
import pandas as pd

# -----------------------------
# SAMPLE DATA
# -----------------------------
data = {
    "product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone"],
    "city": ["Chennai", "Mumbai", "Delhi", "Chennai", "Delhi"],
    "sales": [50000, 30000, 20000, 45000, 25000],
    "month": ["Jan", "Jan", "Jan", "Feb", "Feb"]
}

df = pd.DataFrame(data)

# -----------------------------
# CREATE DATABASE
# -----------------------------
conn = sqlite3.connect("database.db")

df.to_sql("sales", conn, if_exists="replace", index=False)

conn.close()

print("✅ Database created successfully")