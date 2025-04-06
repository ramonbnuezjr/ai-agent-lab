import sqlite3

def connect_db():
    conn = sqlite3.connect("data/summaries.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS summaries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            domain TEXT,
            title TEXT,
            summary TEXT,
            tags TEXT,
            raw_json TEXT
        )
    ''')
    conn.commit()
    return conn
