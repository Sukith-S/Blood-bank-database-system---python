# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign_up_form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import re
import sqlite3

class Ui_SignUp(object):
    def popup(self):

        #Establish connection with database
        conn=sqlite3.connect("project.db")
        c=conn.cursor()
        c.execute('''SELECT Username FROM user''')
        names={name[0] for name in c.fetchall()}


        #To input details
        name1=str(self.fname.text())
        name2=str(self.lname.text())
        phone=str(self.mobile.text())
        mail=str(self.email.text())
        donated=str(self.dondetails.toPlainText())
        history=str(self.hisdetails.toPlainText())
        user=str(self.username.text())
        passwd=str(self.password.text())
        sex=""
        
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

        #To check whether email-id and password is correct
        string=re.compile("\w+@[a-z]\D.\D[a-z]")
        d=re.compile('\d')
        if len(name1)==0 or len(name2)==0 or len(phone)==0 or len(mail)==0 or len(user)==0 or len(passwd)==0 or len(donated)==0 or len(history)==0 or len(sex)==0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("All the fields are required.")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        elif phone.isdigit()==False or len(phone)<10:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Enter correct mobile number.")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        elif string.findall(mail)==[]:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Enter correct email address.")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        elif d.findall(passwd)==[]:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Password should contain atleast 1 digit.")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        elif user in names:
            #Checking if username already exists
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Username already taken.")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        else:
            c1="INSERT INTO user VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
            c2=(name1,name2,bd,sex,state,bg,phone,mail,donated,history,user,passwd)
            c.execute(c1,c2)
            conn.commit()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Congragulations! You're now a part of the community.")
            msg.setWindowTitle("Sign Up Successful")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
            #SignUp.close()


        #To print input data
        print(name1,name2,phone,mail,user,passwd,donated,history,sex,state,bg,bd)


        
    def setupUi(self, SignUp):
        SignUp.setObjectName("SignUp")
        SignUp.resize(700, 500)
        SignUp.setMaximumSize(700,500)
        SignUp.setMinimumSize(700,500)
        SignUp.setUnifiedTitleAndToolBarOnMac(False)
        #SignUp.setStyleSheet("background-color: rgb(253, 247, 245);")
        self.centralwidget = QtWidgets.QWidget(SignUp)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 700, 1000))
        self.bg.setStyleSheet(u"background:qconicalgradient(cx:1, cy:0, angle:0, stop:0.00568182 rgba(255, 0, 0, 255), stop:0.602273 rgba(255, 243, 243, 255))")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.formLayout_2 = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.formLayout)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")

        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.fname = QtWidgets.QLineEdit(self.centralwidget)
        self.fname.setObjectName("fname")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fname)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lname = QtWidgets.QLineEdit(self.centralwidget)

        self.lname.setObjectName("lname")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lname)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_8)
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
        self.formLayout_2.setLayout(10, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_9)
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
        self.formLayout_2.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.state)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
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
        self.horizontalLayout_4.addWidget(self.bloodgroup)
        self.formLayout_2.setLayout(16, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.mobile = QtWidgets.QLineEdit(self.centralwidget)
        self.mobile.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.mobile.setMaxLength(10)
        self.mobile.setObjectName("mobile")
        self.formLayout_2.setWidget(19, QtWidgets.QFormLayout.FieldRole, self.mobile)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(22, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.email.setObjectName("email")
        self.formLayout_2.setWidget(22, QtWidgets.QFormLayout.FieldRole, self.email)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(24, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setStyleSheet("font: 75 8pt \"Palatino Linotype\";")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        self.formLayout_2.setLayout(24, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(33, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.dondetails = QtWidgets.QTextEdit(self.centralwidget)
        self.dondetails.setObjectName("dondetails")
        self.formLayout_2.setWidget(33, QtWidgets.QFormLayout.FieldRole, self.dondetails)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(40, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setStyleSheet("font: 75 8pt \"Palatino Linotype\";")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_3.addWidget(self.label_15)
        self.formLayout_2.setLayout(40, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(45, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.hisdetails = QtWidgets.QTextEdit(self.centralwidget)
        self.hisdetails.setObjectName("hisdetails")
        self.formLayout_2.setWidget(45, QtWidgets.QFormLayout.FieldRole, self.hisdetails)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(47, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setObjectName("username")
        self.formLayout_2.setWidget(47, QtWidgets.QFormLayout.FieldRole, self.username)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setStyleSheet("font: 75 10pt \"Palatino Linotype\";")
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(52, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        #self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.formLayout_2.setWidget(52, QtWidgets.QFormLayout.FieldRole, self.password)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("font: 75 8pt \"Palatino Linotype\";")
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(53, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.signupf = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.signupf.setFont(font)
        self.signupf.setStyleSheet("background:rgb(227, 227, 227)")
        self.signupf.setObjectName("signupf")
        self.verticalLayout.addWidget(self.signupf)

        #display popup if everything is right
        self.signupf.clicked.connect(self.popup)
        
        self.formLayout_2.setLayout(59, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
        self.changes = QtWidgets.QLabel(self.centralwidget)
        self.changes.setObjectName("changes")
        self.formLayout_2.setWidget(60, QtWidgets.QFormLayout.FieldRole, self.changes)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.dob = QtWidgets.QDateEdit(self.centralwidget)
        self.dob.setObjectName("dob")
        self.horizontalLayout_5.addWidget(self.dob)
        self.formLayout_2.setLayout(7, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        SignUp.setCentralWidget(self.centralwidget)

        self.retranslateUi(SignUp)
        self.fname.returnPressed.connect(self.lname.setFocus) # type: ignore
        self.lname.returnPressed.connect(self.dob.setFocus) # type: ignore
        self.bloodgroup.activated['QString'].connect(self.mobile.setFocus) # type: ignore
        self.mobile.returnPressed.connect(self.email.setFocus) # type: ignore
        self.username.returnPressed.connect(self.password.setFocus) # type: ignore
        self.password.returnPressed.connect(self.signupf.animateClick) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(SignUp)

    def retranslateUi(self, SignUp):
        _translate = QtCore.QCoreApplication.translate
        SignUp.setWindowTitle(_translate("SignUp", "Sign Up Form"))
        self.label_10.setText(_translate("SignUp", "First Name: "))
        self.label_6.setText(_translate("SignUp", "Last Name: "))
        self.label_7.setText(_translate("SignUp", "Date of Birth: "))
        self.label_8.setText(_translate("SignUp", "Gender: "))
        self.male.setText(_translate("SignUp", "Male"))
        self.female.setText(_translate("SignUp", "Female"))
        self.others.setText(_translate("SignUp", "Others"))
        self.label_9.setText(_translate("SignUp", "State: "))
        self.state.setItemText(0, _translate("SignUp", "Andaman and Nicobar Islands"))
        self.state.setItemText(1, _translate("SignUp", "Andhra Pradesh"))
        self.state.setItemText(2, _translate("SignUp", "Arunachal Pradesh"))
        self.state.setItemText(3, _translate("SignUp", "Assam"))
        self.state.setItemText(4, _translate("SignUp", "Bihar"))
        self.state.setItemText(5, _translate("SignUp", "Chandigarh "))
        self.state.setItemText(6, _translate("SignUp", "Chhattisgarh"))
        self.state.setItemText(7, _translate("SignUp", "Dadra and Nagar Haveli and Daman and Diu"))
        self.state.setItemText(8, _translate("SignUp", "Delhi"))
        self.state.setItemText(9, _translate("SignUp", "Goa"))
        self.state.setItemText(10, _translate("SignUp", "Gujarat"))
        self.state.setItemText(11, _translate("SignUp", "Haryana"))
        self.state.setItemText(12, _translate("SignUp", "Himachal Pradesh"))
        self.state.setItemText(13, _translate("SignUp", "Jammu and Kashmir"))
        self.state.setItemText(14, _translate("SignUp", "Jharkhand"))
        self.state.setItemText(15, _translate("SignUp", "Karnataka"))
        self.state.setItemText(16, _translate("SignUp", "Kerala"))
        self.state.setItemText(17, _translate("SignUp", "Ladakh"))
        self.state.setItemText(18, _translate("SignUp", "Lakshadweep"))
        self.state.setItemText(19, _translate("SignUp", "Madhya Pradesh"))
        self.state.setItemText(20, _translate("SignUp", "Maharashtra"))
        self.state.setItemText(21, _translate("SignUp", "Manipur"))
        self.state.setItemText(22, _translate("SignUp", "Meghalaya"))
        self.state.setItemText(23, _translate("SignUp", "Mizoram"))
        self.state.setItemText(24, _translate("SignUp", "Nagaland"))
        self.state.setItemText(25, _translate("SignUp", "Odisha"))
        self.state.setItemText(26, _translate("SignUp", "Puducherry"))
        self.state.setItemText(27, _translate("SignUp", "Punjab"))
        self.state.setItemText(28, _translate("SignUp", "Rajasthan"))
        self.state.setItemText(29, _translate("SignUp", "Sikkim"))
        self.state.setItemText(30, _translate("SignUp", "Tamil Nadu"))
        self.state.setItemText(31, _translate("SignUp", "Telangana"))
        self.state.setItemText(32, _translate("SignUp", "Tripura"))
        self.state.setItemText(33, _translate("SignUp", "Uttar Pradesh"))
        self.state.setItemText(34, _translate("SignUp", "Uttarakhand"))
        self.state.setItemText(35, _translate("SignUp", "West Bengal"))
        self.label_11.setText(_translate("SignUp", "Blood Group: "))
        self.bloodgroup.setItemText(0, _translate("SignUp", "A+"))
        self.bloodgroup.setItemText(1, _translate("SignUp", "A-"))
        self.bloodgroup.setItemText(2, _translate("SignUp", "B+"))
        self.bloodgroup.setItemText(3, _translate("SignUp", "B-"))
        self.bloodgroup.setItemText(4, _translate("SignUp", "O+"))
        self.bloodgroup.setItemText(5, _translate("SignUp", "O-"))
        self.bloodgroup.setItemText(6, _translate("SignUp", "AB+"))
        self.bloodgroup.setItemText(7, _translate("SignUp", "AB-"))
        self.label_12.setText(_translate("SignUp", "Mobile No: "))
        self.label_13.setText(_translate("SignUp", "Email ID: "))
        self.label.setText(_translate("SignUp", "Donated blood before?"))
        self.label_14.setText(_translate("SignUp", "If yes, mention the date, city and state where you donated blood. If no, write NA. "))
        self.label_16.setText(_translate("SignUp", "Details: "))
        self.label_2.setText(_translate("SignUp", "Any medical history?"))
        self.label_15.setText(_translate("SignUp", "If yes, mention the details. If no, write NA."))
        self.label_17.setText(_translate("SignUp", "Details:"))
        self.label_3.setText(_translate("SignUp", "Username: "))
        self.label_18.setText(_translate("SignUp", "Password: "))
        self.label_4.setText(_translate("SignUp", "Password must contain atleast one number."))
        self.signupf.setText(_translate("SignUp", "Sign Up"))
        self.changes.setText(_translate("SignUp", ""))

import logo_rc
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignUp = QtWidgets.QMainWindow()
    ui = Ui_SignUp()
    ui.setupUi(SignUp)
    SignUp.show()
    sys.exit(app.exec_())
