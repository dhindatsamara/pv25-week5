# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Coolyeah\kampus\semester_6\pemvis\pv25-week5\form_validation.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 50, 43, 39))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(290, 60, 209, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 80, 41, 39))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(290, 90, 209, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.email.setFont(font)
        self.email.setObjectName("email")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 140, 29, 39))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.age = QtWidgets.QLineEdit(self.centralwidget)
        self.age.setGeometry(QtCore.QRect(290, 150, 211, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.age.setFont(font)
        self.age.setObjectName("age")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 170, 102, 39))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.number = QtWidgets.QLineEdit(self.centralwidget)
        self.number.setGeometry(QtCore.QRect(290, 180, 211, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.number.setFont(font)
        self.number.setObjectName("number")
        self.address = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.address.setGeometry(QtCore.QRect(290, 210, 321, 149))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.address.setFont(font)
        self.address.setObjectName("address")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(210, 200, 71, 39))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(220, 360, 52, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gender = QtWidgets.QComboBox(self.centralwidget)
        self.gender.setGeometry(QtCore.QRect(290, 370, 91, 22))
        self.gender.setObjectName("gender")
        self.gender.addItem("")
        self.gender.setItemText(0, "")
        self.gender.addItem("")
        self.gender.addItem("")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 390, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.edu = QtWidgets.QComboBox(self.centralwidget)
        self.edu.setGeometry(QtCore.QRect(290, 400, 171, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edu.sizePolicy().hasHeightForWidth())
        self.edu.setSizePolicy(sizePolicy)
        self.edu.setObjectName("edu")
        self.edu.addItem("")
        self.edu.setItemText(0, "")
        self.edu.addItem("")
        self.edu.addItem("")
        self.edu.addItem("")
        self.edu.addItem("")
        self.edu.addItem("")
        self.edu.addItem("")
        self.edu.addItem("")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(290, 450, 81, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save.sizePolicy().hasHeightForWidth())
        self.save.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.save.setFont(font)
        self.save.setObjectName("save")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(530, 450, 81, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 550, 321, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(180, 110, 91, 39))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.dob = QtWidgets.QDateEdit(self.centralwidget)
        self.dob.setGeometry(QtCore.QRect(290, 120, 211, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.dob.setFont(font)
        self.dob.setObjectName("dob")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form Validation"))
        self.label.setText(_translate("MainWindow", "Name:"))
        self.label_2.setText(_translate("MainWindow", "Email:"))
        self.label_3.setText(_translate("MainWindow", "Age:"))
        self.label_4.setText(_translate("MainWindow", "Phone Number:"))
        self.label_6.setText(_translate("MainWindow", " Address:"))
        self.label_7.setText(_translate("MainWindow", "Gender:"))
        self.gender.setItemText(1, _translate("MainWindow", "Male"))
        self.gender.setItemText(2, _translate("MainWindow", "Female"))
        self.label_8.setText(_translate("MainWindow", " Education:"))
        self.edu.setItemText(1, _translate("MainWindow", "Elementary School"))
        self.edu.setItemText(2, _translate("MainWindow", "Junior High School"))
        self.edu.setItemText(3, _translate("MainWindow", "Senior High School"))
        self.edu.setItemText(4, _translate("MainWindow", "Diploma"))
        self.edu.setItemText(5, _translate("MainWindow", "Bachelor\'s Degree"))
        self.edu.setItemText(6, _translate("MainWindow", "Master\'s Degree"))
        self.edu.setItemText(7, _translate("MainWindow", "Doctoral Degree"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.label_9.setText(_translate("MainWindow", "Dhinda Tsamara Shalsabilla (F1D022005)"))
        self.label_10.setText(_translate("MainWindow", "  Date of Birth:"))
