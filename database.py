import sqlite3

class Database:
    def store_clip(self, date, time, text):
        pass


    def create_table(self):
        conn = sqlite3.connect('database.db')
        query = "CREATE TABLE clipboard (datetime VARCHAR(25), text VARCHAR(255))"
        conn.execute(query)

Database().create_table()