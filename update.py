import backup

def update_contact(contact_book):
    search_key = input("Enter name to search and update: ")

    for idx, contact in enumerate(contact_book):
        if (search_key.lower() in contact["name"].lower()):
            print(f"Found index: {idx+1} !!!\n{contact['name']} - {contact['phone']} - {contact['email']}")

    selected_idx = int(input("Enter a   contact index to  update: "))

    new_name = contact_book[selected_idx-1]["name"]
    new_phone = contact_book[selected_idx-1]["phone"]
    new_email = contact_book[selected_idx-1]["email"]

    up1 = input("Do you want to update the name [y to proceed]: ")
    if (up1 == "y"):
        new_name = input("Enter new name: ")

    up2 = input("Do you want to update the phone [y to proceed]: ")
    if (up2 == "y"):
        new_phone = input("Enter new phone: ")
    up3 = input("Do you want to update the email [y to proceed]: ")
    if (up3 == "y"):
        new_email = input("Enter new email: ")

    contact_book[selected_idx-1].update(
        {
            "name": new_name,
            "phone": new_phone,
            "email": new_email,
        }

    )


    print("Contact updated successfully!!!")

    backup.backup_contact(contact_book)

    return contact_book
