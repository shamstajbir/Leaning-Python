import backup


def remove_contact(contact_book):
    search_key = input("Enter name to search and delete: ")

    for idx, contact in enumerate(contact_book):
        if (search_key.lower() in contact["name"].lower()):
            print(f"Found index: {idx + 1} !!!\n{contact['name']} - {contact['phone']} - {contact['email']}")

    selected_idx = int(input("Enter a contact index to remove: "))
    contact_book.pop(selected_idx - 1)

    print("Contact removed successfully!!!")

    backup.backup_contact(contact_book)

    return contact_book