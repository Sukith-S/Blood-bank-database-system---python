# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first786.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
from sign_up_form import Ui_SignUp
from admin_page import Ui_adminpage
from user_page import Ui_userpage
import sqlite3



class Ui_home(object):
    def openSignup(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_SignUp()
        self.ui.setupUi(self.window)
        #home.hide()#Hides this window when next window opens
        self.window.show()
        #home.showMinimized()

    def gotouser(self):
        conn=sqlite3.connect("project.db")
        c=conn.cursor()

        #To input details
        userid=str(self.userid.text())
        userpass=str(self.userpass.text())
        print(userid,userpass)

        #we need to check conditions and SQL here
        c1="SELECT * FROM user WHERE Username=? AND Password=?"
        c2=(userid,userpass)
        c.execute(c1,c2)
        results=c.fetchall()
        if results:
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_userpage()
            self.ui.setupUi(self.window)
            self.ui.user_name.setText(userid)
            self.window.show()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Incorrect username or password.")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        
        

    def gotoadmin(self):
        conn=sqlite3.connect("project.db")
        c=conn.cursor()

        #To input details
        adminid=str(self.adminid.text())
        adminpass=str(self.adminpass.text())
        print(adminid,adminpass)

        #we need to check conditions and SQL here
        c1="SELECT * FROM admin WHERE Username=? AND Password=?"
        c2=(adminid,adminpass)
        c.execute(c1,c2)
        results=c.fetchall()
        if results:
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_adminpage()
            self.ui.setupUi(self.window)
            self.ui.admin_name.setText(adminid)
            self.window.show()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Incorrect username or password.")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        
    def setupUi(self, home):
        home.setObjectName("home")
        home.resize(700, 400)
        home.setMaximumSize(700, 400)
        home.setMinimumSize(700, 400)        
        home.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(home)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 700, 400))
        self.bg.setStyleSheet("background-image:url(:/background/bloodCells.jpg)")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;\n"
"font: 75 40pt \"Segoe Print\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 73, 201, 16))
        self.label_2.setStyleSheet("color:white;font: 75 italic 8pt \"Lucida Bright\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 124, 91, 21))
        self.label_3.setStyleSheet("color:white;\n"
"font: 13pt \"Gill Sans Ultra Bold Condensed\";\n"
"text-decoration: underline;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(490, 124, 91, 21))
        self.label_4.setStyleSheet("color:white;\n"
"font: 13pt \"Gill Sans Ultra Bold Condensed\";\n"
"text-decoration: underline;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 170, 91, 21))
        self.label_5.setStyleSheet("color:white;\n"
"font: 14pt \"Gill Sans MT Condensed\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(380, 170, 91, 21))
        self.label_6.setStyleSheet("color:white;\n"
"font: 14pt \"Gill Sans MT Condensed\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(73, 210, 91, 21))
        self.label_7.setStyleSheet("color:white;\n"
"font: 14pt \"Gill Sans MT Condensed\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(382, 210, 91, 21))
        self.label_8.setStyleSheet("color:white;\n"
"font: 14pt \"Gill Sans MT Condensed\";")
        self.label_8.setObjectName("label_8")
        self.userlogin = QtWidgets.QPushButton(self.centralwidget)
        self.userlogin.setGeometry(QtCore.QRect(180, 250, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.userlogin.setFont(font)
        self.userlogin.setStyleSheet("font: 75 8pt \"Palatino Linotype\";")
        self.userlogin.setObjectName("userlogin")

        #go to user page
        self.userlogin.clicked.connect(self.gotouser)

        self.adminlogin = QtWidgets.QPushButton(self.centralwidget)
        self.adminlogin.setGeometry(QtCore.QRect(490, 250, 75, 23))
        self.adminlogin.setStyleSheet("font: 75 8pt \"Palatino Linotype\";")
        self.adminlogin.setObjectName("adminlogin")

        #go to admin page
        self.adminlogin.clicked.connect(self.gotoadmin)

        self.userid = QtWidgets.QLineEdit(self.centralwidget)
        self.userid.setGeometry(QtCore.QRect(160, 172, 113, 20))
        self.userid.setText("")
        self.userid.setObjectName("userid")
        self.userpass = QtWidgets.QLineEdit(self.centralwidget)
        self.userpass.setGeometry(QtCore.QRect(160, 210, 113, 20))
        self.userpass.setToolTip("")
        self.userpass.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.userpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.userpass.setObjectName("userpass")
        self.adminid = QtWidgets.QLineEdit(self.centralwidget)
        self.adminid.setGeometry(QtCore.QRect(470, 172, 113, 20))
        self.adminid.setText("")
        self.adminid.setObjectName("adminid")
        self.adminpass = QtWidgets.QLineEdit(self.centralwidget)
        self.adminpass.setGeometry(QtCore.QRect(470, 210, 113, 20))
        self.adminpass.setToolTip("")
        self.adminpass.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.adminpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.adminpass.setObjectName("adminpass")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 320, 500, 16))
        self.label_9.setStyleSheet("color:white;font: 75 italic 10pt \"Lucida Bright\";")
        self.label_9.setObjectName("label_9")
        self.signup = QtWidgets.QPushButton(self.centralwidget)
        self.signup.setGeometry(QtCore.QRect(40, 345, 75, 23))
        self.signup.setStyleSheet("font: 75 8pt \"Palatino Linotype\";")
        self.signup.setObjectName("signup")

        #calling the function to display signup form
        self.signup.clicked.connect(self.openSignup)

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(550, 30, 401, 243))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("bl3.png"))
        self.label_10.setObjectName("label_10")
        home.setCentralWidget(self.centralwidget)


        self.retranslateUi(home)
        self.userid.returnPressed.connect(self.userpass.setFocus) # type: ignore
        self.userpass.returnPressed.connect(self.userlogin.animateClick) # type: ignore
        self.adminid.returnPressed.connect(self.adminpass.setFocus) # type: ignore
        self.adminpass.returnPressed.connect(self.adminlogin.animateClick) # type: ignore
        self.userlogin.clicked.connect(self.userpass.clear)
        self.userlogin.clicked.connect(self.adminid.clear)
        self.userlogin.clicked.connect(self.adminpass.clear)
        self.adminlogin.clicked.connect(self.adminpass.clear)
        self.adminlogin.clicked.connect(self.userid.clear)
        self.adminlogin.clicked.connect(self.userpass.clear)
        QtCore.QMetaObject.connectSlotsByName(home)

    def retranslateUi(self, home):
        _translate = QtCore.QCoreApplication.translate
        home.setWindowTitle(_translate("home", "Home Page"))
        self.label.setText(_translate("home", "Welcome .."))
        self.label_2.setText(_translate("home", "Donate Blood, Donate life !"))
        self.label_3.setText(_translate("home", "User"))
        self.label_4.setText(_translate("home", "Admin"))
        self.label_5.setText(_translate("home", "Username:"))
        self.label_6.setText(_translate("home", "Username:"))
        self.label_7.setText(_translate("home", "Password:"))
        self.label_8.setText(_translate("home", "Password:"))
        self.userlogin.setText(_translate("home", "Login"))
        self.adminlogin.setText(_translate("home", "Login"))
        self.label_9.setText(_translate("home", "Haven\'t donated yet, sign up and be a part of the community!"))
        self.signup.setText(_translate("home", "Sign Up"))

import logo_rc
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    home = QtWidgets.QMainWindow()
    ui = Ui_home()
    ui.setupUi(home)
    home.show()
    sys.exit(app.exec_())
