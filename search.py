def search_contact(contact_book):
    search_key = input("Enter name to search in the model by : ")

    flag = False
    for idx, contact in enumerate(contact_book):
        if (search_key.lower() in contact["name"].lower()):
            print(f"index: {idx+1} !!!\n{contact['name']} - {contact['phone']} - {contact['email']}")
            flag = True

    if (not flag):
        print("No contact found (-_-)")