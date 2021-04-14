# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/window_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(3300, 1900)
        self.identity_frame = QtWidgets.QFrame(Form)
        self.identity_frame.setGeometry(QtCore.QRect(2480, 520, 800, 330))
        self.identity_frame.setStyleSheet("#identity_frame {\n"
"    background-color: #EEEEEE;\n"
"    border: 2px solid black;\n"
"    border-radius: 15px;\n"
"}")
        self.identity_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.identity_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.identity_frame.setObjectName("identity_frame")
        self.identity_frame_title = QtWidgets.QLabel(self.identity_frame)
        self.identity_frame_title.setGeometry(QtCore.QRect(0, 0, 800, 70))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.identity_frame_title.setFont(font)
        self.identity_frame_title.setStyleSheet("background-color: #D0D0D0;\n"
"border: 2px solid black;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"")
        self.identity_frame_title.setTextFormat(QtCore.Qt.PlainText)
        self.identity_frame_title.setAlignment(QtCore.Qt.AlignCenter)
        self.identity_frame_title.setObjectName("identity_frame_title")
        self.name_frame = QtWidgets.QFrame(self.identity_frame)
        self.name_frame.setGeometry(QtCore.QRect(0, 80, 800, 80))
        self.name_frame.setStyleSheet("")
        self.name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.name_frame.setObjectName("name_frame")
        self.name_title = QtWidgets.QLabel(self.name_frame)
        self.name_title.setGeometry(QtCore.QRect(20, 0, 130, 80))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.name_title.setFont(font)
        self.name_title.setAlignment(QtCore.Qt.AlignCenter)
        self.name_title.setObjectName("name_title")
        self.name = QtWidgets.QLineEdit(self.name_frame)
        self.name.setGeometry(QtCore.QRect(150, 8, 630, 60))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(13)
        self.name.setFont(font)
        self.name.setAutoFillBackground(False)
        self.name.setStyleSheet("background-color: white;\n"
"border: 2px solid gray;\n"
"border-radius: 15px;")
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setReadOnly(True)
        self.name.setObjectName("name")
        self.time_frame = QtWidgets.QFrame(self.identity_frame)
        self.time_frame.setGeometry(QtCore.QRect(0, 160, 800, 80))
        self.time_frame.setStyleSheet("")
        self.time_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.time_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.time_frame.setObjectName("time_frame")
        self.time_title = QtWidgets.QLabel(self.time_frame)
        self.time_title.setGeometry(QtCore.QRect(20, 0, 130, 80))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.time_title.setFont(font)
        self.time_title.setAlignment(QtCore.Qt.AlignCenter)
        self.time_title.setObjectName("time_title")
        self.time = QtWidgets.QLineEdit(self.time_frame)
        self.time.setGeometry(QtCore.QRect(150, 10, 630, 60))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(13)
        self.time.setFont(font)
        self.time.setStyleSheet("background-color: white;\n"
"border: 2px solid gray;\n"
"border-radius: 15px;")
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setReadOnly(True)
        self.time.setObjectName("time")
        self.location_frame = QtWidgets.QFrame(self.identity_frame)
        self.location_frame.setGeometry(QtCore.QRect(0, 240, 800, 80))
        self.location_frame.setStyleSheet("")
        self.location_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.location_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.location_frame.setObjectName("location_frame")
        self.location_title = QtWidgets.QLabel(self.location_frame)
        self.location_title.setGeometry(QtCore.QRect(20, 0, 130, 80))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.location_title.setFont(font)
        self.location_title.setAlignment(QtCore.Qt.AlignCenter)
        self.location_title.setObjectName("location_title")
        self.location = QtWidgets.QLineEdit(self.location_frame)
        self.location.setGeometry(QtCore.QRect(150, 10, 630, 60))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(13)
        self.location.setFont(font)
        self.location.setStyleSheet("background-color: white;\n"
"border: 2px solid gray;\n"
"border-radius: 15px;")
        self.location.setAlignment(QtCore.Qt.AlignCenter)
        self.location.setReadOnly(True)
        self.location.setObjectName("location")
        self.records_frame = QtWidgets.QFrame(Form)
        self.records_frame.setGeometry(QtCore.QRect(2480, 870, 800, 1010))
        self.records_frame.setStyleSheet("#records_frame {\n"
"    background-color: #EEEEEE;\n"
"    border: 2px solid black;\n"
"    border-radius: 15px;\n"
"}")
        self.records_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.records_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.records_frame.setObjectName("records_frame")
        self.records_frame_title = QtWidgets.QLabel(self.records_frame)
        self.records_frame_title.setGeometry(QtCore.QRect(0, 0, 800, 70))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.records_frame_title.setFont(font)
        self.records_frame_title.setStyleSheet("background-color: #D0D0D0;\n"
"border: 2px solid black;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"")
        self.records_frame_title.setAlignment(QtCore.Qt.AlignCenter)
        self.records_frame_title.setObjectName("records_frame_title")
        self.records_style_frame = QtWidgets.QFrame(self.records_frame)
        self.records_style_frame.setGeometry(QtCore.QRect(20, 90, 760, 900))
        self.records_style_frame.setStyleSheet("#records_style_frame {\n"
"    background-color: white;\n"
"    border: 2px solid gray;\n"
"    border-radius: 15px;\n"
"}")
        self.records_style_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.records_style_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.records_style_frame.setObjectName("records_style_frame")
        self.records = QtWidgets.QListView(self.records_style_frame)
        self.records.setEnabled(True)
        self.records.setGeometry(QtCore.QRect(20, 20, 720, 860))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.records.setFont(font)
        self.records.setAutoFillBackground(False)
        self.records.setStyleSheet("background-color: white;\n"
"border: 0px;")
        self.records.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.records.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.records.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.records.setMovement(QtWidgets.QListView.Static)
        self.records.setFlow(QtWidgets.QListView.TopToBottom)
        self.records.setProperty("isWrapping", False)
        self.records.setResizeMode(QtWidgets.QListView.Fixed)
        self.records.setViewMode(QtWidgets.QListView.ListMode)
        self.records.setUniformItemSizes(False)
        self.records.setWordWrap(True)
        self.records.setObjectName("records")
        self.picture_frame = QtWidgets.QFrame(Form)
        self.picture_frame.setGeometry(QtCore.QRect(2640, 20, 480, 480))
        self.picture_frame.setStyleSheet("#picture_frame {\n"
"    background-color: #EEEEEE;\n"
"    border: 2px solid black;\n"
"    border-radius: 15px;\n"
"}")
        self.picture_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.picture_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.picture_frame.setObjectName("picture_frame")
        self.picture = QtWidgets.QLabel(self.picture_frame)
        self.picture.setGeometry(QtCore.QRect(20, 20, 440, 440))
        self.picture.setStyleSheet("background-color: white;\n"
"border: 2px solid gray;")
        self.picture.setText("")
        self.picture.setScaledContents(True)
        self.picture.setWordWrap(True)
        self.picture.setObjectName("picture")
        self.camera_style_frame = QtWidgets.QFrame(Form)
        self.camera_style_frame.setGeometry(QtCore.QRect(20, 20, 2440, 1860))
        self.camera_style_frame.setStyleSheet("#camera_style_frame {\n"
"    background-color: #EEEEEE;\n"
"    border: 2px solid black;\n"
"    border-radius: 15px;\n"
"}")
        self.camera_style_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.camera_style_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.camera_style_frame.setObjectName("camera_style_frame")
        self.camera = QtWidgets.QLabel(self.camera_style_frame)
        self.camera.setGeometry(QtCore.QRect(20, 20, 2400, 1820))
        self.camera.setStyleSheet("background-color: white;\n"
"border: 2px solid gray;")
        self.camera.setText("")
        self.camera.setScaledContents(True)
        self.camera.setObjectName("camera")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.identity_frame_title.setText(_translate("Form", "個人資訊"))
        self.name_title.setText(_translate("Form", "姓名："))
        self.time_title.setText(_translate("Form", "時間："))
        self.location_title.setText(_translate("Form", "地點："))
        self.records_frame_title.setText(_translate("Form", "歷史紀錄"))
