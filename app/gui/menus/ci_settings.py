# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pbgui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CiSettings(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupLetters(self):
        for letter in 'ABCDEFGHIJKLMNOP':
            horizontalLayoutLetter = QtWidgets.QHBoxLayout()
            horizontalLayoutLetter.setObjectName(
                'horizontalLayoutLetter_' + letter)

            labelLetter = QtWidgets.QLabel(self.verticalLayoutWidget)
            labelLetter.setObjectName('labelLetter_' + letter)
            labelLetter.setText('Letra ' + letter + ':')

            doubleSpinBox = QtWidgets.QDoubleSpinBox(
                self.verticalLayoutWidget)
            doubleSpinBox.setObjectName('doubleSpinBoxLetter_' + letter)

            horizontalLayoutLetter.addWidget(labelLetter)
            horizontalLayoutLetter.addWidget(doubleSpinBox)
            self.verticalLayout.addLayout(horizontalLayoutLetter)
#

    def setupUi(self):
        # ParamsWindow.setObjectName("ParamsWindow")
        # ParamsWindow.setWindowModality(QtCore.Qt.WindowModality)
        # ParamsWindow.resize(340, 420)

        # self.centralwidget = QtWidgets.QWidget(ParamsWindow)
        # self.centralwidget.setObjectName("centralwidget")

        # self.verticalLayoutWidget = QtWidgets.QWidget()
        # self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 311, 350))
        # self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        # self.verticalLayout = QtWidgets.QVBoxLayout()
        # self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        # self.verticalLayout.setObjectName("verticalLayout")
        layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)

        # self.pushButton = QtWidgets.QPushButton(self)
        # self.pushButton.setGeometry(QtCore.QRect(132, 380, 75, 23))
        # self.pushButton.setObjectName("pushButton")
        # self.pushButton.clicked.connect(
        #     QtCore.QCoreApplication.instance().quit)
        # self.pushButton.setText('Guardar')

        # self.setupLetters()

        # self.setLayout(self.verticalLayout)

        # ParamsWindow.setCentralWidget(self.centralwidget)
