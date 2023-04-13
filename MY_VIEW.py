import sys
from controller import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cams = None
        self.title = "App"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowIcon(self.style().standardIcon(QStyle.SP_DirClosedIcon))

        buttonWindow1 = QPushButton('View Products', self)
        buttonWindow1.move(300, 100)
        buttonWindow1.clicked.connect(self.buttonWindow1_onClick)

        buttonWindow2 = QPushButton('Add Customer', self)
        buttonWindow2.move(300, 200)
        buttonWindow2.clicked.connect(self.buttonWindow2_onClick)

        buttonWindow3 = QPushButton('Window3', self)
        buttonWindow3.move(300, 300)
        buttonWindow3.clicked.connect(self.buttonWindow3_onClick)

        self.show()

    def buttonWindow1_onClick(self):
        self.statusBar().showMessage("Switched to window 1")
        self.cams = Window1()
        self.cams.show()
        self.close()

    def buttonWindow2_onClick(self):
        self.statusBar().showMessage("Switched to window 2")
        self.cams = Window2()
        self.cams.show()
        self.close()

    def buttonWindow3_onClick(self):
        self.statusBar().showMessage("Switched to window 3")
        self.cams = Window3()
        self.cams.show()
        self.close()


class Window1(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Window1')

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
        self.pushButton.clicked.connect(self.goMainWindow)

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

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()


class Window2(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Window2')

        self.cams = None
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setGeometry(self.top, self.left, self.width, self.height)

        #Return to home
        self.homeButton = QPushButton(self)
        self.homeButton.setText('Return to Homepage')
        self.homeButton.setGeometry(260, 450, 150, 30)
        self.homeButton.clicked.connect(self.goMainWindow)

        self.addCustomerButton = QPushButton(self)
        self.addCustomerButton.setText('Add Customer')
        self.addCustomerButton.setGeometry(260, 450, 150, 30)
        self.addCustomerButton.clicked.connect(self.addCustomer)

        mainLayout = QVBoxLayout()
        # self.cus_fname_lbl = QLabel("First Name: ")
        # self.cus_lname_lbl = QLabel("Last Name: ")
        # self.cus_phone_lbl = QLabel("Phone: ")
        # self.cus_email_lbl = QLabel("Email: ")
        # self.cus_address_lbl = QLabel("Address: ")
        #
        self.cus_fname = QLineEdit("", self)
        self.cus_lname = QLineEdit("", self)
        self.cus_phone = QLineEdit("", self)
        self.cus_email = QLineEdit("", self)
        self.cus_address = QLineEdit("", self)

        fname_row = QHBoxLayout()
        fname_row.addWidget(QLabel("First Name: "))
        fname_row.addWidget(self.cus_fname)
        mainLayout.addLayout(fname_row)

        lname_row = QHBoxLayout()
        lname_row.addWidget(QLabel("Last Name: "))
        lname_row.addWidget(self.cus_lname)
        mainLayout.addLayout(lname_row)

        phone_row = QHBoxLayout()
        phone_row.addWidget(QLabel("Phone: "))
        phone_row.addWidget(self.cus_phone)
        mainLayout.addLayout(phone_row)

        email_row = QHBoxLayout()
        email_row.addWidget(QLabel("Email: "))
        email_row.addWidget(self.cus_email)
        mainLayout.addLayout(email_row)

        address_row = QHBoxLayout()
        address_row.addWidget(QLabel("Address: "))
        address_row.addWidget(self.cus_address)
        mainLayout.addLayout(address_row)

        mainLayout.addWidget(self.addCustomerButton)
        mainLayout.addWidget(self.homeButton)
        self.setLayout(mainLayout)

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()

    def addCustomer(self):
        add_customer(self.cus_fname.text(), self.cus_lname.text(), self.cus_phone.text(), self.cus_email.text(), self.cus_address.text())


class Window3(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Window1')

        self.cams = None
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.button = QPushButton()
        self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.button.setIcon(self.style().standardIcon(QStyle.SP_ArrowLeft))
        self.button.setIconSize(QSize(200, 200))

        self.pushButton = QPushButton(self)
        self.pushButton.setText('Return to Homepage')
        self.pushButton.setGeometry(260, 450, 150, 30)
        self.pushButton.clicked.connect(self.goMainWindow)

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
