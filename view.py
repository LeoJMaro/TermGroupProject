import sys
from controller import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class HomepageWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.cams = None
        self.title = "App"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.initialize_windows()

    def initialize_windows(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_DirClosedIcon))

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

        main_layout = QVBoxLayout()
        main_layout.addWidget(btn_view_products)
        main_layout.addWidget(btn_view_oos_products)
        main_layout.addWidget(btn_view_recent_customers)
        main_layout.addWidget(btn_add_customer)
        main_layout.addWidget(btn_start_transaction)

        self.setLayout(main_layout)

        self.show()

    def btn_view_products_on_click(self):
        self.cams = ViewProductsWindow()
        self.cams.show()
        self.close()

    def btn_view_out_of_stock_products_on_click(self):
        self.cams = ViewOOSProductsWindow()
        self.cams.show()
        self.close()

    def btn_view_recent_customers_on_click(self):
        self.cams = ViewRecentCustomers()
        self.cams.show()
        self.close()

    def btn_add_customer_on_click(self):
        self.cams = AddCustomerWindow()
        self.cams.show()
        self.close()

    def btn_start_transaction_on_click(self):
        self.cams = StartTransactionWindow()
        self.cams.show()
        self.close()


class ViewProductsWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('View Products')

        self.cams = None
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setGeometry(self.top, self.left, self.width, self.height)

        # Return Button
        self.pushButton = QPushButton(self)
        self.pushButton.setText('Return to Homepage')
        self.pushButton.setGeometry(260, 450, 150, 30)
        self.pushButton.clicked.connect(self.show_homepage)

        # create table view and set model
        self.table_view = QTableView()
        self.model = QStandardItemModel()
        self.table_view.setModel(self.model)

        cols = show_products()[0]

        self.model.setHorizontalHeaderLabels(cols)
        self.table_view.verticalHeader().setVisible(False)

        for col in range(len(cols)):
            self.table_view.setColumnWidth(col, 200)

        rows = show_products()[1]

        self.model.insertRows(0, len(rows), QModelIndex())

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

        # add table view to layout
        layout = QVBoxLayout()
        layout.addWidget(self.table_view)
        layout.addWidget(self.pushButton)
        self.setLayout(layout)

    def show_homepage(self):
        self.cams = HomepageWindow()
        self.cams.show()
        self.close()


class ViewOOSProductsWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('View Out of Stock Products')

        self.cams = None
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setGeometry(self.top, self.left, self.width, self.height)

        # Return Button
        self.pushButton = QPushButton(self)
        self.pushButton.setText('Return to Homepage')
        self.pushButton.setGeometry(260, 450, 150, 30)
        self.pushButton.clicked.connect(self.show_homepage)

        # create table view and set model
        self.table_view = QTableView()
        self.model = QStandardItemModel()
        self.table_view.setModel(self.model)

        cols = show_out_of_stock_products()[0]

        self.model.setHorizontalHeaderLabels(cols)
        self.table_view.verticalHeader().setVisible(False)

        for col in range(len(cols)):
            self.table_view.setColumnWidth(col, 200)

        rows = show_out_of_stock_products()[1]

        self.model.insertRows(0, len(rows), QModelIndex())

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


        # add table view to layout
        layout = QVBoxLayout()
        layout.addWidget(self.table_view)
        layout.addWidget(self.pushButton)
        self.setLayout(layout)

    def show_homepage(self):
        self.cams = HomepageWindow()
        self.cams.show()
        self.close()


