
import sys
import controller
from controller import *
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout,\
    QTableWidget, QTableWidgetItem, QLineEdit, QComboBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

# This was the original GUI view created for the project, it acted as first draft for the current view, and without
# the effort and many contributions of the team members who completed it, the new view would not have been possible


widgets = {
    "button_inventory": [],
    "transaction": [],
    "customer":[]
}

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Homepage")
window.setFixedWidth(1200)
window.setFixedHeight(800)


window.setStyleSheet("background:black;")

invoice_window = QWidget()
invoice_window.setFixedWidth(1000)
invoice_window.setFixedHeight(500)
invoice_window.setStyleSheet("background:black;")


grid = QGridLayout()

def clear_widgets():
    for widget in widgets:

        if widgets[widget] != []:
            widgets[widget][-1].hide()

        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()

def homepage():

    button_inventory = QPushButton("Inventory")
    button_inventory.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button_inventory.setStyleSheet("border: 4px solid white;" + "color:white;")
    button_inventory.clicked.connect(clear_widgets)
    button_inventory.clicked.connect(inventory_page)
    widgets["button_inventory"].append(button_inventory)
    grid.addWidget(widgets["button_inventory"][-1], 0, 0)

    transaction = QPushButton("Transaction")
    transaction.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    transaction.setStyleSheet("border: 4px solid white;" + "color:white;")
    transaction.clicked.connect(clear_widgets)
    transaction.clicked.connect(point_of_sale_display)
    widgets["transaction"].append(transaction)

    grid.addWidget(widgets["transaction"][-1], 1, 0)
    transaction.clicked.connect(point_of_sale_display)

    customer = QPushButton("Customer")
    customer.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    customer.setStyleSheet("border: 4px solid white;" + "color:white;")
    customer.style()
    customer.clicked.connect(clear_widgets)
    customer.clicked.connect(customer_display)
    widgets["customer"].append(customer)

    grid.addWidget(widgets["customer"][-1], 2, 0)


def inventory_page():

    table = QTableWidget()
    table.height()
    table.width()
    grid.addWidget(table, 1, 0)
    table.setColumnCount(6)
    data = controller.show_products()[1]
    table.setHorizontalHeaderLabels(["product_id",
                                     "vendor_id",
                                     "product_name",
                                     "product_description",
                                     "inventory_stock",
                                     "price"])
    table.setStyleSheet("color:white;")
    for row, end in enumerate(data):

        data = QTableWidgetItem(end[0])
        data.setTextAlignment(4)
        table.insertRow(row)
        table.setItem(row, 0, QTableWidgetItem(str(end[0])))
        table.setItem(row, 1, QTableWidgetItem(str(end[1])))
        table.setItem(row, 2, QTableWidgetItem(str(end[2])))
        table.setItem(row, 3, QTableWidgetItem(str(end[3])))
        table.setItem(row, 4, QTableWidgetItem(str(end[4])))
        table.setItem(row, 5, QTableWidgetItem(str(end[5])))
    add_to_inventory_button = QPushButton("Add to Inventory")
    add_to_inventory_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    grid.addWidget(add_to_inventory_button,0,0)
    add_to_inventory_button.setStyleSheet("background-color: white;")
    add_to_inventory_button.clicked.connect(customer_display)

    def add_to_inventory_display():
        window.setWindowTitle("Add to Inventory")

        product_name_label = QLabel("Product Name:")
        grid.addWidget(product_name_label,1,1)
        product_name_label.setStyleSheet("")


        # function that sets all the labels, buttons, line edits in place Window title and title, background color
