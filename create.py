import backup

def create_contact(contact_book):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contact_book.append(new_contact)

    print("Contact created successfully!!!")

    backup.backup_contact(contact_book)

    return contact_book