# Phonebook

This app was created as a test assigment during a job application process.
The app allows basic manipulation of contact information in a phonebook (add, search, edit and display contacts) without the use of a database.
The data is stored in a csv file and is accessed through a command line interface.

## Installation and setup

1. Clone the repository to your local computer:

```
git clone git@github.com:kgdpete2022/phonebook.git
```

2. (Optional) In the console run the script to upload initial data to the csv file:

```
python load_test_data.py
```


## Basic commands:

All commands are executing through the use of the -A/--action attribute, consisting of 4 options: print, add, search, edit.

