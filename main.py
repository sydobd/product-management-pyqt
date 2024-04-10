import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Manger")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450, 150, 1350, 750)
        self.setFixedSize(self.size())

        self.UI()
        self.show()

    def UI(self):
        self.toolBar()
        self.tabWidget()
        self.widgets()
        self.layouts()

    def toolBar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        # Toolbar #
        # Add product #
        self.addProduct = QAction(QIcon('icons/add.png'), "Add Product",self)
        self.tb.addAction(self.addProduct)
        self.tb.addSeparator()

        # Add Member #
        self.addMember = QAction(QIcon('icons/users.png'), "Add Member", self)
        self.tb.addAction(self.addMember)
        self.tb.addSeparator()

        # Sell Product #
        self.sellProduct = QAction(QIcon('icons/sell.png'), "Sell Product", self)
        self.tb.addAction(self.sellProduct)
        self.tb.addSeparator()

    def tabWidget(self):
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs) #tabs will not be displayed if not use this
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab1, "Products")
        self.tabs.addTab(self.tab2, "Members")
        self.tabs.addTab(self.tab3, "Statistics")

    def widgets(self):
        # Tab1 #
        # left layout widget #
        self.productsTable = QTableWidget()
        self.productsTable.setColumnCount(6)
        self.productsTable.setColumnHidden(0, True) #product Id column
        self.productsTable.setHorizontalHeaderItem(0, QTableWidgetItem("Product ID"))
        self.productsTable.setHorizontalHeaderItem(1, QTableWidgetItem("Product Name"))
        self.productsTable.setHorizontalHeaderItem(2, QTableWidgetItem("Manufacturer"))
        self.productsTable.setHorizontalHeaderItem(3, QTableWidgetItem("Price"))
        self.productsTable.setHorizontalHeaderItem(4, QTableWidgetItem("Qouta"))
        self.productsTable.setHorizontalHeaderItem(5, QTableWidgetItem("Availability"))
        # right layout widget #
        self.searchText = QLabel("Search")
        self.searchEntry = QLineEdit()
        self.searchEntry.setPlaceholderText("Search for products")
        self.searchButton = QPushButton("Search")
        self.allProducts = QRadioButton("All Products")
        self.availableProducts = QRadioButton("Available")
        self.notAvailableProducts = QRadioButton("Not Available")
        self.listButton = QPushButton("List")

    def layouts(self):
        # Tab 1 #
        self.mainLayout = QHBoxLayout()
        self.mainLeftLayout = QVBoxLayout()
        self.mainRightLayout = QVBoxLayout()
        self.rightTopLayout = QHBoxLayout()
        self.rightMiddleLayout = QHBoxLayout()
        self.topGroupBox = QGroupBox("Search Box")
        self.middleGroupBox = QGroupBox("List Box")
        # left layout widget #
        self.mainLeftLayout.addWidget(self.productsTable)

        # right top layout widget #
        self.rightTopLayout.addWidget(self.searchText)
        self.rightTopLayout.addWidget(self.searchEntry)
        self.rightTopLayout.addWidget(self.searchButton)
        self.topGroupBox.setLayout(self.rightTopLayout)
        self.rightMiddleLayout.addWidget(self.allProducts)
        self.rightMiddleLayout.addWidget(self.availableProducts)
        self.rightMiddleLayout.addWidget(self.notAvailableProducts)
        self.rightMiddleLayout.addWidget(self.listButton)
        self.middleGroupBox.setLayout(self.rightMiddleLayout)

        self.mainRightLayout.addWidget(self.topGroupBox)
        self.mainRightLayout.addWidget(self.middleGroupBox)
        self.mainLayout.addLayout(self.mainLeftLayout, 70)
        self.mainLayout.addLayout(self.mainRightLayout, 30)
        self.tab1.setLayout(self.mainLayout)  # tabs behaves is main window

def main():
    App = QApplication(sys.argv)
    window = Main()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()