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

        buttonWindow1 = QPushButton('Window1', self)
        buttonWindow1.move(300, 100)
        buttonWindow1.clicked.connect(self.buttonWindow1_onClick)

        buttonWindow2 = QPushButton('Window2', self)
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

        self.model.setItem(0, 0, QStandardItem("Alice"))
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
        self.setLayout(layout)

    def goMainWindow(self):
        self.cams = Window()
        self.cams.show()
        self.close()


class Window2(QMainWindow):
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


class Window3(QMainWindow):
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
