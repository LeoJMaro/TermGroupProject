import sys
from controller import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class HomepageWindow(QWidget):
    """
    Homepage window class that redirects to other windows using buttons
    """

    def __init__(self):
        super().__init__()
        self.cams = None
        self.title = "Newfie Buddy's Board Game Emporium"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.initialize_window()

    def initialize_window(self):
        """
        Initializes widgets settings for the main window
        :return: None
        """
        # Window settings
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_DirClosedIcon))

        # Create buttons and connect their functions
        btn_view_products = QPushButton('View Products', self)
        btn_view_products.clicked.connect(self.btn_view_products_on_click)

        btn_view_oos_products = QPushButton('View Out of Stock Products', self)
        btn_view_oos_products.clicked.connect(self.btn_view_out_of_stock_products_on_click)

        btn_view_recent_customers = QPushButton('View Customers Active in the Last Month', self)
        btn_view_recent_customers.clicked.connect(self.btn_view_recent_customers_on_click)

        btn_add_customer = QPushButton('Add Customer', self)
        btn_add_customer.clicked.connect(self.btn_add_customer_on_click)

        btn_start_transaction = QPushButton('Start Transaction', self)
        btn_start_transaction.clicked.connect(self.btn_start_transaction_on_click)

        btn_add_stock = QPushButton('Add Stock', self)
        btn_add_stock.clicked.connect(self.btn_add_stock_on_click)

        # Create labels
        lbl_title = QLabel("Newfie Buddy's Board Game Emporium")
        lbl_title.setFont(QFont('Comic Sans MS', 20))
        lbl_title.setAlignment(Qt.AlignCenter)
        lbl_title.setMaximumHeight(36)

        # Create labels
        lbl_credits = QLabel("Created By: Jason Somerton-Earle, Gregory Dawe, Joel Oram, & Noah Forward")
        lbl_credits.setFont(QFont('Comic Sans MS', 12))
        lbl_credits.setAlignment(Qt.AlignCenter)
        lbl_credits.setMaximumHeight(30)

        # Create main layout and add buttons and labels to it
        main_layout = QVBoxLayout()
        main_layout.addWidget(lbl_title)
        main_layout.addWidget(btn_view_products)
        main_layout.addWidget(btn_view_oos_products)
        main_layout.addWidget(btn_view_recent_customers)
        main_layout.addWidget(btn_add_customer)
        main_layout.addWidget(btn_start_transaction)
        main_layout.addWidget(btn_add_stock)
        main_layout.addWidget(lbl_credits)

        self.setLayout(main_layout)

        self.show()

    def btn_view_products_on_click(self):
        """
        Open the view products window and close the current window
        :return: None
        """
        self.cams = ViewProductsWindow()
        self.cams.show()
        self.close()

    def btn_view_out_of_stock_products_on_click(self):
        """
        Open the view out of stock products window and close the current window
        :return: None
        """
        self.cams = ViewOOSProductsWindow()
        self.cams.show()
        self.close()

    def btn_view_recent_customers_on_click(self):
        """
        Open the view recent customers window and close the current window
        :return: None
        """
        self.cams = ViewRecentCustomers()
        self.cams.show()
        self.close()

    def btn_add_customer_on_click(self):
        """
        Open the add customers window and close the current window
        :return: None
        """
        self.cams = AddCustomerWindow()
        self.cams.show()
        self.close()

    def btn_start_transaction_on_click(self):
        """
        Open the start transaction window and close the current window
        :return: None
        """
        self.cams = StartTransactionWindow()
        self.cams.show()
        self.close()

    def btn_add_stock_on_click(self):
        """
        Open the add stock window and close the current window
        :return: None
        """
        self.cams = AddStockWindow()
        self.cams.show()
        self.close()


