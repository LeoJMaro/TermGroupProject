from prettytable import PrettyTable

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget,QFileDialog, QGridLayout, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

from controller import *

widgets = {
    "buttons": {}
}


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Add Customer")
window.setFixedWidth(1000)
window.setFixedHeight(500)
window.setStyleSheet("background:black;")


grid = QGridLayout()


def customer():

    title = QLabel('Customer Information')
    title.setStyleSheet("color:white;")
    grid.addWidget(title,0,1)

    first_name_label = QLabel('First Name')
    first_name_label.setStyleSheet("color: white;")
    grid.addWidget(first_name_label,1,0)
    first_name_input = QLineEdit()
    first_name_input.setStyleSheet("background: white;")
    grid.addWidget(first_name_input, 1, 1)


    last_name_label = QLabel('Last Name')
    last_name_label.setStyleSheet("color: white;")
    grid.addWidget(last_name_label, 2, 0)
    last_name_input = QLineEdit()
    last_name_input.setStyleSheet("background: white;")
    grid.addWidget(last_name_input, 2, 1)

    phone_label = QLabel('Phone Number')
    phone_label.setStyleSheet("color: white;")
    grid.addWidget(phone_label, 3, 0)
    phone_input = QLineEdit()
    phone_input.setStyleSheet("background: white;")
    grid.addWidget(phone_input, 3, 1)

    email_label = QLabel('Email')
    email_label.setStyleSheet("color: white;")
    grid.addWidget(email_label, 4, 0)
    email_input = QLineEdit()
    email_input.setStyleSheet("background: white;")
    grid.addWidget(email_input, 4, 1)

    address_label = QLabel('Address')
    address_label.setStyleSheet("color: white;")
    grid.addWidget(address_label, 5, 0)
    address_input = QLineEdit()
    address_input.setStyleSheet("background: white;")
    grid.addWidget(address_input, 5, 1)

    add_button = QPushButton('Add Customer')
    add_button.setStyleSheet("background: white;")
    grid.addWidget(add_button,6,1)

    feedback_label = QLabel()
    feedback_label.setStyleSheet("color:white;")
    grid.addWidget(feedback_label,7,1)

    def add_new_customer():


        try:
            customer_first_name = first_name_input.text()
            customer_last_name = last_name_input.text()
            customer_phone = phone_input.text()
            customer_email = email_input.text()
            customer_address = address_input.text()
            print("worked")
            to_controller = add_customer(customer_first_name,customer_last_name,customer_phone,customer_email,customer_address)
        except Exception as e:
            feedback_label.setText(str(e))

        else:
            if to_controller == 1:
                feedback_label.setText("Customer Added")
            else:
                feedback_label.setText("Failed to Add Customer")

    add_button.clicked.connect(add_new_customer)

#homepage()
customer()






window.setLayout(grid)

window.show()

sys.exit(app.exec())








#---------------------------------------------------------------------------------------------------------------
# Placeholder view
transaction_items = []
products_table = PrettyTable()
def initialize_tables():
    products_table = PrettyTable()
    products_table.field_names = show_products()[0]
    products_table.add_rows(show_products()[1])
    return products_table
def display_options():
    print('=' * 50)
    print('0. Exit')
    print('1. Start Transaction ')
    print('=' * 50)


def transaction_options():
    print('=' * 50)
    print('0. Exit')
    print('1. Show Items')
    print('2. Add Item')
    print('3. Remove Item')
    print('=' * 50)


if __name__ == '__main__':
    products_table = initialize_tables()
    while True:
        display_options()
        user_choice = input('Enter a choice: ')
        match user_choice:
            case '0':
                break
            case '1':
                while True:
                    transaction_options()
                    user_choice = input('Enter a choice: ')
                    match user_choice:
                        case '0':
                            break
                        case '1':
                            print(products_table)
                        case '2':
                            print(products_table)
                            user_product_choice = input('Choose product: ')


                        case '3':
                            pass
            case '2':
                pass
