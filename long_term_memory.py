import sqlite3


DB_NAME = "agent_memory.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_table():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_memory(role, message):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO memories (role, message)
        VALUES (?, ?)
        """,
        (role, message)
    )

    connection.commit()
    connection.close()


def get_memories(limit=10):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT role, message
        FROM memories
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    )

    memories = cursor.fetchall()

    connection.close()

    # Reverse so oldest appears first
    memories.reverse()

    return memories