import sqlite3

class Database:
    def store_clip(self, datetime, text):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        query = f"INSERT INTO clipboard VALUES ('{datetime}', '{text}');"
        cursor.execute(query)

    def create_table(self):
        conn = sqlite3.connect('database.db')
        query = "CREATE TABLE IF NOT EXISTS clipboard (datetime TEXT, text TEXT);"
        conn.execute(query)

db = Database()
db.create_table()
db.store_clip("08-05-20", "alksjdfkajdlfhk")