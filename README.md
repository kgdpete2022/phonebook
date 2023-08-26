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

All commands are executed by running the phonebook.py script with the -A/--action argument, consisting of 4 possible options: print, add, edit, search:

1. print - displays contacts from the phonebook sorted by last name in alphabetical order, requires no additional arguments. Example:
```
python phonebook.py -A print
```
Follow the prompts to display the contacts or exit.

2. add - adds a new contact to the phonebook, requires one additional argument: -nc/--new_contact (a string of 6 comma-separated values corresponding to last name, first name, middle name, company name, work phone, cellphone). Example:
```
python phonebook.py -A add -nc "Scott, Michael, Gary, Dunder Mifflin, (012) 3456789, (987) 64321"
```
3. edit - edits an existing contact in the phonebook, requires two extra arguments: -oc/--old_contact and -nc/--new_contact (both are strings of 6 comma-separated values corresponding to last name, first name, middle name, company name, work phone, cellphone). -oc data must be entered in full to avoid ambiguity or a false match. Example:
```
python phonebook.py -A edit -oc "Scott, Michael, Gary, Dunder Mifflin, (012) 3456789, (987) 64321" -nc "Shrute, Dwight, Kurt, Dunder Mifflin, (012) 111111, (987) 2222222"
```
4. search - finds contacts in the phonebook matching the provided data, requires one additional argument: -sv/--search_values (6 comma-separated values corresponding to last name, first name, middle name, company name, work phone, cellphone. Leave blank space for values that should not be searched. Each value is case-sensitive and may be added in part, in full, or left blank. Multiple matches may be found as the result.) Example:

```
python phonebook.py -A search -sv "P,,,,,"
```
This will return all contacts with last name starting with the letter "P" (7 matches in the test dataset):
----------------------------------------------------------------------------------------------------------------------------------
Last name       First Name      Middle Name     Company                                       Phone (work)         Phone (cell)        
----------------------------------------------------------------------------------------------------------------------------------
Paul            Gisela          Channing        Dapibus Gravida Corp.                         (021) 24818674       (006) 94200382
Petty           Fitzgerald      Reese           Iaculis Inc.                                  (00366) 5083088      (08607) 6564837
Phillips        Helen           Clare           Interdum Inc.                                 (08184) 2673517      (033883) 076142
Phillips        Jaime           Iona            Nulla Semper Tellus Limited                   (0629) 29168229      (098) 26132110
Pope            Dara            Tarik           Sociis Natoque Inc.                           (00282) 9917572      (0087) 85734227
Potter          Maxwell         Ori             Cras Lorem Inc.                               (04884) 2440861      (044) 18012479
Pratt           Ima             Kiayada         Nisl Maecenas Associates                      (0238) 13933753      (084) 77213442
----------------------------------------------------------------------------------------------------------------------------------
Contacts 1-7 of 7


```
python phonebook.py -A search -sv "tt,,,,,07"
```
This will return all contacts with last name containing "tt" and cellphone having the sequence of "07" (2 matches in the test dataset):
----------------------------------------------------------------------------------------------------------------------------------
Last name       First Name      Middle Name     Company                                       Phone (work)         Phone (cell)        
----------------------------------------------------------------------------------------------------------------------------------
Petty           Fitzgerald      Reese           Iaculis Inc.                                  (00366) 5083088      (08607) 6564837
Sutton          Amy             Cecilia         Tempus Non Ltd                                (084) 84047599       (0623) 14378007
----------------------------------------------------------------------------------------------------------------------------------
Contacts 1-2 of 2



## Developed by
Piotr Shopin (mail4dev2022@gmail.com)