def customer_display():
    window.setWindowTitle("Add Customer")
    title = QLabel('Customer Information')
    title.setStyleSheet("color:white;")
    grid.addWidget(title,0,1)
    # Label and input for customer_first_name
    first_name_label = QLabel('First Name')
    first_name_label.setStyleSheet("color: white;")
    grid.addWidget(first_name_label,1,0)
    first_name_input = QLineEdit()
    first_name_input.setStyleSheet("background: white;")
    grid.addWidget(first_name_input, 1, 1)
    # Label and input for customer_last_name
    last_name_label = QLabel('Last Name')
    last_name_label.setStyleSheet("color: white;")
    grid.addWidget(last_name_label, 2, 0)
    last_name_input = QLineEdit()
    last_name_input.setStyleSheet("background: white;")
    grid.addWidget(last_name_input, 2, 1)
    # Label and input for customer_phone
    phone_label = QLabel('Phone Number')
    phone_label.setStyleSheet("color: white;")
    grid.addWidget(phone_label, 3, 0)
    phone_input = QLineEdit()
    phone_input.setStyleSheet("background: white;")
    grid.addWidget(phone_input, 3, 1)
        # Label and input for customer_email
    email_label = QLabel('Email')
    email_label.setStyleSheet("color: white;")
    grid.addWidget(email_label, 4, 0)
    email_input = QLineEdit()
    email_input.setStyleSheet("background: white;")
    grid.addWidget(email_input, 4, 1)
        # Label and input for customer_address
    address_label = QLabel('Address')
    address_label.setStyleSheet("color: white;")
    grid.addWidget(address_label, 5, 0)
    address_input = QLineEdit()
    address_input.setStyleSheet("background: white;")
    grid.addWidget(address_input, 5, 1)
        # Button adds info from gui inputs to customer_table when clicked
    add_button = QPushButton('Add Customer')
    add_button.setStyleSheet("background: white;")
    grid.addWidget(add_button,6,1)
        # Label that confirms wheather add has worked or not
    feedback_label = QLabel()
    feedback_label.setStyleSheet("color:white;")
    grid.addWidget(feedback_label,7,1)

    def add_new_customer():
        # Function that connects add customer line edits and button to database
        try:
            customer_first_name = first_name_input.text()
            customer_last_name = last_name_input.text()
            customer_phone = phone_input.text()
            customer_email = email_input.text()
            customer_address = address_input.text()
            to_controller = add_customer(customer_first_name,customer_last_name,
                                         customer_phone,customer_email,customer_address)
        except Exception as e:
            feedback_label.setText(str(e))

        else:
            if to_controller == 1:
                feedback_label.setText("Customer Added")
            else:
                feedback_label.setText("Failed to Add Customer")

    add_button.clicked.connect(add_new_customer)

