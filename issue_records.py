from db_connection import get_connection

def issue_book(book_id, member_id, issue_date, due_date):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO issue_records (book_id, member_id, issue_date, due_date, return_date)
        VALUES (?, ?, ?, ?, NULL)
    """, (book_id, member_id, issue_date, due_date))

    cursor.execute("""
        UPDATE books SET status = 'Issued' WHERE book_id = ?
    """, (book_id,))

    connection.commit()
    connection.close()

def return_book(issue_id, return_date, book_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE issue_records SET return_date = ? WHERE issue_id = ?
    """, (return_date, issue_id))

    cursor.execute("""
        UPDATE books SET status = 'Available' WHERE book_id = ?
    """, (book_id,))

    connection.commit()
    connection.close()
