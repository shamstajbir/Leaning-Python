def backup_contact(contact_book):
    with open("contcats.csv", "wt") as fp:
        pass

    with open("contcats.csv", "a", newline="\n") as fp:
        for contact in contact_book:
            line = f"{contact["name"]},{contact["phone"]},{contact["email"]}\n"
            fp.write(line)