class ViewProductsWindow(QWidget):
    """
    Window for viewing all store products
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # Set window info
        self.setWindowTitle('View Products')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_DirClosedIcon))
        self.cams = None

        # Set window dimensions
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setGeometry(self.top, self.left, self.width, self.height)

        # Home Button
        self.home_button = QPushButton(self)
        self.home_button.setText('Return to Homepage')
        self.home_button.setGeometry(260, 450, 150, 30)
        self.home_button.clicked.connect(self.show_homepage)

        # Create table view and set model
        self.table_view = QTableView()
        self.model = QStandardItemModel()
        self.table_view.setModel(self.model)

        # Set column headers of table and disable vertical headers
        cols = show_products()[0]
        self.model.setHorizontalHeaderLabels(cols)
        self.table_view.verticalHeader().setVisible(False)

        # Set width of  cells
        for col in range(len(cols)):
            self.table_view.setColumnWidth(col, 200)

        # Get rows and insert equivalent amount of empty rows into table
        rows = show_products()[1]
        self.model.insertRows(0, len(rows), QModelIndex())

        # Set empty rows to row data and center align their text
        for row, data in enumerate(rows):
            self.model.setItem(row, 0, QStandardItem(f"{rows[row][0]}"))
            self.model.setItem(row, 1, QStandardItem(f"{rows[row][1]}"))
            self.model.setItem(row, 2, QStandardItem(f"{rows[row][2]}"))
            self.model.setItem(row, 3, QStandardItem(f"{rows[row][3]}"))
            self.model.setItem(row, 4, QStandardItem(f"{rows[row][4]}"))
            self.model.setItem(row, 5, QStandardItem(f"{rows[row][5]}"))

            for col in range(len(cols)):
                index = self.model.index(row, col, QModelIndex())
                self.model.setData(index, Qt.AlignCenter, Qt.TextAlignmentRole)

        # Add table view and home button to main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.table_view)
        main_layout.addWidget(self.home_button)

        self.setLayout(main_layout)

    def show_homepage(self):
        """
        Close current window and open homepage
        :return: None
        """
        self.cams = HomepageWindow()
        self.cams.show()
        self.close()


class ViewOOSProductsWindow(QWidget):
    """
    Window for viewing out of stock products
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # Set window details
        self.setWindowTitle('View Out of Stock Products')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_DirClosedIcon))
        self.cams = None

        # Set window dimensions
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setGeometry(self.top, self.left, self.width, self.height)

        # Home Button
        self.home_button = QPushButton(self)
        self.home_button.setText('Return to Homepage')
        self.home_button.setGeometry(260, 450, 150, 30)
        self.home_button.clicked.connect(self.show_homepage)

        # Create table view and set model
        self.table_view = QTableView()
        self.model = QStandardItemModel()
        self.table_view.setModel(self.model)

        # Set column headers of table and disable vertical headers
        cols = show_out_of_stock_products()[0]
        self.model.setHorizontalHeaderLabels(cols)
        self.table_view.verticalHeader().setVisible(False)

        # Set width of table cells
        for col in range(len(cols)):
            self.table_view.setColumnWidth(col, 200)

        # Get rows and add equivalent amount empty rows
        rows = show_out_of_stock_products()[1]
        self.model.insertRows(0, len(rows), QModelIndex())

        # Set empty rows to row data and center their text
        for row, data in enumerate(rows):
            self.model.setItem(row, 0, QStandardItem(f"{rows[row][0]}"))
            self.model.setItem(row, 1, QStandardItem(f"{rows[row][1]}"))
            self.model.setItem(row, 2, QStandardItem(f"{rows[row][2]}"))
            self.model.setItem(row, 3, QStandardItem(f"{rows[row][3]}"))
            self.model.setItem(row, 4, QStandardItem(f"{rows[row][4]}"))
            self.model.setItem(row, 5, QStandardItem(f"{rows[row][5]}"))

            for col in range(len(cols)):
                index = self.model.index(row, col, QModelIndex())
                self.model.setData(index, Qt.AlignCenter, Qt.TextAlignmentRole)

        # Add table view and home button to main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.table_view)
        main_layout.addWidget(self.home_button)
        self.setLayout(main_layout)

    def show_homepage(self):
        """
        Close current window and open homepage
        :return: None
        """
        self.cams = HomepageWindow()
        self.cams.show()
        self.close()


