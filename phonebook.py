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
        print("The file {CSV_FILE} has been updated")


def add_contact_to_phonebook(contact):
    """Reads contacts from csv, adds new contact, writes the updated contacts to csv"""
    contacts = read_list_from_csv()
    if contact in contacts:
        print(f"Such contact already exists!")
    else:
        contacts.append(contact)
        write_list_to_csv(contacts)


def edit_existing_contact(contact_old, contact_new):
    """Reads contacts from csv, finds the contact to update, edit it, write all contacts to csv"""
    contacts = read_list_from_csv()
    if contact_new in contacts:
        print(f"Can't make this change, as such contact already exists!")
    else:
        index = contacts.index(contact_old)
        contacts[index] = contact_new
        write_list_to_csv(contacts)


def find_contacts(search_values):
    """Finds contacts based on provided search values"""
    contacts = read_list_from_csv()
    matched_contacts = []
    for contact in contacts:
        search_values_matched = True
        for i in range(len(HEADER_FIELDS)):
            if search_values[i] in contact[i]:
                continue
            else:
                search_values_matched = False
                break
        if search_values_matched:
            matched_contacts.append(contact)
        else:
            search_values_matched = True
    return matched_contacts


def print_contacts(contacts_to_print, contacts_per_page=None):
    if not contacts_to_print:
        print("No contacts to print!")
    else:
        contacts_to_print.sort()
        total_contacts = len(contacts_to_print)
        if contacts_per_page == None:
            contacts_per_page = total_contacts
        total_full_pages = (
            total_contacts // contacts_per_page if contacts_per_page else 0
        )

        # number of contacts on the last page if total contacts not evenly divided by contacts per page
        contacts_on_partly_filled_page = (
            total_contacts % contacts_per_page if contacts_per_page else 0
        )

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

            print(
                "{:<15} {:<15} {:<15} {:<45} {:<20} {:<20}".format(
                    *contacts_to_print[i]
                )
            )

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


# add_contact_to_phonebook(
#     [
#         "Douglas",
#         "Phillip",
#         "Gisela",
#         "Tincidunt Orci PC",
#         "(01850) 7252127",
#         "(04695) 3413952",
#     ]
# )


# print_contacts(read_list_from_csv(), 30)
print_contacts(
    find_contacts(
        [
            "",
            "",
            "",
            "",
            "",
            "72",
        ]
    )
)
