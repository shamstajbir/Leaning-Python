import json
from utils import *

books = []

def load_books():
    global books
    try:
        with open('books.json', 'r') as file:
            books = json.load(file)
    except FileNotFoundError:
        books = []

def save_books():
    with open('books.json', 'w') as file:
        json.dump(books, file, indent=4)

def add_book():
    title = input("Enter book title: ")
    authors = input("Enter author(s): ")
    isbn = input("Enter ISBN: ")
    year = input("Enter publishing year: ")
    price = validate_price(input("Enter price: "))
    quantity = validate_quantity(input("Enter quantity: "))

    book = {
        "title": title,
        "authors": authors,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity
    }

    books.append(book)
    save_books()
    print("Book added successfully!")

def view_books():
    for book in books:
        print(book)

def search_books_by_title_or_isbn():
    search_term = input("Enter title or ISBN to search: ")
    results = [book for book in books if search_term.lower() in book['title'].lower() or search_term in book['isbn']]
    for result in results:
        print(result)

def search_books_by_author():
    search_term = input("Enter author name to search: ")
    results = [book for book in books if search_term.lower() in book['authors'].lower()]
    for result in results:
        print(result)

def remove_book():
    search_term = input("Enter title or ISBN to remove: ")
    book_to_remove = None
    for book in books:
        if search_term.lower() in book['title'].lower() or search_term in book['isbn']:
            book_to_remove = book
            break

    if book_to_remove:
        books.remove(book_to_remove)
        save_books()
        print("Book removed successfully!")
    else:
        print("Book not found.")
