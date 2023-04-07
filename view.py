import sys
import controller
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, \
    QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

widgets = {
    "buttons": {}
}


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("{Point of Sale")
window.setFixedWidth(1000)
window.setFixedHeight(500)
# window.setStyleSheet("background:black;")

grid = QGridLayout()


def homepage():

    button_inventory = QPushButton("Inventory")
    button_inventory.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button_inventory.setStyleSheet("border: 4px solid white;" + "color:white;")
    widgets["buttons"]["inventory"] = button_inventory
    grid.addWidget(button_inventory, 0, 0)

    Transaction = QPushButton("Transaction")
    Transaction.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    Transaction.setStyleSheet("border: 4px solid white;" + "color:white;")
    widgets["buttons"]["Transaction"] = Transaction
    grid.addWidget(Transaction, 1, 0)

    customer = QPushButton("customer")
    customer.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    customer.setStyleSheet("border: 4px solid white;" + "color:white;")
    widgets["buttons"]["customer"] = customer
    grid.addWidget(customer, 2, 0)
def inventory_page():
    row = 0
    table = QTableWidget()
    table.column()
    table.insertRow()
    table.insertColumn()

    grid.addWidget(table, 0, 0)

    datos = controller.show_products()[1]
    for endian in datos:
        table.setRowCount(row + 1)

        idDato = QTableWidgetItem(endian[0])
        idDato.setTextAlignment(4)

        table.setItem(row, 0, idDato)
        table.setItem(row, 1, QTableWidgetItem(endian[1]))
        table.setItem(row, 2, QTableWidgetItem(endian[2]))
        table.setItem(row, 3, QTableWidgetItem(endian[3]))
        table.setItem(row, 4, QTableWidgetItem(endian[4]))
        table.setItem(row, 5, QTableWidgetItem(str(endian[5])))

        row += 1

inventory_page()



window.setLayout(grid)

window.show()

sys.exit(app.exec())






