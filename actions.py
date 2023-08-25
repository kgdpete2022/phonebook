import csv

from settings import CSV_FILE, HEADER_FIELDS, PAGED_OUT_THRESHOLD, TOTAL_WIDTH


def read_list_from_csv():
    """Takes a csv file and returns a list of contacts as lists"""
    with open(CSV_FILE, "r") as f:
        # Convert data to list omitting the header
        contacts = list(csv.reader(f))[1:]
    return contacts


def write_list_to_csv(contacts):
    """Takes a list of contacts, adds header fields, writes the result into a csv file."""
    with open(CSV_FILE, "w", newline="") as f:
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


def search_contacts(search_values):
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


def print_formatted_header():
    print("-" * TOTAL_WIDTH)
    print("{:<15} {:<15} {:<15} {:<45} {:<20} {:<20}".format(*HEADER_FIELDS))
    print("-" * TOTAL_WIDTH)


def print_formatted_contact(contact):
    print("{:<15} {:<15} {:<15} {:<45} {:<20} {:<20}".format(*contact))


def print_contacts_range(contacts, start_index, end_index):
    print_formatted_header()
    for contact in contacts[start_index:end_index]:
        print_formatted_contact(contact)
    print("-" * TOTAL_WIDTH)
    print(f"Contacts {start_index + 1}-{end_index} of {len(contacts)}\n")


def print_contacts(contacts):
    contacts.sort()
    total_contacts = len(contacts)
    if total_contacts <= PAGED_OUT_THRESHOLD:
        contacts_per_page = 0
    else:
        contacts_per_page = int(
            input(
                "Enter the number of contacts to be printed on each page or '0' to print them all on one page: "
            )
        )

    if not total_contacts:
        print("No contacts to print!\n")

    elif not contacts_per_page or contacts_per_page >= total_contacts:
        print_contacts_range(contacts, 0, total_contacts)

    else:
        full_pages = total_contacts // contacts_per_page
        contacts_on_partly_filled_page = total_contacts % contacts_per_page
        total_pages = (
            full_pages + 1 if contacts_on_partly_filled_page else full_pages
        )
        current_page = 1

        user_input = "n"

        while True:
            start_index = (current_page - 1) * contacts_per_page
            if current_page == total_pages and contacts_on_partly_filled_page:
                end_index = (
                    current_page - 1
                ) * contacts_per_page + contacts_on_partly_filled_page
            else:
                end_index = current_page * contacts_per_page
            print_contacts_range(contacts, start_index, end_index)

            user_input = input(
                "Enter 'n' to see the next page, 'p' to see the previous page, or 'e' to end browsing: "
            )

            if user_input == "e":
                print("Phonebook browsing ended by the user.\n")
                break
            elif user_input == "n":
                if current_page != total_pages:
                    current_page += 1
                else:
                    print(
                        "This is the last page. Please try another option.\n"
                    )
                continue
            elif user_input == "p":
                if current_page != 1:
                    current_page -= 1
                    continue
                else:
                    print(
                        "This is the first page. Please try another option.\n"
                    )
            else:
                print(
                    f"'{user_input}' is not a valid option, please try again.\n"
                )