class ViewRecentCustomers(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('View Recent Customers')

        self.cams = None
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setGeometry(self.top, self.left, self.width, self.height)

        # Return Button
        self.pushButton = QPushButton(self)
        self.pushButton.setText('Return to Homepage')
        self.pushButton.setGeometry(260, 450, 150, 30)
        self.pushButton.clicked.connect(self.show_homepage)

        # create table view and set model
        self.table_view = QTableView()
        self.model = QStandardItemModel()
        self.table_view.setModel(self.model)

        cols = get_customers_last_month()[0]

        self.model.setHorizontalHeaderLabels(cols)
        self.table_view.verticalHeader().setVisible(False)

        for col in range(len(cols)):
            self.table_view.setColumnWidth(col, 200)

        rows = get_customers_last_month()[1]

        self.model.insertRows(0, len(rows), QModelIndex())

        for row, data in enumerate(rows):
            self.model.setItem(row, 0, QStandardItem(f"{rows[row][0]}"))
            self.model.setItem(row, 1, QStandardItem(f"{rows[row][1]}"))
            self.model.setItem(row, 2, QStandardItem(f"{rows[row][2]}"))
            self.model.setItem(row, 3, QStandardItem(f"{rows[row][3]}"))

            for col in range(len(cols)):
                index = self.model.index(row, col, QModelIndex())
                self.model.setData(index, Qt.AlignCenter, Qt.TextAlignmentRole)


        # add table view to layout
        layout = QVBoxLayout()
        layout.addWidget(self.table_view)
        layout.addWidget(self.pushButton)
        self.setLayout(layout)

    def show_homepage(self):
        self.cams = HomepageWindow()
        self.cams.show()
        self.close()


class AddCustomerWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Add Customer')

        self.cams = None
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setGeometry(self.top, self.left, self.width, self.height)

        # Return to home
        self.homeButton = QPushButton(self)
        self.homeButton.setText('Return to Homepage')
        self.homeButton.setGeometry(260, 450, 150, 30)
        self.homeButton.clicked.connect(self.show_homepage)

        self.addCustomerButton = QPushButton(self)
        self.addCustomerButton.setText('Add Customer')
        self.addCustomerButton.setGeometry(260, 450, 150, 30)
        self.addCustomerButton.clicked.connect(self.add_customer)

        self.lbl_output = QLabel("")
        self.lbl_output.setAlignment(Qt.AlignCenter)
        self.lbl_output.setMaximumHeight(30)

        main_layout = QVBoxLayout()

        self.cus_first_name = QLineEdit("", self)
        self.cus_last_name = QLineEdit("", self)

        self.cus_phone = QLineEdit("", self)
        self.cus_email = QLineEdit("", self)
        self.cus_address = QLineEdit("", self)


        first_name_row = QHBoxLayout()
        first_name_row.addWidget(QLabel("First Name: "))
        first_name_row.addWidget(self.cus_first_name)
        main_layout.addLayout(first_name_row)

        last_name_row = QHBoxLayout()
        last_name_row.addWidget(QLabel("Last Name: "))
        last_name_row.addWidget(self.cus_last_name)
        main_layout.addLayout(last_name_row)


        phone_row = QHBoxLayout()
        phone_row.addWidget(QLabel("Phone: "))
        phone_row.addWidget(self.cus_phone)
        main_layout.addLayout(phone_row)

        email_row = QHBoxLayout()
        email_row.addWidget(QLabel("Email: "))
        email_row.addWidget(self.cus_email)
        main_layout.addLayout(email_row)

        address_row = QHBoxLayout()
        address_row.addWidget(QLabel("Address: "))
        address_row.addWidget(self.cus_address)
        main_layout.addLayout(address_row)

        button_col = QVBoxLayout()
        button_col.addWidget(self.lbl_output)
        button_col.addWidget(self.addCustomerButton)
        button_col.addWidget(self.homeButton)
        main_layout.addLayout(button_col)

        self.setLayout(main_layout)

    def show_homepage(self):
        self.cams = HomepageWindow()
        self.cams.show()
        self.close()

    def add_customer(self):
        add_customer(self.cus_first_name.text(), self.cus_last_name.text(), self.cus_phone.text(),
                     self.cus_email.text(), self.cus_address.text())
        self.lbl_output.setText(f"Successfully added {self.cus_first_name.text()}")



class StartTransactionWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Start Transaction')

        self.cams = None
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.current_invoice_id = None
        self.current_customer_id = None

        # Home Button
        self.home_button = QPushButton(self)
        self.home_button.setText('Return to Homepage')
        self.home_button.clicked.connect(self.show_homepage)

        self.lbl_output = QLabel("")
        self.lbl_output.setAlignment(Qt.AlignCenter)
        self.lbl_output.setMaximumHeight(30)

        main_layout = QVBoxLayout()

        self.cus_cbo = QComboBox()
        self.cus_button = QPushButton("Select Customer")
        self.cus_button.clicked.connect(self.select_customer_on_click)

        self.cus_cbo.addItem('')
        row = get_customer_names()
        for i in row[1]:
            data = str(i[0])
            self.cus_cbo.addItem(data)

        choose_customer_row = QHBoxLayout()
        choose_customer_row.addWidget(QLabel("Customer: "))
        choose_customer_row.addWidget(self.cus_cbo)
        choose_customer_row.addWidget(self.cus_button)

        self.prod_cbo = QComboBox()
        self.prod_button = QPushButton("Add Product ")
        self.prod_button.clicked.connect(self.select_product_on_click)
        self.prod_quantity_line = QLineEdit()
        self.prod_quantity_line.setFixedWidth(50)

        self.prod_cbo.setEnabled(False)
        self.prod_button.setEnabled(False)
        self.prod_quantity_line.setEnabled(False)

        self.prod_cbo.addItem('')
        row = get_product_names()
        for i in row[1]:
            data = str(i[0])
            self.prod_cbo.addItem(data)

        choose_product_row = QHBoxLayout()
        choose_product_row.addWidget(QLabel("Product: "))
        choose_product_row.addWidget(self.prod_cbo)
        choose_product_row.addWidget(self.prod_quantity_line)
        choose_product_row.addWidget(self.prod_button)


        self.btn_complete_invoice = QPushButton(self)
        self.btn_complete_invoice.setText('Complete Invoice')
        self.btn_complete_invoice.clicked.connect(self.btn_complete_invoice_on_click)
        self.btn_complete_invoice.setEnabled(False)

        self.btn_show_invoice = QPushButton(self)
        self.btn_show_invoice.setText('Show Invoice')
        self.btn_show_invoice.clicked.connect(self.btn_show_invoice_on_click)
        self.btn_show_invoice.setEnabled(False)

        main_layout.addLayout(choose_customer_row)
        main_layout.addLayout(choose_product_row)

        main_layout.addWidget(self.lbl_output)
        main_layout.addWidget(self.btn_complete_invoice)
        main_layout.addWidget(self.btn_show_invoice)

        main_layout.addWidget(self.home_button)

        self.setLayout(main_layout)

    def show_homepage(self):
        self.cams = HomepageWindow()
        self.cams.show()
        self.close()

    def select_customer_on_click(self):
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
        if self.prod_cbo.currentText() == '':
            self.lbl_output.setText('Product choice cannot be empty!')
        else:
            prod_id = get_product_id(self.prod_cbo.currentText())
            if self.prod_quantity_line.text() == '':
                self.lbl_output.setText('Quantity choice cannot be empty!')
            else:
                if check_if_invoice_product_exists(self.current_invoice_id, prod_id):
                    increase_invoice_product_inventory(self.prod_quantity_line.text(), self.current_invoice_id, prod_id)
                else:
                    current_inventory_count = get_product_quantity_by_id(prod_id)[0][1]
                    print(current_inventory_count)
                    if current_inventory_count < int(self.prod_quantity_line.text()):
                        self.lbl_output.setText(f"{self.prod_cbo.currentText()} is currently out of stock and cannot be added")
                    else:
                        add_product_to_invoice_products(self.current_invoice_id, prod_id, self.prod_quantity_line.text())
                        decrease_inventory(self.prod_quantity_line.text(), prod_id)
                        self.lbl_output.setText(f"{self.prod_quantity_line.text()}x {self.prod_cbo.currentText()} Added to Transaction")

    def btn_complete_invoice_on_click(self):
        self.btn_complete_invoice.setEnabled(False)
        self.prod_cbo.setEnabled(False)
        self.prod_button.setEnabled(False)
        self.prod_quantity_line.setEnabled(False)
        self.btn_show_invoice.setEnabled(True)
        self.lbl_output.setText(f"Transaction Closed for {self.cus_cbo.currentText()}, Invoice Generated")

    def btn_show_invoice_on_click(self):
        self.cams = ViewCurrentInvoiceWindow(self.current_invoice_id)
        self.cams.show()


class ViewCurrentInvoiceWindow(QWidget):
    def __init__(self, current_invoice, parent=None):
        super().__init__(parent)
        self.setWindowTitle('View Current Invoice')

        self.cams = None
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.current_invoice_id = current_invoice

        # Return Button
        self.pushButton = QPushButton(self)
        self.pushButton.setText('Close')
        self.pushButton.setGeometry(260, 450, 150, 30)
        self.pushButton.clicked.connect(self.show_homepage)

        # create table view and set model
        self.table_view = QTableView()
        self.model = QStandardItemModel()
        self.table_view.setModel(self.model)

        cols = show_current_invoice(self.current_invoice_id)[0]

        self.model.setHorizontalHeaderLabels(cols)

        self.table_view.verticalHeader().setVisible(False)

        for col in range(len(cols)):
            self.table_view.setColumnWidth(col, 200)

        rows = show_current_invoice(self.current_invoice_id)[1]

        self.model.insertRows(0, len(rows), QModelIndex())

        for row, data in enumerate(rows):
            self.model.setItem(row, 0, QStandardItem(f"{rows[row][0]}"))
            self.model.setItem(row, 1, QStandardItem(f"{rows[row][1]}"))
            self.model.setItem(row, 2, QStandardItem(f"{rows[row][2]}"))
            self.model.setItem(row, 3, QStandardItem(f"{rows[row][3]}"))
            self.model.setItem(row, 4, QStandardItem(f"{rows[row][4]}"))

            for col in range(len(cols)):
                index = self.model.index(row, col, QModelIndex())
                self.model.setData(index, Qt.AlignCenter, Qt.TextAlignmentRole)

        # add table view to layout
        layout = QVBoxLayout()
        layout.addWidget(self.table_view)
        layout.addWidget(self.pushButton)
        self.setLayout(layout)

    def show_homepage(self):
        self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    qss = "styles.qss"
    with open(qss, "r") as fh:
        app.setStyleSheet(fh.read())
    ex = HomepageWindow()
    sys.exit(app.exec_())
