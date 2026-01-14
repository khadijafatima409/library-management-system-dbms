from db_connection import get_connection

def add_book(title, author, publisher, category, isbn, status):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO books (title, author, publisher, category, isbn, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (title, author, publisher, category, isbn, status))
    connection.commit()
    connection.close()

def get_all_books():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    connection.close()
    return books

def update_book_status(book_id, status):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE books SET status = ? WHERE book_id = ?
    """, (status, book_id))
    connection.commit()
    connection.close()

def delete_book(book_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
    connection.commit()
    connection.close()
