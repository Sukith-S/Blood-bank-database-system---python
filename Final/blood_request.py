# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blood_request.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import sqlite3
import re


class Ui_Request(object):
    def send(self):

        #Establish connection with database
        conn=sqlite3.connect("project.db")
        c=conn.cursor()

        #To input details
        name=str(self.receivername.text())
        citydata=str(self.city.text())
        phone=str(self.mobile.text())        

        #To input date
        bd=self.dob.date()
        bd=bd.toPyDate()
        bd=str(bd)

        #To input Gender
        if self.male.isChecked()==True:
            sex="Male"
        elif self.female.isChecked()==True:
            sex="Female"
        elif self.others.isChecked()==True:
            sex="Others"

        #To input state
        if self.state.currentIndex()==0:
            state="Andaman and Nicobar Islands"
        elif self.state.currentIndex()==1:
            state="Andhra Pradesh"
        elif self.state.currentIndex()==2:
            state="Arunachal Pradesh"
        elif self.state.currentIndex()==3:
            state="Assam"
        elif self.state.currentIndex()==4:
            state="Bihar"
        elif self.state.currentIndex()==5:
            state="Chandigarh"
        elif self.state.currentIndex()==6:
            state="Chhattisgarh"
        elif self.state.currentIndex()==7:
            state="Dadra and Nagar Haveli and Daman and Diu"
        elif self.state.currentIndex()==8:
            state="Delhi"
        elif self.state.currentIndex()==9:
            state="Goa"
        elif self.state.currentIndex()==10:
            state="Gujarat"
        elif self.state.currentIndex()==11:
            state="Haryana"
        elif self.state.currentIndex()==12:
            state="Himachal Pradesh"
        elif self.state.currentIndex()==13:
            state="Jammu and Kashmir"
        elif self.state.currentIndex()==14:
            state="Jharkhand"
        elif self.state.currentIndex()==15:
            state="Karnataka"
        elif self.state.currentIndex()==16:
            state="Kerala"
        elif self.state.currentIndex()==17:
            state="Ladakh"
        elif self.state.currentIndex()==18:
            state="Lakshadweep"
        elif self.state.currentIndex()==19:
            state="Madhya Pradesh"
        elif self.state.currentIndex()==20:
            state="Maharashtra"
        elif self.state.currentIndex()==21:
            state="Manipur"
        elif self.state.currentIndex()==22:
            state="Meghalaya"
        elif self.state.currentIndex()==23:
            state="Mizoram"
        elif self.state.currentIndex()==24:
            state="Nagaland"
        elif self.state.currentIndex()==25:
            state="Odisha"
        elif self.state.currentIndex()==26:
            state="Puducherry"
        elif self.state.currentIndex()==27:
            state="Punjab"
        elif self.state.currentIndex()==28:
            state="Rajasthan"
        elif self.state.currentIndex()==29:
            state="Sikkim"
        elif self.state.currentIndex()==30:
            state="Tamil Nadu"
        elif self.state.currentIndex()==31:
            state="Telangana"
        elif self.state.currentIndex()==32:
            state="Tripura"
        elif self.state.currentIndex()==33:
            state="Uttar Pradesh"
        elif self.state.currentIndex()==34:
            state="Uttarakhand"
        elif self.state.currentIndex()==35:
            state="West Bengal"
        
        
        #To check bloodgroup
        if self.bloodgroup.currentIndex()==0:
            bg="A+"
        elif self.bloodgroup.currentIndex()==1:
            bg="A-"
        elif self.bloodgroup.currentIndex()==2:
            bg="B+"
        elif self.bloodgroup.currentIndex()==3:
            bg="B-"
        elif self.bloodgroup.currentIndex()==4:
            bg="O+"
        elif self.bloodgroup.currentIndex()==5:
            bg="O-"
        elif self.bloodgroup.currentIndex()==6:
            bg="AB+"
        elif self.bloodgroup.currentIndex()==7:
            bg="AB-"

        #To print input data
        print(name,bd,sex,bg,citydata,state,phone)

        #To enter data into table
        c1="INSERT INTO requests VALUES (?,?,?,?,?,?,?)"
        c2=(name,bd,sex,bg,citydata,state,phone)
        c.execute(c1,c2)
        conn.commit()
        #self.label.setText("Welcome")
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Your request has been sent successfully.")
        msg.setWindowTitle("Request Sent")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()
        #Request.close()



    def setupUi(self, Request):
        Request.setObjectName("Request")
        Request.resize(600, 270)
        Request.setMaximumSize(600,270)
        Request.setMinimumSize(600,270)
        self.centralwidget = QtWidgets.QWidget(Request)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 600, 300))
        self.bg.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0, y1:0, x2:0.767, y2:0.857955, stop:0 rgba(0, 142, 227, 255), stop:1 rgba(255, 255, 255, 255))")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.formLayout_2 = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.receivername = QtWidgets.QLineEdit(self.centralwidget)
        self.receivername.setObjectName("receivername")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.receivername)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.male = QtWidgets.QRadioButton(self.centralwidget)
        self.male.setStyleSheet("font: 75 8pt \"Palatino Linotype\";")
        self.male.setObjectName("male")
        self.horizontalLayout.addWidget(self.male)
        self.female = QtWidgets.QRadioButton(self.centralwidget)
        self.female.setStyleSheet("font: 75 8pt \"Palatino Linotype\";")
        self.female.setObjectName("female")
        self.horizontalLayout.addWidget(self.female)
        self.others = QtWidgets.QRadioButton(self.centralwidget)
        self.others.setStyleSheet("font: 75 8pt \"Palatino Linotype\";")
        self.others.setObjectName("others")
        self.horizontalLayout.addWidget(self.others)
        self.formLayout_2.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bloodgroup = QtWidgets.QComboBox(self.centralwidget)
        self.bloodgroup.setObjectName("bloodgroup")
        self.bloodgroup.addItem("")
        self.bloodgroup.addItem("")
        self.bloodgroup.addItem("")
        self.bloodgroup.addItem("")
        self.bloodgroup.addItem("")
        self.bloodgroup.addItem("")
        self.bloodgroup.addItem("")
        self.bloodgroup.addItem("")
        self.horizontalLayout_2.addWidget(self.bloodgroup)
        self.formLayout_2.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.city = QtWidgets.QLineEdit(self.centralwidget)
        self.city.setObjectName("city")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.city)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.state = QtWidgets.QComboBox(self.centralwidget)
        self.state.setObjectName("state")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.state)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.mobile = QtWidgets.QLineEdit(self.centralwidget)
        self.mobile.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.mobile.setMaxLength(10)
        self.mobile.setObjectName("mobile")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.mobile)
        self.changes = QtWidgets.QLabel(self.centralwidget)
        self.changes.setText("")
        self.changes.setObjectName("changes")
        self.formLayout_2.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.changes)
        self.sendrequest = QtWidgets.QPushButton(self.centralwidget)
        self.sendrequest.setStyleSheet("background:rgb(227, 227, 227)")
        self.sendrequest.setObjectName("sendrequest")
        self.formLayout_2.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.sendrequest)

        #send request if everything is right
        self.sendrequest.clicked.connect(self.send)

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.dob = QtWidgets.QDateEdit(self.centralwidget)
        self.dob.setObjectName("dob")
        self.horizontalLayout_6.addWidget(self.dob)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_6)
        Request.setCentralWidget(self.centralwidget)


        self.retranslateUi(Request)
        QtCore.QMetaObject.connectSlotsByName(Request)

    def retranslateUi(self, Request):
        _translate = QtCore.QCoreApplication.translate
        Request.setWindowTitle(_translate("Request", "Send Request"))
        self.label.setText(_translate("Request", "Name of receiver: "))
        self.label_7.setText(_translate("Request", "Date of Birth: "))
        self.label_8.setText(_translate("Request", "Gender: "))
        self.male.setText(_translate("Request", "Male"))
        self.female.setText(_translate("Request", "Female"))
        self.others.setText(_translate("Request", "Others"))
        self.label_11.setText(_translate("Request", "Blood Group: "))
        self.bloodgroup.setItemText(0, _translate("Request", "A+"))
        self.bloodgroup.setItemText(1, _translate("Request", "A-"))
        self.bloodgroup.setItemText(2, _translate("Request", "B+"))
        self.bloodgroup.setItemText(3, _translate("Request", "B-"))
        self.bloodgroup.setItemText(4, _translate("Request", "O+"))
        self.bloodgroup.setItemText(5, _translate("Request", "O-"))
        self.bloodgroup.setItemText(6, _translate("Request", "AB+"))
        self.bloodgroup.setItemText(7, _translate("Request", "AB-"))
        self.label_2.setText(_translate("Request", "City: "))
        self.label_9.setText(_translate("Request", "State: "))
        self.state.setItemText(0, _translate("Request", "Andaman and Nicobar Islands"))
        self.state.setItemText(1, _translate("Request", "Andhra Pradesh"))
        self.state.setItemText(2, _translate("Request", "Arunachal Pradesh"))
        self.state.setItemText(3, _translate("Request", "Assam"))
        self.state.setItemText(4, _translate("Request", "Bihar"))
        self.state.setItemText(5, _translate("Request", "Chandigarh "))
        self.state.setItemText(6, _translate("Request", "Chhattisgarh"))
        self.state.setItemText(7, _translate("Request", "Dadra and Nagar Haveli and Daman and Diu"))
        self.state.setItemText(8, _translate("Request", "Delhi"))
        self.state.setItemText(9, _translate("Request", "Goa"))
        self.state.setItemText(10, _translate("Request", "Gujarat"))
        self.state.setItemText(11, _translate("Request", "Haryana"))
        self.state.setItemText(12, _translate("Request", "Himachal Pradesh"))
        self.state.setItemText(13, _translate("Request", "Jammu and Kashmir"))
        self.state.setItemText(14, _translate("Request", "Jharkhand"))
        self.state.setItemText(15, _translate("Request", "Karnataka"))
        self.state.setItemText(16, _translate("Request", "Kerala"))
        self.state.setItemText(17, _translate("Request", "Ladakh"))
        self.state.setItemText(18, _translate("Request", "Lakshadweep"))
        self.state.setItemText(19, _translate("Request", "Madhya Pradesh"))
        self.state.setItemText(20, _translate("Request", "Maharashtra"))
        self.state.setItemText(21, _translate("Request", "Manipur"))
        self.state.setItemText(22, _translate("Request", "Meghalaya"))
        self.state.setItemText(23, _translate("Request", "Mizoram"))
        self.state.setItemText(24, _translate("Request", "Nagaland"))
        self.state.setItemText(25, _translate("Request", "Odisha"))
        self.state.setItemText(26, _translate("Request", "Puducherry"))
        self.state.setItemText(27, _translate("Request", "Punjab"))
        self.state.setItemText(28, _translate("Request", "Rajasthan"))
        self.state.setItemText(29, _translate("Request", "Sikkim"))
        self.state.setItemText(30, _translate("Request", "Tamil Nadu"))
        self.state.setItemText(31, _translate("Request", "Telangana"))
        self.state.setItemText(32, _translate("Request", "Tripura"))
        self.state.setItemText(33, _translate("Request", "Uttar Pradesh"))
        self.state.setItemText(34, _translate("Request", "Uttarakhand"))
        self.state.setItemText(35, _translate("Request", "West Bengal"))
        self.label_12.setText(_translate("Request", "Mobile No: "))
        self.sendrequest.setText(_translate("Request", "Send Request"))

import logo_rc
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Request = QtWidgets.QMainWindow()
    ui = Ui_Request()
    ui.setupUi(Request)
    Request.show()
    sys.exit(app.exec_())
