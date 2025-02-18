def view_all_contacts(contact_book):
    for contact in contact_book:
        print(
            contact["name"],
            contact["phone"],
            contact["email"],
            sep= " | "
        )