class ViewRecentCustomers(QWidget):
    """
    Window for showing customers with activity within the last month
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # Set window details
        self.setWindowTitle('View Recent Customers')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_DirClosedIcon))
        self.cams = None

        # Set Window dimensions
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setGeometry(self.top, self.left, self.width, self.height)

        # Home Button
        self.home_button = QPushButton(self)
        self.home_button.setText('Return to Homepage')
        self.home_button.setGeometry(260, 450, 150, 30)
        self.home_button.clicked.connect(self.show_homepage)

        # Create table view and set model
        self.table_view = QTableView()
        self.model = QStandardItemModel()
        self.table_view.setModel(self.model)

        # Set column headers on table and disable vertical headers
        cols = get_customers_last_month()[0]
        self.model.setHorizontalHeaderLabels(cols)
        self.table_view.verticalHeader().setVisible(False)

        # Set width of cells in table
        for col in range(len(cols)):
            self.table_view.setColumnWidth(col, 200)

        # Get rows and add equivalent amount empty rows to table
        rows = get_customers_last_month()[1]
        self.model.insertRows(0, len(rows), QModelIndex())

        # Set empty rows to row data and center their text
        for row, data in enumerate(rows):
            self.model.setItem(row, 0, QStandardItem(f"{rows[row][0]}"))
            self.model.setItem(row, 1, QStandardItem(f"{rows[row][1]}"))
            self.model.setItem(row, 2, QStandardItem(f"{rows[row][2]}"))
            self.model.setItem(row, 3, QStandardItem(f"{rows[row][3]}"))

            for col in range(len(cols)):
                index = self.model.index(row, col, QModelIndex())
                self.model.setData(index, Qt.AlignCenter, Qt.TextAlignmentRole)

        # Add table view and home button to main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.table_view)
        main_layout.addWidget(self.home_button)
        self.setLayout(main_layout)

    def show_homepage(self):
        """
        Close current window and open homepage
        :return: None
        """
        self.cams = HomepageWindow()
        self.cams.show()
        self.close()


class AddCustomerWindow(QWidget):
    """
    Window for adding new customers to the database
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # Set window details
        self.setWindowTitle('Add Customer')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_DirClosedIcon))
        self.cams = None

        # Set window dimensions
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setGeometry(self.top, self.left, self.width, self.height)

        # Home button
        self.home_button = QPushButton(self)
        self.home_button.setText('Return to Homepage')
        self.home_button.setGeometry(260, 450, 150, 30)
        self.home_button.clicked.connect(self.show_homepage)

        # Add Customer button
        self.add_customer_button = QPushButton(self)
        self.add_customer_button.setText('Add Customer')
        self.add_customer_button.setGeometry(260, 450, 150, 30)
        self.add_customer_button.clicked.connect(self.add_customer)

        # Feedback label
        self.lbl_output = QLabel("")
        self.lbl_output.setAlignment(Qt.AlignCenter)
        self.lbl_output.setMaximumHeight(30)

        # Create main layout
        main_layout = QVBoxLayout()

        # Create user input fields for new customer
        self.cus_first_name = QLineEdit("", self)
        self.cus_last_name = QLineEdit("", self)
        self.cus_phone = QLineEdit("", self)
        self.cus_email = QLineEdit("", self)
        self.cus_address = QLineEdit("", self)

        # Create layout as row for first name widgets and add the row to the main layout
        first_name_row = QHBoxLayout()
        first_name_row.addWidget(QLabel("First Name: "))
        first_name_row.addWidget(self.cus_first_name)
        main_layout.addLayout(first_name_row)

        # Create layout as row for last name widgets and add the row to the main layout
        last_name_row = QHBoxLayout()
        last_name_row.addWidget(QLabel("Last Name: "))
        last_name_row.addWidget(self.cus_last_name)
        main_layout.addLayout(last_name_row)

        # Create layout as row for phone widgets and add the row to the main layout
        phone_row = QHBoxLayout()
        phone_row.addWidget(QLabel("Phone: "))
        phone_row.addWidget(self.cus_phone)
        main_layout.addLayout(phone_row)

        # Create layout as row for email widgets and add the row to the main layout
        email_row = QHBoxLayout()
        email_row.addWidget(QLabel("Email: "))
        email_row.addWidget(self.cus_email)
        main_layout.addLayout(email_row)

        # Create layout as row for address widgets and add the row to the main layout
        address_row = QHBoxLayout()
        address_row.addWidget(QLabel("Address: "))
        address_row.addWidget(self.cus_address)
        main_layout.addLayout(address_row)

        # Create layout as column for buttons and feedback and add the columns to the main layout
        button_col = QVBoxLayout()
        button_col.addWidget(self.lbl_output)
        button_col.addWidget(self.add_customer_button)
        button_col.addWidget(self.home_button)
        main_layout.addLayout(button_col)

        self.setLayout(main_layout)

    def show_homepage(self):
        """
        Close current window and open homepage
        :return: None
        """
        self.cams = HomepageWindow()
        self.cams.show()
        self.close()

    def add_customer(self):
        """
        Adds a new customer to the database using user input fields.
        :return: None
        """
        if self.cus_first_name.text() == "" or self.cus_last_name.text() == "" or self.cus_phone.text() == "" or self.cus_email.text() == "" or self.cus_address.text() == "":
            self.lbl_output.setText(f"All fields must be filled")
        else:
            add_customer(self.cus_first_name.text(), self.cus_last_name.text(), self.cus_phone.text(),
                         self.cus_email.text(), self.cus_address.text())
            self.lbl_output.setText(f"Successfully added {self.cus_first_name.text()}")


