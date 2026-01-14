from db_connection import get_connection

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        publisher TEXT,
        category TEXT,
        isbn TEXT,
        status TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS members (
        member_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        address TEXT,
        membership_date TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS librarians (
        librarian_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS issue_records (
        issue_id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER,
        member_id INTEGER,
        issue_date TEXT,
        due_date TEXT,
        return_date TEXT,
        FOREIGN KEY(book_id) REFERENCES books(book_id),
        FOREIGN KEY(member_id) REFERENCES members(member_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fines (
        fine_id INTEGER PRIMARY KEY AUTOINCREMENT,
        issue_id INTEGER,
        amount REAL,
        payment_status TEXT,
        FOREIGN KEY(issue_id) REFERENCES issue_records(issue_id)
    )
    """)

    connection.commit()
    connection.close()

create_tables()
