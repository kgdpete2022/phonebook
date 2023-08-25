import csv

CSV_FILE = "phonebook.csv"
HEADER_FIELDS = [
    "Last name",
    "First Name",
    "Middle Name",
    "Company",
    "Phone (work)",
    "Phone (cell)",
]


def read_list_from_csv():
    """Takes a csv file and returns a list of contacts as lists"""
    with open(CSV_FILE, "r") as f:
        # Convert data to list omitting the header
        contacts = list(csv.reader(f))[1:]
    return contacts


def write_list_to_csv(contacts):
    """Takes a list of contacts, adds header fields, writes the result into a csv file."""
    with open(CSV_FILE, "w") as f:
        write = csv.writer(f)
        write.writerow(HEADER_FIELDS)
        write.writerows(contacts)
        print("The file {CSV_FILE} has been updated sucessfully")


def add_contact_to_phonebook(contact):
    """Reads contacts from csv, adds new contact, writes the updated contacts to CSV"""
    contacts = read_list_from_csv()
    contacts.append(contact)
    return contacts


def print_phonebook(contacts_per_page=None):
    contacts = read_list_from_csv()
    contacts.sort()
    total_contacts = len(contacts)
    if contacts_per_page == None:
        contacts_per_page = total_contacts
    total_full_pages = total_contacts // contacts_per_page

    # number of contacts on the last page if total contacts not evenly divided by contacts per page
    contacts_on_partly_filled_page = total_contacts % contacts_per_page

    for i in range(total_contacts):
        # prints header fiels on every new page of contacts
        if (i + 1) % contacts_per_page == 1:
            print("-" * 130)
            print(
                "{:<15} {:<15} {:<15} {:<45} {:<20} {:<20}".format(
                    *HEADER_FIELDS
                )
            )
            print("-" * 130)

        print("{:<15} {:<15} {:<15} {:<45} {:<20} {:<20}".format(*contacts[i]))

        # prints a line and contacts range at the end of each page of contacts
        if (i + 1) % contacts_per_page == 0:
            print("-" * 130)
            print(
                f"contacts {i + 2 - contacts_per_page}-{i + 1} of {total_contacts}"
            )
    # prints a line and contacts range on the last page of contacts (if total contacts not evenly divided by contacts per page)
    if contacts_on_partly_filled_page:
        print("-" * 130)
        print(
            f"contacts {total_full_pages * contacts_per_page + 1}-{total_contacts} of {total_contacts}"
        )


print_phonebook(20)
