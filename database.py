import sqlite3

class Database:

    def store_clip(self, datetime, text):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        query = "CREATE TABLE IF NOT EXISTS clipboard (datetime TEXT, text TEXT);"
        cursor.execute(query)

        query = "INSERT INTO clipboard (datetime, text) VALUES (?, ?);"
        cursor.execute(query, (datetime, text))
        conn.commit()
        conn.close()

    def get_clips(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        query = "SELECT * FROM clipboard;"
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return rows

    def delete_clip(self, text):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        query = "DELETE FROM clipboard WHERE text=?"
        cursor.execute(query, (text,))
        conn.commit()
        conn.close()

    def clear_clips(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        query = "DELETE FROM clipboard;"
        cursor.execute(query)
        conn.commit()
        conn.close()