import sqlite3

conn = sqlite3.connect("chat.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    username TEXT PRIMARY KEY,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS messages(
    username TEXT,
    message TEXT
)
""")

conn.commit()

def register_user(username, password):
    cursor.execute("INSERT INTO users VALUES (?,?)", (username, password))
    conn.commit()

def login_user(username, password):
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                   (username, password))
    return cursor.fetchone()

def save_message(username, message):
    cursor.execute("INSERT INTO messages VALUES (?,?)", (username, message))
    conn.commit()

def load_messages():
    cursor.execute("SELECT * FROM messages")
    return cursor.fetchall()
