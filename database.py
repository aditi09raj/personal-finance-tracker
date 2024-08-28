import sqlite3

DB_FILE = "tracker.db"

def connect():
    conn = sqlite3.connect(DB_FILE)
    return conn

def setup():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            type TEXT NOT NULL CHECK (type IN ('Income', 'Expense')),
            category TEXT NOT NULL,
            amount REAL NOT NULL CHECK (amount > 0),
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_entry(date, trans_type, category, amount, description):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transactions (date, type, category, amount, description)
        VALUES (?, ?, ?, ?, ?)
    ''', (date, trans_type, category, amount, description))
    conn.commit()
    conn.close()

def view_all():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions ORDER BY id ASC')
    records = cursor.fetchall()
    conn.close()
    return records

def delete_entry(entry_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM transactions WHERE id = ?', (entry_id,))
    conn.commit()
    conn.close()

def check_balance():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT 
            SUM(CASE WHEN type = 'Income' THEN amount ELSE 0 END) -
            SUM(CASE WHEN type = 'Expense' THEN amount ELSE 0 END)
        AS balance FROM transactions
    ''')
    balance = cursor.fetchone()[0]
    conn.close()
    return balance if balance else 0.0
