from actions import (
    print_formatted_contact,
    print_formatted_header,
    read_list_from_csv,
)
from settings import TOTAL_WIDTH


def print_contacts_range(contacts, start_index, end_index):
    print_formatted_header()
    for contact in contacts[start_index:end_index]:
        print_formatted_contact(contact)
    print("-" * TOTAL_WIDTH)
    print(f"Contacts {start_index + 1}-{end_index} of {len(contacts)}\n")


def print_contacts(contacts):
    contacts.sort()
    contacts_per_page = int(
        input(
            "Enter the number of contacts to be printed on each page or '0' to print them all on one page: "
        )
    )
    total_contacts = len(contacts)

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
                print("Phonebook browsing ended by the user")
                break
            elif user_input == "n":
                if current_page != total_pages:
                    current_page += 1
                else:
                    print("This is the last page. Please try another option.")
                continue
            elif user_input == "p":
                if current_page != 1:
                    current_page -= 1
                    continue
                else:
                    print("This is the first page. Please try another option.")
            else:
                print(f"'{user_input}' is not a valid option, please again.")


test_contacts = read_list_from_csv()

print_contacts(test_contacts)
