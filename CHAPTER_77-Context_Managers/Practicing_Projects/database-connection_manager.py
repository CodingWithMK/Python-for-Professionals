import sqlite3

class DatabaseConnectionManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()
        if exc_type is not None:
            print(f"An error occured: {exc_value}")
            return False
        return True

# Example usage
if __name__ == "__main__":
    with DatabaseConnectionManager("CHAPTER_77-Context_Managers/Practicing_Projects/example.db") as connect:
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
        cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
        cursor.execute("INSERT INTO users (name) VALUES ('Bob')")
        connect.commit()

        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()

# This code defines a context manager for managing database connections using SQLite.
# It creates a table, inserts some data, and retrieves it within a context manager.
# The connection is automatically closed when exiting the context.
# The context manager also handles exceptions and prints an error message if one occurs.