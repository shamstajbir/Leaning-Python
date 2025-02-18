import json
from utils import *

lent_books = []

def load_lent_books():
    global lent_books
    try:
        with open('lent_books.json', 'r') as file:
            lent_books = json.load(file)
    except FileNotFoundError:
        lent_books = []

def save_lent_books():
    with open('lent_books.json', 'w') as file:
        json.dump(lent_books, file, indent=4)

def lend_book():
    search_term = input("Enter title or ISBN to lend: ")
    for book in books:
        if search_term.lower() in book['title'].lower() or search_term in book['isbn']:
            if book['quantity'] > 0:
                borrower = input("Enter borrower's name: ")
                book['quantity'] -= 1
                lent_books.append({"book": book, "borrower": borrower})
                save_books()
                save_lent_books()
                print("Book lent successfully!")
                return
            else:
                print("Not enough books available to lend.")
                return
    print("Book not found.")

def return_book():
    search_term = input("Enter title or ISBN to return: ")
    borrower_name = input("Enter borrower's name: ")
    for lent in lent_books:
        if (search_term.lower() in lent['book']['title'].lower() or search_term in lent['book']['isbn']) and borrower_name == lent['borrower']:
            lent_books.remove(lent)
            for book in books:
                if book['isbn'] == lent['book']['isbn']:
                    book['quantity'] += 1
                    save_books()
                    save_lent_books()
                    print("Book returned successfully!")
                    return
    print("Lent book not found.")

def view_lent_books():
    for lent in lent_books:
        print(f"Book: {lent['book']['title']}, Borrower: {lent['borrower']}")
