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


def get_sorted_list_from_csv(CSV_FILE):
    """Takes a csv file and returns a sorted list of lists"""
    with open(CSV_FILE, "r") as f:
        csv_f = csv.reader(f)
        contacts = []
        for contact in csv_f:
            contacts.append(contact)
    header = contacts[0]
    contacts = contacts[1:]
    contacts.sort()
    return header + contacts


def write_sorted_list_to_csv(CSV_FILE, contacts):
    """Takes a sorted list of lists and writes it into a csv file"""
    with open(CSV_FILE, "w") as f:
        write = csv.writer(f)
        write.writerows(contacts)
        print("The file {CSV_FILE} has been updated sucessfully")


def print_contacts(contacts, contacts_per_page=None):
    total_contacts = len(contacts)
    if contacts_per_page == None:
        contacts_per_page = total_contacts
    total_full_pages = total_contacts // contacts_per_page
    contacts_on_last_page = total_contacts % contacts_per_page

    for i in range(len(contacts)):
        print("{:<15} {:<15} {:<15} {:<45} {:<20} {:<20}".format(*contacts[i]))
        if (i + 1) % contacts_per_page == 0:
            print("-" * 130)
            print(
                f"contacts {i + 2 - contacts_per_page}-{i + 1} of {total_contacts}"
            )
    if contacts_on_last_page:
        print("-" * 130)
        print(
            f"contacts {total_full_pages * contacts_per_page + 1}-{total_contacts} of {total_contacts}"
        )


print_contacts(get_sorted_list_from_csv(CSV_FILE), 20)