class StartTransactionWindow(QWidget):
    """
    Window for performing transactions
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # Set window details
        self.setWindowTitle('Start Transaction')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_DirClosedIcon))
        self.cams = None
        self.current_invoice_id = None
        self.current_customer_id = None

        # Set window dimensions
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setGeometry(self.top, self.left, self.width, self.height)

        # Home Button
        self.home_button = QPushButton(self)
        self.home_button.setText('Return to Homepage')
        self.home_button.clicked.connect(self.show_homepage)

        # Feedback label
        self.lbl_output = QLabel("")
        self.lbl_output.setAlignment(Qt.AlignCenter)
        self.lbl_output.setMaximumHeight(30)

        main_layout = QVBoxLayout()

        # Customer Selection widgets
        self.cus_cbo = QComboBox()
        self.cus_button = QPushButton("Select Customer")
        self.cus_button.clicked.connect(self.select_customer_on_click)

        # Add items to combo box
        self.cus_cbo.addItem('')
        row = get_customer_names()
        for i in row[1]:
            data = str(i[0])
            self.cus_cbo.addItem(data)

        # Add customer widgets to layout as row
        choose_customer_row = QHBoxLayout()
        choose_customer_row.addWidget(QLabel("Customer: "))
        choose_customer_row.addWidget(self.cus_cbo)
        choose_customer_row.addWidget(self.cus_button)

        # Product selection widgets
        self.prod_cbo = QComboBox()
        self.prod_button = QPushButton("Add Product ")
        self.prod_button.clicked.connect(self.select_product_on_click)
        self.prod_quantity_line = QLineEdit()
        self.prod_quantity_line.setFixedWidth(50)

        # Product selection disabled until customer picked
        self.prod_cbo.setEnabled(False)
        self.prod_button.setEnabled(False)
        self.prod_quantity_line.setEnabled(False)

        # Fill product combo box with data
        self.prod_cbo.addItem('')
        row = get_product_names()
        for i in row[1]:
            data = str(i[0])
            self.prod_cbo.addItem(data)

        # Add product widgets to layout as row
        choose_product_row = QHBoxLayout()
        choose_product_row.addWidget(QLabel("Product: "))
        choose_product_row.addWidget(self.prod_cbo)
        choose_product_row.addWidget(self.prod_quantity_line)
        choose_product_row.addWidget(self.prod_button)

        # Finish transaction button
        self.btn_complete_invoice = QPushButton(self)
        self.btn_complete_invoice.setText('Complete Transaction')
        self.btn_complete_invoice.clicked.connect(self.btn_complete_invoice_on_click)
        self.btn_complete_invoice.setEnabled(False)

        # Show invoice button
        self.btn_show_invoice = QPushButton(self)
        self.btn_show_invoice.setText('Show Invoice')
        self.btn_show_invoice.clicked.connect(self.btn_show_invoice_on_click)
        self.btn_show_invoice.setEnabled(False)

        # Add customer and product row to main layout
        main_layout.addLayout(choose_customer_row)
        main_layout.addLayout(choose_product_row)

        # Add feedback label and buttons
        main_layout.addWidget(self.lbl_output)
        main_layout.addWidget(self.btn_complete_invoice)
        main_layout.addWidget(self.btn_show_invoice)
        main_layout.addWidget(self.home_button)

        self.setLayout(main_layout)

    def show_homepage(self):
        """
        Close current window and open homepage
        :return: None
        """
        self.cams = HomepageWindow()
        self.cams.show()
        self.close()

    def select_customer_on_click(self):
        """
        On click method for the select customer button to set the customer of the current invoice.
        Enables product selection row
        :return: None
        """
        if self.cus_cbo.currentText() == '':
            self.lbl_output.setText('Customer choice cannot be empty!')
        else:
            self.prod_cbo.setEnabled(True)
            self.prod_button.setEnabled(True)
            self.prod_quantity_line.setEnabled(True)
            self.btn_complete_invoice.setEnabled(True)

            cus_id = get_customer_by_name(self.cus_cbo.currentText())[1][0][0]
            self.current_customer_id = cus_id
            add_invoice(cus_id, 'NOW()')
            self.current_invoice_id = get_most_recent_invoice_id_by_date()
            self.cus_cbo.setEnabled(False)
            self.cus_button.setEnabled(False)

            self.lbl_output.setText(f"Transaction started for {self.cus_cbo.currentText()}")

    def select_product_on_click(self):
        """
        On click method for the select product button to add products to the current invoice.
        :return: None
        """
        # Check for empty combo box
        if self.prod_cbo.currentText() == '':
            self.lbl_output.setText('Product choice cannot be empty!')
        else:
            prod_id = get_product_id(self.prod_cbo.currentText())
            # Check for empty or invalid quantity
            if self.prod_quantity_line.text() == "" or not self.prod_quantity_line.text().isdigit():
                self.lbl_output.setText("Quantity must be a number and cannot be empty!")
            else:
                # Check if product already in invoice, if so increase quantity
                if check_if_invoice_product_exists(self.current_invoice_id, prod_id):
                    increase_invoice_product_inventory(self.prod_quantity_line.text(), self.current_invoice_id, prod_id)
                else:
                    # Check if the product has available stock to match desired quantity
                    current_inventory_count = get_product_quantity_by_id(prod_id)[0][1]
                    if current_inventory_count < int(self.prod_quantity_line.text()):
                        self.lbl_output.setText(
                            f"{self.prod_cbo.currentText()} is currently out of stock and cannot be added")
                    else:
                        # Add product to invoice and decrease its stock based on quantity
                        add_product_to_invoice_products(self.current_invoice_id, prod_id,
                                                        self.prod_quantity_line.text())
                        decrease_inventory(self.prod_quantity_line.text(), prod_id)
                        self.lbl_output.setText(
                            f"{self.prod_quantity_line.text()}x {self.prod_cbo.currentText()} Added to Transaction")

    def btn_complete_invoice_on_click(self):
        """
        On click method for the complete invoice button to finish the current invoice.
        Enables show invoice button
        :return: None
        """
        self.btn_complete_invoice.setEnabled(False)
        self.prod_cbo.setEnabled(False)
        self.prod_button.setEnabled(False)
        self.prod_quantity_line.setEnabled(False)
        self.btn_show_invoice.setEnabled(True)
        self.lbl_output.setText(f"Transaction Closed for {self.cus_cbo.currentText()}, Invoice Generated")

    def btn_show_invoice_on_click(self):
        """
        On click method for the show invoice button to open the current invoice window
        :return: None
        """
        self.cams = ViewCurrentInvoiceWindow(self.current_invoice_id)
        self.cams.show()


class ViewCurrentInvoiceWindow(QWidget):
    """
    Window for viewing invoice generated by complete transaction
    """
    def __init__(self, current_invoice, parent=None):
        super().__init__(parent)
        # Set Window Info
        self.setWindowTitle('View Current Invoice')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_DirClosedIcon))
        self.cams = None

        # Set Window Dimensions
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setGeometry(self.top, self.left, self.width, self.height)

        # Inherit current invoice id from Transaction Window
        self.current_invoice_id = current_invoice

        # Return Button
        self.pushButton = QPushButton(self)
        self.pushButton.setText('Close')
        self.pushButton.setGeometry(260, 450, 150, 30)
        self.pushButton.clicked.connect(self.close_page)

        # Create table view and set model
        self.table_view = QTableView()
        self.model = QStandardItemModel()
        self.table_view.setModel(self.model)

        # Set get column headers and set them to the table
        cols = show_current_invoice(self.current_invoice_id)[0]
        self.model.setHorizontalHeaderLabels(cols)

        # Disable vertical headers
        self.table_view.verticalHeader().setVisible(False)

        # Set width of column cells
        for col in range(len(cols)):
            self.table_view.setColumnWidth(col, 200)

        # Get row data
        rows = show_current_invoice(self.current_invoice_id)[1]

        # Insert empty rows to be filled
        self.model.insertRows(0, len(rows) + 1, QModelIndex())

        # Fill row cells  with data and center their text
        for row, data in enumerate(rows):
            self.model.setItem(row, 0, QStandardItem(f"{rows[row][0]}"))
            self.model.setItem(row, 1, QStandardItem(f"{rows[row][1]}"))
            self.model.setItem(row, 2, QStandardItem(f"{rows[row][2]}"))
            self.model.setItem(row, 3, QStandardItem(f"{rows[row][3]}"))

            for col in range(len(cols)):
                index = self.model.index(row, col, QModelIndex())
                self.model.setData(index, Qt.AlignCenter, Qt.TextAlignmentRole)

        # Fill summary row data
        self.model.setItem(len(rows), 0, QStandardItem("Total:"))
        self.model.setItem(len(rows), 2, QStandardItem(f"{get_current_invoice_quantity(self.current_invoice_id)}"))
        self.model.setItem(len(rows), 3, QStandardItem(f"{get_current_invoice_total(self.current_invoice_id)}"))

        # Center align summary row text
        index1 = self.model.index(len(rows), 0, QModelIndex())
        self.model.setData(index1, Qt.AlignCenter, Qt.TextAlignmentRole)
        index2 = self.model.index(len(rows), 2, QModelIndex())
        self.model.setData(index2, Qt.AlignCenter, Qt.TextAlignmentRole)
        index3 = self.model.index(len(rows), 3, QModelIndex())
        self.model.setData(index3, Qt.AlignCenter, Qt.TextAlignmentRole)

        # Create main layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.table_view)
        layout.addWidget(self.pushButton)
        self.setLayout(layout)

    def close_page(self):
        """
        Closes the current window
        :return: None
        """
        self.close()


class AddStockWindow(QWidget):
    """
    Window for increasing stock of products
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set Title and Icon
        self.setWindowTitle('Add Stock')
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_DirClosedIcon))

        # Set window dimensions
        self.cams = None
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setGeometry(self.top, self.left, self.width, self.height)

        # Home Button
        self.home_button = QPushButton(self)
        self.home_button.setText('Return to Homepage')
        self.home_button.setGeometry(260, 450, 150, 30)
        self.home_button.clicked.connect(self.show_homepage)

        # Product Row
        self.prod_cbo = QComboBox()
        self.prod_button = QPushButton("Add Product ")
        self.prod_button.clicked.connect(self.select_product_on_click)
        self.prod_quantity_line = QLineEdit()
        self.prod_quantity_line.setFixedWidth(50)

        # Feedback Label
        self.lbl_feedback = QLabel()
        self.lbl_feedback.setAlignment(Qt.AlignCenter)
        self.lbl_feedback.setMaximumHeight(30)

        # Fill product combo box
        self.prod_cbo.addItem('')
        row = get_product_names()
        for i in row[1]:
            data = str(i[0])
            self.prod_cbo.addItem(data)

        # Create product row layout and add product widgets
        product_row = QHBoxLayout()
        product_row.addWidget(self.prod_cbo)
        product_row.addWidget(self.prod_quantity_line)
        product_row.addWidget(self.prod_button)

        # Create main layout and add table and return button
        main_layout = QVBoxLayout()
        main_layout.addLayout(product_row)
        main_layout.addWidget(self.lbl_feedback)
        main_layout.addWidget(self.home_button)

        self.setLayout(main_layout)

    def show_homepage(self):
        """
        Close current window and open homepage
        :return: None
        """
        self.cams = HomepageWindow()
        self.cams.show()
        self.close()

    def select_product_on_click(self):
        """
        Get current product id and use it to increase inventory
        :return: None
        """
        # Check for empty combo box choice
        if self.prod_cbo.currentText() == '':
            self.lbl_feedback.setText('Product choice cannot be empty!')
        else:
            # Check for empty or invalid quantity
            if self.prod_quantity_line.text() == "" or not self.prod_quantity_line.text().isdigit():
                self.lbl_feedback.setText("Quantity must be a number and cannot be empty!")
            else:
                # Increase stock of selected product
                current_product = get_product_id(self.prod_cbo.currentText())
                increase_inventory(self.prod_quantity_line.text(), current_product)
                self.lbl_feedback.setText(f"Added {self.prod_quantity_line.text()} {self.prod_cbo.currentText()}")


if __name__ == '__main__':
    # Start App
    app = QApplication(sys.argv)

    # Apply styles
    qss = "styles.qss"
    with open(qss, "r") as fh:
        app.setStyleSheet(fh.read())

    # Initialize Homepage
    ex = HomepageWindow()

    # Close app
    sys.exit(app.exec_())
