import csv

from test_data import contacts

if __name__ == "__main__":
    with open("phonebook.csv", "w", encoding="utf8", newline="") as f:
        fc = csv.DictWriter(
            f,
            fieldnames=contacts[0].keys(),
        )
        fc.writeheader()
        fc.writerows(contacts)
