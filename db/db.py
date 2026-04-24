import sqlite3
from typing import Optional

#db init
#cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, course TEXT, marks INTEGER, grade TEXT)')

class DatabaseManager:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.connection: Optional[sqlite3.Connection] = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row 
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            if not exc_type:
                self.connection.commit()
            self.connection.close()


