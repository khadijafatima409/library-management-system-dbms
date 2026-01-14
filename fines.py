from db_connection import get_connection

def add_fine(issue_id, amount):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO fines (issue_id, amount, payment_status)
        VALUES (?, ?, 'Unpaid')
    """, (issue_id, amount))
    connection.commit()
    connection.close()
