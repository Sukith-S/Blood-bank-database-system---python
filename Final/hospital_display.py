import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import re

class HospitalData(QWidget):
    def __init__(self, parent=None):
        super(HospitalData, self).__init__(parent)
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
        self.tableView.setStyleSheet("background:qconicalgradient(cx:1, cy:0, angle:0, stop:0.204545 rgba(68, 0, 255, 255), stop:0.596591 rgba(255, 243, 243, 255))")
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.tableView)
        self.setLayout(self.layout)
        self.setWindowTitle("HospitalData")
        self.resize(1000, 450)
        self.setMinimumSize(1000,450)
    def initializedModel(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("project.db")
        if not self.db.open():
            return False
        self.queryModel.setHeaderData(0, Qt.Horizontal, "Hospital Name")
        self.queryModel.setHeaderData(1, Qt.Horizontal, "Address")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "City")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "State")
        self.queryModel.setHeaderData(3, Qt.Horizontal, "Contact Details")

        
        # Get all the records of the table
        sql = "SELECT * FROM hospital"
        self.queryModel.setQuery(sql, self.db)
        self.totalRecordCount = self.queryModel.rowCount()

    def closeEvent(self,event):
        self.db.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HospitalData()
    window.show()
    sys.exit(app.exec_())


