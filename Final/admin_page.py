# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_page.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import re
import sqlite3
from user_display import UserData
from hospital_display import HospitalData
from request_display import RequestData
from camp_display import CampData


class Ui_adminpage(object):

    def userview(self):
        self.w=UserData()
        self.w.show()

    def requestview(self):
        self.w=RequestData()
        self.w.show()
        

    def hospitalview(self):
        self.w=HospitalData()
        self.w.show()

    def campview(self):
        self.w=CampData()
        self.w.show()
       
        
    def hospital(self):
        
        #Establish connection with database
        conn=sqlite3.connect("project.db")
        c=conn.cursor()

        #To input details
        name=str(self.hname.text())
        addr=str(self.haddr.text())
        city=str(self.hcity.text())
        hcondet=str(self.hcdetails.text())

        #To input hstate
        if self.hstate.currentIndex()==0:
            hstate="Andaman and Nicobar Islands"
        elif self.hstate.currentIndex()==1:
            hstate="Andhra Pradesh"
        elif self.hstate.currentIndex()==2:
            hstate="Arunachal Pradesh"
        elif self.hstate.currentIndex()==3:
            hstate="Assam"
        elif self.hstate.currentIndex()==4:
            hstate="Bihar"
        elif self.hstate.currentIndex()==5:
            hstate="Chandigarh"
        elif self.hstate.currentIndex()==6:
            hstate="Chhattisgarh"
        elif self.hstate.currentIndex()==7:
            hstate="Dadra and Nagar Haveli and Daman and Diu"
        elif self.hstate.currentIndex()==8:
            hstate="Delhi"
        elif self.hstate.currentIndex()==9:
            hstate="Goa"
        elif self.hstate.currentIndex()==10:
            hstate="Gujarat"
        elif self.hstate.currentIndex()==11:
            hstate="Haryana"
        elif self.hstate.currentIndex()==12:
            hstate="Himachal Pradesh"
        elif self.hstate.currentIndex()==13:
            hstate="Jammu and Kashmir"
        elif self.hstate.currentIndex()==14:
            hstate="Jharkhand"
        elif self.hstate.currentIndex()==15:
            hstate="Karnataka"
        elif self.hstate.currentIndex()==16:
            hstate="Kerala"
        elif self.hstate.currentIndex()==17:
            hstate="Ladakh"
        elif self.hstate.currentIndex()==18:
            hstate="Lakshadweep"
        elif self.hstate.currentIndex()==19:
            hstate="Madhya Pradesh"
        elif self.hstate.currentIndex()==20:
            hstate="Maharashtra"
        elif self.hstate.currentIndex()==21:
            hstate="Manipur"
        elif self.hstate.currentIndex()==22:
            hstate="Meghalaya"
        elif self.hstate.currentIndex()==23:
            hstate="Mizoram"
        elif self.hstate.currentIndex()==24:
            hstate="Nagaland"
        elif self.hstate.currentIndex()==25:
            hstate="Odisha"
        elif self.hstate.currentIndex()==26:
            hstate="Puducherry"
        elif self.hstate.currentIndex()==27:
            hstate="Punjab"
        elif self.hstate.currentIndex()==28:
            hstate="Rajasthan"
        elif self.hstate.currentIndex()==29:
            hstate="Sikkim"
        elif self.hstate.currentIndex()==30:
            hstate="Tamil Nadu"
        elif self.hstate.currentIndex()==31:
            hstate="Telangana"
        elif self.hstate.currentIndex()==32:
            hstate="Tripura"
        elif self.hstate.currentIndex()==33:
            hstate="Uttar Pradesh"
        elif self.hstate.currentIndex()==34:
            hstate="Uttarakhand"
        elif self.hstate.currentIndex()==35:
            hstate="West Bengal"

        #To print details
        print(name,addr,city,hstate,hcondet)

        #To insert data in table
        c1="INSERT INTO hospital VALUES (?,?,?,?,?)"
        c2=(name,addr,city,hstate,hcondet)
        c.execute(c1,c2)
        conn.commit()
        #self.label.setText("Welcome")
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("The hospital has been successfully added.")
        msg.setWindowTitle("Registration Successful")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()


    def camp(self):

        #Establish connection with database
        conn=sqlite3.connect("project.db")
        c=conn.cursor()

        #To input details
        time=str(self.ctime.text())
        addr=str(self.caddr.text())
        city=str(self.ccity.text())
        hcondet=str(self.ccdetails.text())

        #To input date
        dc=self.doc.date()
        dc=dc.toPyDate()
        dc=str(dc)

        #To input cstate
        if self.cstate.currentIndex()==0:
            cstate="Andaman and Nicobar Islands"
        elif self.cstate.currentIndex()==1:
            cstate="Andhra Pradesh"
        elif self.cstate.currentIndex()==2:
            cstate="Arunachal Pradesh"
        elif self.cstate.currentIndex()==3:
            cstate="Assam"
        elif self.cstate.currentIndex()==4:
            cstate="Bihar"
        elif self.cstate.currentIndex()==5:
            cstate="Chandigarh"
        elif self.cstate.currentIndex()==6:
            cstate="Chhattisgarh"
        elif self.cstate.currentIndex()==7:
            cstate="Dadra and Nagar Haveli and Daman and Diu"
        elif self.cstate.currentIndex()==8:
            cstate="Delhi"
        elif self.cstate.currentIndex()==9:
            cstate="Goa"
        elif self.cstate.currentIndex()==10:
            cstate="Gujarat"
        elif self.cstate.currentIndex()==11:
            cstate="Haryana"
        elif self.cstate.currentIndex()==12:
            cstate="Himachal Pradesh"
        elif self.cstate.currentIndex()==13:
            cstate="Jammu and Kashmir"
        elif self.cstate.currentIndex()==14:
            cstate="Jharkhand"
        elif self.cstate.currentIndex()==15:
            cstate="Karnataka"
        elif self.cstate.currentIndex()==16:
            cstate="Kerala"
        elif self.cstate.currentIndex()==17:
            cstate="Ladakh"
        elif self.cstate.currentIndex()==18:
            cstate="Lakshadweep"
        elif self.cstate.currentIndex()==19:
            cstate="Madhya Pradesh"
        elif self.cstate.currentIndex()==20:
            cstate="Maharashtra"
        elif self.cstate.currentIndex()==21:
            cstate="Manipur"
        elif self.cstate.currentIndex()==22:
            cstate="Meghalaya"
        elif self.cstate.currentIndex()==23:
            cstate="Mizoram"
        elif self.cstate.currentIndex()==24:
            cstate="Nagaland"
        elif self.cstate.currentIndex()==25:
            cstate="Odisha"
        elif self.cstate.currentIndex()==26:
            cstate="Puducherry"
        elif self.cstate.currentIndex()==27:
            cstate="Punjab"
        elif self.cstate.currentIndex()==28:
            cstate="Rajasthan"
        elif self.cstate.currentIndex()==29:
            cstate="Sikkim"
        elif self.cstate.currentIndex()==30:
            cstate="Tamil Nadu"
        elif self.cstate.currentIndex()==31:
            cstate="Telangana"
        elif self.cstate.currentIndex()==32:
            cstate="Tripura"
        elif self.cstate.currentIndex()==33:
            cstate="Uttar Pradesh"
        elif self.cstate.currentIndex()==34:
            cstate="Uttarakhand"
        elif self.cstate.currentIndex()==35:
            cstate="West Bengal"

        #To print details
        print(dc,addr,city,cstate,time,hcondet)

        #To insert data in table
        c1="INSERT INTO camps VALUES (?,?,?,?,?,?)"
        c2=(dc,addr,city,cstate,time,hcondet)
        c.execute(c1,c2)
        conn.commit()
        #self.label.setText("Welcome")
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("The camp details have been added successfully.")
        msg.setWindowTitle("Registration Successful")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()




    def setupUi(self, adminpage):
        adminpage.setObjectName("adminpage")
        adminpage.resize(1200, 650)
        adminpage.setMaximumSize(1200, 650)
        adminpage.setMinimumSize(1200, 650)     
        self.centralwidget = QtWidgets.QWidget(adminpage)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1200, 650))
        self.bg.setStyleSheet("background-image:url(:/background/background.jpeg)")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.heading = QtWidgets.QLabel(self.centralwidget)
        self.heading.setGeometry(QtCore.QRect(30, 20, 565, 35))
        self.heading.setStyleSheet("font: 75 20pt \"Segoe Print\"")
        self.heading.setObjectName("heading")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(830, 10, 250, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.admin_name = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.admin_name.setStyleSheet("font: 75 italic 14pt \"Lucida Bright\";")
        self.admin_name.setObjectName("admin_name")
        self.horizontalLayout.addWidget(self.admin_name)
        self.logout = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)                
        self.logout.setFont(font)
        self.logout.setStyleSheet("border: 1px solid black;")
        self.logout.setObjectName("logout")        
        self.horizontalLayout.addWidget(self.logout)

        #calling the function to close the window.
        self.logout.clicked.connect(lambda:adminpage.close())
        
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(630, 60, 530, 111))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.viewdonors = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)        
        self.viewdonors.setFont(font)
        self.viewdonors.setStyleSheet("border: 1px solid black;")
        self.viewdonors.setObjectName("viewdonors")
        self.horizontalLayout_5.addWidget(self.viewdonors)

        #display user data
        self.viewdonors.clicked.connect(self.userview)
        
        self.viewrequest = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)       
        self.viewrequest.setFont(font)
        self.viewrequest.setStyleSheet("border: 1px solid black;")
        self.viewrequest.setObjectName("viewrequest")
        self.horizontalLayout_5.addWidget(self.viewrequest)

        #display request data
        self.viewrequest.clicked.connect(self.requestview)
        

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(60, 60, 530, 111))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.viewbloodbank = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.viewbloodbank.setFont(font)
        self.viewbloodbank.setStyleSheet("border: 1px solid black;")
        self.viewbloodbank.setObjectName("viewbloodbank")
        self.horizontalLayout_4.addWidget(self.viewbloodbank)

        #display hospital data
        self.viewbloodbank.clicked.connect(self.hospitalview)
        

        self.viewcamp = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.viewcamp.setFont(font)
        self.viewcamp.setStyleSheet("border: 1px solid black;")
        self.viewcamp.setObjectName("viewcamp")
        self.horizontalLayout_4.addWidget(self.viewcamp)

        #display camp data
        self.viewcamp.clicked.connect(self.campview)
        

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 180, 561, 456))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_21.addWidget(self.label_5)
        self.hname = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hname.setObjectName("hname")
        self.horizontalLayout_21.addWidget(self.hname)
        self.verticalLayout.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.haddr = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.haddr.setObjectName("haddr")
        self.horizontalLayout_7.addWidget(self.haddr)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.hcity = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hcity.setObjectName("hcity")
        self.horizontalLayout_3.addWidget(self.hcity)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.hstate = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.hstate.setObjectName("hstate")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.hstate.addItem("")
        self.horizontalLayout_6.addWidget(self.hstate)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.hcdetails = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hcdetails.setObjectName("hcdetails")
        self.horizontalLayout_2.addWidget(self.hcdetails)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.addhospital = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.addhospital.setFont(font)
        self.addhospital.setStyleSheet("border: 1px solid black;")
        self.addhospital.setObjectName("addhospital")
        self.verticalLayout.addWidget(self.addhospital)

        #to add hosp
        self.addhospital.clicked.connect(self.hospital)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(620, 180, 531, 450))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_10.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_20.addWidget(self.label_10)
        self.doc = QtWidgets.QDateEdit(self.verticalLayoutWidget_2)
        self.doc.setObjectName("doc")
        self.horizontalLayout_20.addWidget(self.doc)
        self.verticalLayout_2.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_11.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_19.addWidget(self.label_11)
        self.caddr = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.caddr.setObjectName("caddr")
        self.horizontalLayout_19.addWidget(self.caddr)
        self.verticalLayout_2.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_12.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        self.ccity = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.ccity.setObjectName("ccity")
        self.horizontalLayout_10.addWidget(self.ccity)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_13.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_9.addWidget(self.label_13)
        self.cstate = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.cstate.setObjectName("cstate")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.cstate.addItem("")
        self.horizontalLayout_9.addWidget(self.cstate)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_14.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_11.addWidget(self.label_14)
        self.ctime = QtWidgets.QTimeEdit(self.verticalLayoutWidget_2)


        self.ctime.setObjectName("ctime")
        self.horizontalLayout_11.addWidget(self.ctime)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_15.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_8.addWidget(self.label_15)
        self.ccdetails = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.ccdetails.setObjectName("ccdetails")
        self.horizontalLayout_8.addWidget(self.ccdetails)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.addcamp = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.addcamp.setFont(font)
        self.addcamp.setStyleSheet("border: 1px solid black;")
        self.addcamp.setObjectName("addcamp")
        self.verticalLayout_2.addWidget(self.addcamp)

        #to add camp
        self.addcamp.clicked.connect(self.camp)
        
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(1020, 730, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(1020, 540, 2, 2))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(620, 150, 535, 65))
        self.label_4.setStyleSheet("font: 75 italic 18pt \"Lucida Bright\";\n""text-decoration: underline;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 535, 73))
        self.label_3.setStyleSheet("font: 75 italic 18pt \"Lucida Bright\";\n""text-decoration: underline;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        adminpage.setCentralWidget(self.centralwidget)

        self.retranslateUi(adminpage)
        self.hname.returnPressed.connect(self.haddr.setFocus) # type: ignore
        self.haddr.returnPressed.connect(self.hcity.setFocus)
        self.hstate.activated['QString'].connect(self.hcdetails.setFocus) # type: ignore
        self.hcdetails.returnPressed.connect(self.addhospital.animateClick)
        self.doc.editingFinished.connect(self.caddr.setFocus) # type: ignore
        self.caddr.returnPressed.connect(self.ccity.setFocus)
        self.hstate.activated['QString'].connect(self.ctime.setFocus) # type: ignore
        self.ccdetails.returnPressed.connect(self.addcamp.animateClick)
        self.addhospital.clicked.connect(self.hname.clear)
        self.addhospital.clicked.connect(self.haddr.clear)
        self.addhospital.clicked.connect(self.hcity.clear)
        self.addhospital.clicked.connect(self.hcdetails.clear)
        self.addcamp.clicked.connect(self.caddr.clear)
        self.addcamp.clicked.connect(self.ccity.clear)
        self.addcamp.clicked.connect(self.ccdetails.clear)

        QtCore.QMetaObject.connectSlotsByName(adminpage)

    def retranslateUi(self, adminpage):
        _translate = QtCore.QCoreApplication.translate
        adminpage.setWindowTitle(_translate("adminpage", "Admin Login"))
        self.heading.setText(_translate("adminpage", "The Donors' Community : Admin Panel"))
        self.admin_name.setText(_translate("adminpage", "Name"))
        self.logout.setText(_translate("adminpage", "Logout"))
        self.viewdonors.setText(_translate("adminpage", "View Donors\' List"))
        self.viewrequest.setText(_translate("adminpage", "View Requests"))
        self.viewbloodbank.setText(_translate("adminpage", "View Blood Banks"))
        self.viewcamp.setText(_translate("adminpage", "View Camps"))
        self.label_5.setText(_translate("adminpage", "Hospital Name: "))
        self.label_6.setText(_translate("adminpage", "Address:"))
        self.label_7.setText(_translate("adminpage", "City: "))
        self.label_9.setText(_translate("adminpage", "State:"))
        self.hstate.setItemText(0, _translate("adminpage", "Andaman and Nicobar Islands"))
        self.hstate.setItemText(1, _translate("adminpage", "Andhra Pradesh"))
        self.hstate.setItemText(2, _translate("adminpage", "Arunachal Pradesh"))
        self.hstate.setItemText(3, _translate("adminpage", "Assam"))
        self.hstate.setItemText(4, _translate("adminpage", "Bihar"))
        self.hstate.setItemText(5, _translate("adminpage", "Chandigarh "))
        self.hstate.setItemText(6, _translate("adminpage", "Chhattisgarh"))
        self.hstate.setItemText(7, _translate("adminpage", "Dadra and Nagar Haveli and Daman and Diu"))
        self.hstate.setItemText(8, _translate("adminpage", "Delhi"))
        self.hstate.setItemText(9, _translate("adminpage", "Goa"))
        self.hstate.setItemText(10, _translate("adminpage", "Gujarat"))
        self.hstate.setItemText(11, _translate("adminpage", "Haryana"))
        self.hstate.setItemText(12, _translate("adminpage", "Himachal Pradesh"))
        self.hstate.setItemText(13, _translate("adminpage", "Jammu and Kashmir"))
        self.hstate.setItemText(14, _translate("adminpage", "Jharkhand"))
        self.hstate.setItemText(15, _translate("adminpage", "Karnataka"))
        self.hstate.setItemText(16, _translate("adminpage", "Kerala"))
        self.hstate.setItemText(17, _translate("adminpage", "Ladakh"))
        self.hstate.setItemText(18, _translate("adminpage", "Lakshadweep"))
        self.hstate.setItemText(19, _translate("adminpage", "Madhya Pradesh"))
        self.hstate.setItemText(20, _translate("adminpage", "Maharashtra"))
        self.hstate.setItemText(21, _translate("adminpage", "Manipur"))
        self.hstate.setItemText(22, _translate("adminpage", "Meghalaya"))
        self.hstate.setItemText(23, _translate("adminpage", "Mizoram"))
        self.hstate.setItemText(24, _translate("adminpage", "Nagaland"))
        self.hstate.setItemText(25, _translate("adminpage", "Odisha"))
        self.hstate.setItemText(26, _translate("adminpage", "Puducherry"))
        self.hstate.setItemText(27, _translate("adminpage", "Punjab"))
        self.hstate.setItemText(28, _translate("adminpage", "Rajasthan"))
        self.hstate.setItemText(29, _translate("adminpage", "Sikkim"))
        self.hstate.setItemText(30, _translate("adminpage", "Tamil Nadu"))
        self.hstate.setItemText(31, _translate("adminpage", "Telangana"))
        self.hstate.setItemText(32, _translate("adminpage", "Tripura"))
        self.hstate.setItemText(33, _translate("adminpage", "Uttar Pradesh"))
        self.hstate.setItemText(34, _translate("adminpage", "Uttarakhand"))
        self.hstate.setItemText(35, _translate("adminpage", "West Bengal"))
        self.label_8.setText(_translate("adminpage", "Contact Details: "))
        self.addhospital.setText(_translate("adminpage", "Add Hospital"))
        self.label_10.setText(_translate("adminpage", "Date of Camp: "))
        self.label_11.setText(_translate("adminpage", "Address:"))
        self.label_12.setText(_translate("adminpage", "City: "))
        self.label_13.setText(_translate("adminpage", "State:"))
        self.cstate.setItemText(0, _translate("adminpage", "Andaman and Nicobar Islands"))
        self.cstate.setItemText(1, _translate("adminpage", "Andhra Pradesh"))
        self.cstate.setItemText(2, _translate("adminpage", "Arunachal Pradesh"))
        self.cstate.setItemText(3, _translate("adminpage", "Assam"))
        self.cstate.setItemText(4, _translate("adminpage", "Bihar"))
        self.cstate.setItemText(5, _translate("adminpage", "Chandigarh "))
        self.cstate.setItemText(6, _translate("adminpage", "Chhattisgarh"))
        self.cstate.setItemText(7, _translate("adminpage", "Dadra and Nagar Haveli and Daman and Diu"))
        self.cstate.setItemText(8, _translate("adminpage", "Delhi"))
        self.cstate.setItemText(9, _translate("adminpage", "Goa"))
        self.cstate.setItemText(10, _translate("adminpage", "Gujarat"))
        self.cstate.setItemText(11, _translate("adminpage", "Haryana"))
        self.cstate.setItemText(12, _translate("adminpage", "Himachal Pradesh"))
        self.cstate.setItemText(13, _translate("adminpage", "Jammu and Kashmir"))
        self.cstate.setItemText(14, _translate("adminpage", "Jharkhand"))
        self.cstate.setItemText(15, _translate("adminpage", "Karnataka"))
        self.cstate.setItemText(16, _translate("adminpage", "Kerala"))
        self.cstate.setItemText(17, _translate("adminpage", "Ladakh"))
        self.cstate.setItemText(18, _translate("adminpage", "Lakshadweep"))
        self.cstate.setItemText(19, _translate("adminpage", "Madhya Pradesh"))
        self.cstate.setItemText(20, _translate("adminpage", "Maharashtra"))
        self.cstate.setItemText(21, _translate("adminpage", "Manipur"))
        self.cstate.setItemText(22, _translate("adminpage", "Meghalaya"))
        self.cstate.setItemText(23, _translate("adminpage", "Mizoram"))
        self.cstate.setItemText(24, _translate("adminpage", "Nagaland"))
        self.cstate.setItemText(25, _translate("adminpage", "Odisha"))
        self.cstate.setItemText(26, _translate("adminpage", "Puducherry"))
        self.cstate.setItemText(27, _translate("adminpage", "Punjab"))
        self.cstate.setItemText(28, _translate("adminpage", "Rajasthan"))
        self.cstate.setItemText(29, _translate("adminpage", "Sikkim"))
        self.cstate.setItemText(30, _translate("adminpage", "Tamil Nadu"))
        self.cstate.setItemText(31, _translate("adminpage", "Telangana"))
        self.cstate.setItemText(32, _translate("adminpage", "Tripura"))
        self.cstate.setItemText(33, _translate("adminpage", "Uttar Pradesh"))
        self.cstate.setItemText(34, _translate("adminpage", "Uttarakhand"))
        self.cstate.setItemText(35, _translate("adminpage", "West Bengal"))
        self.label_14.setText(_translate("adminpage", "Time: "))
        self.label_15.setText(_translate("adminpage", "Contact Details: "))
        self.addcamp.setText(_translate("adminpage", "Add Camp"))
        self.label_4.setText(_translate("adminpage", "Add Blood Donation Camp"))
        self.label_3.setText(_translate("adminpage", "Add Hospital having Blood Bank"))

import logo_rc
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    adminpage = QtWidgets.QMainWindow()
    ui = Ui_adminpage()
    ui.setupUi(adminpage)
    adminpage.show()
    sys.exit(app.exec_())

