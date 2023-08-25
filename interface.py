import argparse

parser = argparse.ArgumentParser(
    description="Phonebook - search, edit, and list contacts"
)
parser.add_argument(
    "-A", "--action", choices=("print", "add", "edit", "search")
)

parser.add_argument(
    "-cts",
    "--contact_to_search",
    help="Contact to search. Enter 6 comma-separated values: last name, first name, middle name, company name, work phone, cellphone. Leave blank space for values that should not be searched. Each value may be added in part or in full.",
)

parser.add_argument(
    "-oc",
    "--old_contact",
    help="Contact to be edited. Enter 6 comma-separated values: last name, first name, middle name, company name, work phone, cellphone. No blank values allowed. Used with '--edit' and '--new-contact' arguments.",
)

parser.add_argument(
    "-nc",
    "--new_contact",
    type=str,
    help="Contact to edit. Enter 6 comma-separated values: last name, first name, middle name, company name, work phone, cellphone. No blank values allowed. Used with '--edit' and '--old-contact' arguments.",
)

args = parser.parse_args()
