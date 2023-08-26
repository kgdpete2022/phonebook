import argparse

parser = argparse.ArgumentParser(
    description="Phonebook - search, edit, and list contacts"
)
parser.add_argument(
    "-A", "--action", choices=("print", "add", "edit", "search")
)

parser.add_argument(
    "-sv",
    "--search_values",
    help="Search values. Enter 6 comma-separated values: last name, first name, middle name, company name, work phone, cellphone. Leave blank space for values that should not be searched. Each value is case-sensitive and may be added in part, in full, or left blank. Multiple matches may be found as the result.",
)

parser.add_argument(
    "-oc",
    "--old_contact",
    help="Contact to be edited. Enter 6 comma-separated values: last name, first name, middle name, company name, work phone, cellphone. No blank values allowed. Used with '--edit' and '--new-contact' arguments. Case-sensitive.",
)

parser.add_argument(
    "-nc",
    "--new_contact",
    type=str,
    help="Contact to add. Enter 6 comma-separated values: last name, first name, middle name, company name, work phone, cellphone. No blank values allowed. Used with '--add', '--edit' and '--old-contact' arguments.",
)

args = parser.parse_args()
