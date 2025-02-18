import create
import view
import search
import remove
import backup
import update
import restore

contact_book = []


while(True):
    restore.restore_contact(contact_book)

    print("\nMenue:")
    menue_txt = """
    # Your options:
    1. Create Contact
    2. View All Contact
    3. Search Contacts
    4. Update Contact
    5. Remove Contact
    6. Exit
    """

    print(menue_txt)
    choice = input("Enter your choice: ")

    if (choice == "1"):
        create.create_contact(contact_book)
    elif (choice == "2"):
        view.view_all_contacts(contact_book)
    elif (choice == "3"):
        search.search_contact(contact_book)
    elif (choice == "4"):
        update.update_contact(contact_book)
    elif (choice == "5"):
        remove.remove_contact(contact_book)
    elif (choice == "6"):
        print("Program terminated!!!")
        break
    else:
        print("Wrong choice (-_-)")