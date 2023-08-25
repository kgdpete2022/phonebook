from actions import (
    add_contact_to_phonebook,
    edit_existing_contact,
    print_contacts,
    read_list_from_csv,
    search_contacts,
)
from interface import args

if __name__ == "__main__":
    if args.action == "print":
        print_contacts(read_list_from_csv())
    elif args.action == "add":
        new_contact = args.new_contact.split(",")
        add_contact_to_phonebook(new_contact)
    elif args.action == "edit":
        old_contact = args.old_contact.split(",")
        new_contact = args.new_contact.split(",")
        edit_existing_contact(old_contact, new_contact)
    elif args.action == "search":
        search_values = args.contact_to_search.split(",")
        print_contacts(search_contacts(search_values))
