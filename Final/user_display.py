import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import re

class UserData(QWidget):
    def __init__(self, parent=None):
        super(UserData, self).__init__(parent)
        # Declare Database Connections
        self.db = None
        # Layout Manager
        self.layout = QVBoxLayout()
        # Query Model
        self.queryModel = QSqlQueryModel()
        # Table View
        self.tableView = QTableView()
        self.tableView.setModel(self.queryModel)

        self.initUI()
        self.initializedModel()


    def initUI(self):
        self.tableView.setStyleSheet(u"background:qconicalgradient(cx:1, cy:0, angle:0, stop:0.204545 rgba(255, 0, 194, 255), stop:0.6875 rgba(255, 243, 243, 255))")
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.tableView)
        self.setLayout(self.layout)
        self.setWindowTitle("UserData")
        self.resize(1000, 450)
        self.setMinimumSize(1000,450)
    def initializedModel(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("project.db")
        if not self.db.open():
            return False
        self.queryModel.setHeaderData(0, Qt.Horizontal, "First Name")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "Last Name")
        self.queryModel.setHeaderData(2, Qt.Horizontal, "DOB")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "Gender")
        self.queryModel.setHeaderData(4, Qt.Horizontal, "State")
        self.queryModel.setHeaderData(5, Qt.Horizontal, "Blood Group")
        self.queryModel.setHeaderData(6, Qt.Horizontal, "Mobile")
        self.queryModel.setHeaderData(7, Qt.Horizontal, "Email ID")
        self.queryModel.setHeaderData(8, Qt.Horizontal, "Donation Details")
        self.queryModel.setHeaderData(9, Qt.Horizontal, "Medical Details")
        self.queryModel.setHeaderData(10, Qt.Horizontal, "Username")
        self.queryModel.setHeaderData(11, Qt.Horizontal, "Password")
        
        # Get all the records of the table
        sql = "SELECT * FROM user"
        self.queryModel.setQuery(sql, self.db)
        self.totalRecordCount = self.queryModel.rowCount()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserData()
    window.show()
    sys.exit(app.exec_())


