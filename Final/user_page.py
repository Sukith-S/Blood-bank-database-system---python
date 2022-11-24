# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_page.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from blood_request import Ui_Request
from hospital_display import HospitalData
from camp_display import CampData



class Ui_userpage(object):

    def u_vc(self):
        self.w=CampData()
        self.w.show()

    def u_vh(self):
        self.w=HospitalData()
        self.w.show()

        
    def loadrequest(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Request()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, userpage):
        userpage.setObjectName("userpage")
        userpage.resize(1080, 450)
        userpage.setMaximumSize(1080, 450)
        userpage.setMinimumSize(1080, 450)
        self.centralwidget = QtWidgets.QWidget(userpage)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1080, 450))
        self.bg.setStyleSheet(u"background:color\"white\"")
        # self.bg.setAutoFillBackground(True)
        self.bg.setObjectName("bg")
        self.icon = QtWidgets.QLabel(self.centralwidget)
        self.icon.setObjectName(u"icon")
        self.icon.setGeometry(QtCore.QRect(820, 120, 165, 165))
        self.icon.setAutoFillBackground(False)
        self.icon.setStyleSheet(u"background:url(:/background/bloooood.jpg)")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(700, 10, 351, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # self.hello=QtWidgets.QLabel(self.horizontalLayoutWidget)
        # font = QtGui.QFont()
        # font.setPointSize(14)
        # self.hello.setFont(font)
        # self.hello.setObjectName("hello")
        # self.hello.setText("Hello ")
        # self.horizontalLayout.addWidget(self.hello)

        self.user_name = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.user_name.setFont(font)
        self.user_name.setObjectName("user_name")
        self.horizontalLayout.addWidget(self.user_name)
        self.user_logout = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.user_logout.setFont(font)
        self.user_logout.setStyleSheet("border: 1px solid black;")
        self.user_logout.setObjectName("user_logout")
        self.horizontalLayout.addWidget(self.user_logout)

        #close this window on clicking logout
        self.user_logout.clicked.connect(lambda:userpage.close() )
        
        self.heading_user = QtWidgets.QLabel(self.centralwidget)
        self.heading_user.setGeometry(QtCore.QRect(40, 30, 561, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        font.setItalic(True)
        self.heading_user.setStyleSheet("text-decoration: underline;")
        self.heading_user.setFont(font)
        self.heading_user.setObjectName("heading_user")
        self.description_user = QtWidgets.QLabel(self.centralwidget)
        self.description_user.setGeometry(QtCore.QRect(20, 100, 1011, 191))
        self.description_user.setStyleSheet("font: 75 12pt \"Palatino Linotype\";")
        self.description_user.setObjectName("description_user")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 300, 1001, 131))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.user_campview = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.user_campview.setFont(font)
        self.user_campview.setStyleSheet("border: 1px solid black;")
        self.user_campview.setObjectName("user_campview")
        self.horizontalLayout_2.addWidget(self.user_campview)

        #display camp data
        self.user_campview.clicked.connect(self.u_vc)
        
        self.user_hospitalview = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.user_hospitalview.setFont(font)
        self.user_hospitalview.setStyleSheet("border: 1px solid black;")
        self.user_hospitalview.setObjectName("user_hospitalview")
        self.horizontalLayout_2.addWidget(self.user_hospitalview)

        #display hospital data
        self.user_hospitalview.clicked.connect(self.u_vh)
        
        self.user_request = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.user_request.setFont(font)
        self.user_request.setStyleSheet("border: 1px solid black;")
        self.user_request.setObjectName("user_request")
        self.horizontalLayout_2.addWidget(self.user_request)

        #open request page on clicking
        self.user_request.clicked.connect(self.loadrequest)
        userpage.setCentralWidget(self.centralwidget)


        self.retranslateUi(userpage)
        QtCore.QMetaObject.connectSlotsByName(userpage)

    def retranslateUi(self, userpage):
        _translate = QtCore.QCoreApplication.translate
        userpage.setWindowTitle(_translate("userpage", "User Login"))
        self.user_name.setText(_translate("userpage", "Name"))
        self.user_logout.setText(_translate("userpage", "Logout"))
        self.heading_user.setText(_translate("userpage", "The Donors' Community"))
        self.description_user.setText(_translate("userpage", "Welcome to the donors\' community.\nYou can now be a support for many.\nThe following are some advantages of being a part of the community: \n\t1.   You can have a look on the upcoming blood donation camps being held in your city and state.\n\t2.   You have the access to the list of the hospitals having blood banks.\n\t3.   The most important thing is that you can request for blood for yourself or any of your relative, \n\t      friend or acquaintance in case of need by filling the form.\nWe have established this community to make blood available easily to the people in the need of it."))
        self.user_campview.setText(_translate("userpage", "View Blood Donation Camps"))
        self.user_hospitalview.setText(_translate("userpage", "View Hospitals having Blood Banks"))
        self.user_request.setText(_translate("userpage", "Make a Request"))

import logo_rc
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    userpage = QtWidgets.QMainWindow()
    ui = Ui_userpage()
    ui.setupUi(userpage)
    userpage.show()
    sys.exit(app.exec_())
