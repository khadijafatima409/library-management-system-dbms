from books import add_book, get_all_books
from members import add_member

add_book("DBMS", "Korth", "McGraw Hill", "Education", "12345", "Available")
add_member("Ali", "ali@gmail.com", "0300", "Lahore", "2026-01-14")

print(get_all_books())

