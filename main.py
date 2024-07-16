from book_manager import *
from lending_manager import *


def menu():
    print("Library Management System")
    print("1. Add any Book")
    print("2. View All Books")
    print("3. Search Books by Title/ISBN")
    print("4. Search Books by Author")
    print("5. Remove Book")
    print("6. Lend Book")
    print("7. Return Book")
    print("8. View Lent Books")
    print("9. Exit")

def main():
    load_books()
    load_lent_books()
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_books_by_title_or_isbn()
        elif choice == '4':
            search_books_by_author()
        elif choice == '5':
            remove_book()
        elif choice == '6':
            lend_book()
        elif choice == '7':
            return_book()
        elif choice == '8':
            view_lent_books()
        elif choice == '9':
            save_books()
            save_lent_books()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
