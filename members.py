from db_connection import get_connection

def add_member(name, email, phone, address, membership_date):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO members (name, email, phone, address, membership_date)
        VALUES (?, ?, ?, ?, ?)
    """, (name, email, phone, address, membership_date))
    connection.commit()
    connection.close()

def get_all_members():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()
    connection.close()
    return members
