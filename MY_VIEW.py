import sys
from controller import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class HomepageWindow(QMainWindow):
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
        btn_view_products.move(300, 100)
        btn_view_products.clicked.connect(self.btn_view_products_on_click)

        btn_add_customer = QPushButton('Add Customer', self)
        btn_add_customer.move(300, 200)
        btn_add_customer.clicked.connect(self.btn_add_customer_on_click)

        btn_start_transaction = QPushButton('Start Transaction', self)
        btn_start_transaction.move(300, 300)
        btn_start_transaction.clicked.connect(self.btn_start_transaction_on_click)

        self.show()

    def btn_view_products_on_click(self):
        self.cams = ViewProductsWindow()
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

        for col in range(len(cols)):
            self.table_view.setColumnWidth(col, 200)

        rows = show_products()[1]

        self.model.insertRows(0, len(rows), QModelIndex())

        for row, data in enumerate(rows):
            self.model.setItem(row, 0, QStandardItem(rows[row][0]))
            self.model.setItem(row, 1, QStandardItem(f"{rows[row][1]}"))
            self.model.setItem(row, 2, QStandardItem(f"{rows[row][2]}"))
            self.model.setItem(row, 3, QStandardItem(f"{rows[row][3]}"))
            self.model.setItem(row, 4, QStandardItem(f"{rows[row][4]}"))
            self.model.setItem(row, 5, QStandardItem(f"{rows[row][5]}"))

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

        main_layout = QVBoxLayout()

        self.cus_fname = QLineEdit("", self)
        self.cus_lname = QLineEdit("", self)
        self.cus_phone = QLineEdit("", self)
        self.cus_email = QLineEdit("", self)
        self.cus_address = QLineEdit("", self)

        fname_row = QHBoxLayout()
        fname_row.addWidget(QLabel("First Name: "))
        fname_row.addWidget(self.cus_fname)
        main_layout.addLayout(fname_row)

        lname_row = QHBoxLayout()
        lname_row.addWidget(QLabel("Last Name: "))
        lname_row.addWidget(self.cus_lname)
        main_layout.addLayout(lname_row)

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

        main_layout.addWidget(self.addCustomerButton)
        main_layout.addWidget(self.homeButton)
        self.setLayout(main_layout)

    def show_homepage(self):
        self.cams = HomepageWindow()
        self.cams.show()
        self.close()

    def add_customer(self):
        add_customer(self.cus_fname.text(), self.cus_lname.text(), self.cus_phone.text(), self.cus_email.text(),
                     self.cus_address.text())


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
        self.home_button.setGeometry(260, 450, 150, 30)
        self.home_button.clicked.connect(self.show_homepage)

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



        main_layout.addLayout(choose_customer_row)
        main_layout.addLayout(choose_product_row)
        main_layout.addWidget(self.home_button)

        self.setLayout(main_layout)

    def show_homepage(self):
        self.cams = HomepageWindow()
        self.cams.show()
        self.close()

    def select_customer_on_click(self):
        self.prod_cbo.setEnabled(True)
        self.prod_button.setEnabled(True)
        self.prod_quantity_line.setEnabled(True)
        cus_id = get_customer_by_name(self.cus_cbo.currentText())[1][0][0]
        self.current_customer_id = cus_id
        add_invoice(cus_id, 'NOW()')
        self.current_invoice_id = get_most_recent_invoice_id_by_date()
        self.cus_cbo.setEnabled(False)
        self.cus_button.setEnabled(False)

    def select_product_on_click(self):
        prod_id = get_product_id(self.prod_cbo.currentText())
        if self.prod_quantity_line.text() == '':
            self.prod_quantity_line.setText('1')
        if check_if_invoice_product_exists(self.current_invoice_id, prod_id):
            increase_invoice_product_inventory(self.prod_quantity_line.text(), self.current_invoice_id, prod_id)
        else:
            add_product_to_invoice_products(self.current_invoice_id, prod_id, self.prod_quantity_line.text())
            decrease_inventory(self.prod_quantity_line.text(), prod_id)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HomepageWindow()
    sys.exit(app.exec_())
