# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/startup_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1650, 950)
        Form.setStyleSheet("")
        self.login_frame = QtWidgets.QFrame(Form)
        self.login_frame.setGeometry(QtCore.QRect(500, 500, 660, 341))
        self.login_frame.setStyleSheet("#login_frame {\n"
"    background-color: #EEEEEE;\n"
"    border: 2px solid black;\n"
"    border-radius: 20px;\n"
"}")
        self.login_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_frame.setObjectName("login_frame")
        self.account_frame = QtWidgets.QFrame(self.login_frame)
        self.account_frame.setGeometry(QtCore.QRect(80, 105, 400, 40))
        self.account_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.account_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.account_frame.setObjectName("account_frame")
        self.account_label = QtWidgets.QLabel(self.account_frame)
        self.account_label.setGeometry(QtCore.QRect(0, 0, 100, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.account_label.setFont(font)
        self.account_label.setAlignment(QtCore.Qt.AlignCenter)
        self.account_label.setObjectName("account_label")
        self.account = QtWidgets.QLineEdit(self.account_frame)
        self.account.setGeometry(QtCore.QRect(100, 0, 300, 40))
        self.account.setStyleSheet("background-color: white;\n"
"border: 2px solid gray;\n"
"border-radius: 20px;")
        self.account.setObjectName("account")
        self.key_frame = QtWidgets.QFrame(self.login_frame)
        self.key_frame.setGeometry(QtCore.QRect(80, 175, 400, 40))
        self.key_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.key_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.key_frame.setObjectName("key_frame")
        self.key_label = QtWidgets.QLabel(self.key_frame)
        self.key_label.setGeometry(QtCore.QRect(0, 0, 100, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.key_label.setFont(font)
        self.key_label.setAlignment(QtCore.Qt.AlignCenter)
        self.key_label.setObjectName("key_label")
        self.key = QtWidgets.QLineEdit(self.key_frame)
        self.key.setGeometry(QtCore.QRect(100, 0, 300, 40))
        self.key.setStyleSheet("background-color: white;\n"
"border: 2px solid gray;\n"
"border-radius: 20px;")
        self.key.setObjectName("key")
        self.login_title_frame = QtWidgets.QFrame(self.login_frame)
        self.login_title_frame.setGeometry(QtCore.QRect(0, 0, 660, 70))
        self.login_title_frame.setAutoFillBackground(False)
        self.login_title_frame.setStyleSheet("#login_title_frame {\n"
"    background-color: rgb(0, 170, 255);\n"
"    border: 2px solid black;\n"
"    border-top-left-radius: 20px;\n"
"    border-top-right-radius: 20px;\n"
"}")
        self.login_title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_title_frame.setObjectName("login_title_frame")
        self.login_title = QtWidgets.QLabel(self.login_title_frame)
        self.login_title.setGeometry(QtCore.QRect(245, 0, 170, 70))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.login_title.setFont(font)
        self.login_title.setAlignment(QtCore.Qt.AlignCenter)
        self.login_title.setObjectName("login_title")
        self.login_button = QtWidgets.QPushButton(self.login_frame)
        self.login_button.setGeometry(QtCore.QRect(245, 250, 170, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"border: 2px solid gray;\n"
"border-radius: 20px;")
        self.login_button.setCheckable(True)
        self.login_button.setObjectName("login_button")
        self.logo = QtWidgets.QLabel(Form)
        self.logo.setGeometry(QtCore.QRect(430, 90, 790, 360))
        self.logo.setStyleSheet("")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("assets\\logo.png"))
        self.logo.setObjectName("logo")
        self.background = QtWidgets.QLabel(Form)
        self.background.setGeometry(QtCore.QRect(0, 0, 1651, 951))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("assets\\background.png"))
        self.background.setObjectName("background")
        self.background.raise_()
        self.login_frame.raise_()
        self.logo.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.account_label.setText(_translate("Form", "帳戶："))
        self.key_label.setText(_translate("Form", "金鑰："))
        self.login_title.setText(_translate("Form", "用戶登入"))
        self.login_button.setText(_translate("Form", "登入"))