def point_of_sale_display():
    # Function that sets all labels, and combo boxes in place

    window.setWindowTitle("Point of Sale")
    select_customer_label = QLabel('Select Customer:')
    grid.addWidget(select_customer_label,0,0)
    select_customer_label.setStyleSheet("color: white;")
    # Combo box which allows selection from list of customers from customers table in pgp database
    customer_combobox = QComboBox(window)
    grid.addWidget(customer_combobox,0,1)
    customer_combobox.setStyleSheet("background-color: white;")
    # Uses for loop to add customer_fullname to combo box
    customer_combobox.addItem('')
    row = get_customer_names()
    for i in row[1]:
        data = str(i[0])
        customer_combobox.addItem(data)

    show_invoice_button = QPushButton('Show Invoice')  # Button when clicked shows invoice
    grid.addWidget(show_invoice_button, 4, 1)
    show_invoice_button.setStyleSheet("background-color: white;")

    # Label that holds customer_id, hidden from user, for use by later function
    customer_id_label = QLabel("")
    grid.addWidget(customer_id_label,0,3)

    # function which updates customer_id label with corresponding id for customer name selected
    def update_id_label():

        selected_name = customer_combobox.currentText()
        customer_fullname_split = selected_name.split(' ')
        customer_first_name = customer_fullname_split[0]
        customer_last_name = customer_fullname_split[1]
        info = get_customer_id_by_customer_name(customer_first_name,customer_last_name)

        customer_id_label.setText(info)

    customer_combobox.currentIndexChanged.connect(update_id_label)
        # Label for select product combobox
    select_product_label = QLabel('Select Product:')
    grid.addWidget(select_product_label,1,0)
    select_product_label.setStyleSheet("color: white;")
        # Label that displays price of item selected
    price_label = QLabel()
    grid.addWidget(price_label,1,3)
    price_label.setStyleSheet('color: white;')
        # Combo box which allows selection from list of products from products table in pgp database
    product_combobox = QComboBox(window)
    grid.addWidget(product_combobox, 1, 1)
    product_combobox.setStyleSheet("background-color: white;")
    product_combobox.addItem('')

    quantity_label = QLabel('Qty:')
    grid.addWidget(quantity_label,1,2)
    quantity_label.setStyleSheet("color: white;"+"max-width: 20px")

    quantity_line_edit = QLineEdit()
    grid.addWidget(quantity_line_edit,1,3)
    quantity_line_edit.setStyleSheet("background-color: white;"+"max-width: 50px")

        # Uses for loop to add product_name from product table

    row = get_product_names()
    for i in row[1]:
        pdata = str(i[0])
        product_combobox.addItem(pdata)

    # Function which updates price label with price of current product selection from combobox
    def update_price_label():

        product_name = product_combobox.currentText()
        info = get_price_with_product_name(product_name)
        price = str(f"List Price: ${info[11:16]} ea")
        price_label.setText(price)


    product_combobox.currentIndexChanged.connect(update_price_label)
    # Button which when clicked adds the customer id to the invoices table
    add_customer_id_to_invoices_button = QPushButton("Add Customer")
    grid.addWidget(add_customer_id_to_invoices_button, 0, 4)
    add_customer_id_to_invoices_button.setStyleSheet("background-color: white;")
    # Label which holds the invoice id
    invoice_id_label = QLabel()
    grid.addWidget(invoice_id_label, 4, 0)
    invoice_id_label.setStyleSheet('color: white;')
    # Label which holds product_id
    product_id_label = QLabel()
    grid.addWidget(product_id_label, 4, 0)
    product_id_label.setStyleSheet('color: white;')
    # Button which when clicked adds product id to invoice products table
    add_product_id_to_invoice_products_button = QPushButton("Add Product")
    grid.addWidget(add_product_id_to_invoice_products_button, 1, 4)
    add_product_id_to_invoice_products_button.setStyleSheet("background-color: white;")
    # Label that carries either confirmation of item added or an error code
    feedback_label = QLabel()
    feedback_label.setStyleSheet("color:white;")
    grid.addWidget(feedback_label, 3, 2)

    # Function when called adds the selected customer id to invoices table
    # and gets invoice id from this entry into invoices table for later use
    def add_customer_to_invoices():
        try:
            customer_id = customer_id_label.text()
            id_to_controller = add_customer_id_to_invoices(int(customer_id))
            invoice_id = get_most_recent_invoice_id_by_date()

        except Exception as e:
            feedback_label.setText(str(e))

        else:
            if id_to_controller == 1:
                feedback_label.setText("Successfully Added")
            else:
                feedback_label.setText("Failed to Add")

        # Function which gets product id from the products table using the product name selected from combobox
        # and uses previous query of invoice id then inserts both of them into invoice_products
        def add_product_to_invoice():
            try:
                product_choice = product_combobox.currentText()
                quantity = quantity_line_edit.text()

                product_id = get_product_id(product_choice)
                product_info_to_controller = add_product_to_invoice_products(invoice_id,product_id,quantity)

                # SHOULD BE A COUNT OF HOW MANY TIMES A PRODUCT ID WITH A SPECIFIED INVOICE ID IS PRESENT FOR
                # QUANTITY PURPOSES

            except Exception as e:
                feedback_label.setText(str(e))
            else:
                if product_info_to_controller == 1:
                    feedback_label.setText("Successfully Added")
                else:
                    feedback_label.setText("Failed to Add")

        add_product_id_to_invoice_products_button.clicked.connect(add_product_to_invoice)
    add_customer_id_to_invoices_button.clicked.connect(add_customer_to_invoices)


def invoice_display():
    invoice_window.show()
    grid2 = QGridLayout(invoice_window)
    invoice_window.setWindowTitle("Invoice")
    invoice_title = QLabel('Purchase Information')
    invoice_title.setStyleSheet("color:white;"+"font-size: 20px;")
    grid2.addWidget(invoice_title, 1, 0)

    table = QTableWidget()
    table.setStyleSheet("background-color: white;")
    table.height()
    table.width()
    grid2.addWidget(table, 2, 0)
    table.setColumnCount(6)
    data = controller.show_products()[1]
    for row, end in enumerate(data):

        idDato = QTableWidgetItem(end[0])
        idDato.setTextAlignment(4)
        table.insertRow(row)
        table.setItem(row, 0, idDato)
        table.setItem(row, 1, QTableWidgetItem(str(end[1])))
        table.setItem(row, 2, QTableWidgetItem(str(end[2])))
        table.setItem(row, 3, QTableWidgetItem(str(end[3])))
        table.setItem(row, 4, QTableWidgetItem(str(end[4])))
        table.setItem(row, 5, QTableWidgetItem(str(end[5])))

homepage()
#point_of_sale_display()
window.setLayout(grid)

window.show()

sys.exit(app.exec())