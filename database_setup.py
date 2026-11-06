import sqlite3
import os

DB_FILE = 'election.db'

def setup_database():
    """Create the necessary database tables if they do not exist."""
    print(f"Setting up database: {DB_FILE}")
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Table for voters
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS voters (
            aadhaar TEXT PRIMARY KEY,
            voter_id TEXT UNIQUE,
            has_voted INTEGER DEFAULT 0
        )
    ''')
    
    # Table for votes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS votes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aadhaar TEXT,
            party TEXT
        )
    ''')

    conn.commit()
    conn.close()
    print("Database setup complete.")

if __name__ == "__main__":
    setup_database()
