# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/startup_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(3300, 1900)
        Form.setStyleSheet("")
        self.login_frame = QtWidgets.QFrame(Form)
        self.login_frame.setGeometry(QtCore.QRect(1000, 1000, 1320, 680))
        self.login_frame.setStyleSheet("#login_frame {\n"
"    background-color: #EEEEEE;\n"
"    border: 2px solid black;\n"
"    border-radius: 20px;\n"
"}")
        self.login_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_frame.setObjectName("login_frame")
        self.account_frame = QtWidgets.QFrame(self.login_frame)
        self.account_frame.setGeometry(QtCore.QRect(160, 210, 800, 80))
        self.account_frame.setStyleSheet("#account_frame {\n"
"    border: 0px;\n"
"}")
        self.account_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.account_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.account_frame.setObjectName("account_frame")
        self.account_label = QtWidgets.QLabel(self.account_frame)
        self.account_label.setGeometry(QtCore.QRect(0, 0, 200, 80))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.account_label.setFont(font)
        self.account_label.setAlignment(QtCore.Qt.AlignCenter)
        self.account_label.setObjectName("account_label")
        self.account = QtWidgets.QLineEdit(self.account_frame)
        self.account.setGeometry(QtCore.QRect(200, 0, 600, 80))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(14)
        self.account.setFont(font)
        self.account.setStyleSheet("background-color: white;\n"
"border: 2px solid gray;\n"
"border-radius: 20px;")
        self.account.setText("")
        self.account.setCursorPosition(0)
        self.account.setAlignment(QtCore.Qt.AlignCenter)
        self.account.setObjectName("account")
        self.key_frame = QtWidgets.QFrame(self.login_frame)
        self.key_frame.setGeometry(QtCore.QRect(160, 350, 800, 80))
        self.key_frame.setStyleSheet("#key_frame {\n"
"    border: 0px;\n"
"}")
        self.key_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.key_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.key_frame.setObjectName("key_frame")
        self.key_label = QtWidgets.QLabel(self.key_frame)
        self.key_label.setGeometry(QtCore.QRect(0, 0, 200, 80))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.key_label.setFont(font)
        self.key_label.setAlignment(QtCore.Qt.AlignCenter)
        self.key_label.setObjectName("key_label")
        self.key = QtWidgets.QLineEdit(self.key_frame)
        self.key.setGeometry(QtCore.QRect(200, 0, 600, 80))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(14)
        self.key.setFont(font)
        self.key.setStyleSheet("background-color: white;\n"
"border: 2px solid gray;\n"
"border-radius: 20px;")
        self.key.setEchoMode(QtWidgets.QLineEdit.Password)
        self.key.setCursorPosition(0)
        self.key.setAlignment(QtCore.Qt.AlignCenter)
        self.key.setObjectName("key")
        self.login_title_frame = QtWidgets.QFrame(self.login_frame)
        self.login_title_frame.setGeometry(QtCore.QRect(0, 0, 1320, 140))
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
        self.login_title.setGeometry(QtCore.QRect(490, 0, 340, 140))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK HK")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.login_title.setFont(font)
        self.login_title.setAlignment(QtCore.Qt.AlignCenter)
        self.login_title.setObjectName("login_title")
        self.login_button = QtWidgets.QPushButton(self.login_frame)
        self.login_button.setGeometry(QtCore.QRect(490, 500, 340, 100))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"border: 2px solid gray;\n"
"border-radius: 20px;")
        self.login_button.setCheckable(True)
        self.login_button.setObjectName("login_button")
        self.logo = QtWidgets.QLabel(Form)
        self.logo.setGeometry(QtCore.QRect(860, 180, 1580, 720))
        self.logo.setStyleSheet("")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setWordWrap(True)
        self.logo.setObjectName("assets/logo")
        self.background = QtWidgets.QLabel(Form)
        self.background.setGeometry(QtCore.QRect(0, 0, 3300, 1900))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("assets/background.png"))
        self.background.setScaledContents(True)
        self.background.setWordWrap(True)
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

