
# TermGroupProject

A windows application built in python with PyQt5 to simulate an inventory and transaction system for a fictional board game store called:

*"Newfie Buddy's Board Game Emporium"*

The application allows users to create customers and simulate transactions with these customers where various products can be added to the transaction.

At the end of the transactions an invoice is generated so the user can view all purchased products, their quantity, price, and the total cost of the invoice.

Users can also view existing and unavailable products, view customers with activity within the last month and add stock to products in the store.

The data for the system is stored using a MySQL database which can be generated using an included script.

This project was created as a term project for the College of the North Atlantic's Software Development Co-op course in the Object Oriented Programming and Database Management Systems 2 courses.



## Setup
- Before starting the program, be sure to run *group_project_database_creation_and_insertion_code.sql* in order to generate the required MySQL database
- You may also need to generate a SECRETS.py file with the following body:
 - ` PASSWORD = "your_sql_db_password" USER = "root" DATABASE = "pgp"`
 - Once these first two steps have been completed, you can start the system by running *view.py*
## Authors

- [@LeoJMaro](https://github.com/LeoJMaro)
- [@goro391](https://github.com/goro391)
- [@GregID](https://github.com/gregularjoe)
- [@Noah Forward](https://github.com/UnusualFrog)

## Technologies
Project was created with:

- Python version: 3.11
- MySQL version: 8.0
- PyQt5 version: 5.15.9
- mysql-connector-python version: 8.0.32


