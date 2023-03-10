# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pbgui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

app = None


class Ui_MainWindow(object):

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

    def setupUi(self, ParamsWindow):
        ParamsWindow.setObjectName("ParamsWindow")
        ParamsWindow.setWindowModality(QtCore.Qt.NonModal)
        ParamsWindow.resize(340, 420)

        self.centralwidget = QtWidgets.QWidget(ParamsWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 311, 350))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(132, 380, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(
            QtCore.QCoreApplication.instance().quit)
        self.pushButton.setText('Guardar')

        self.setupLetters()

        ParamsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ParamsWindow)
        QtCore.QMetaObject.connectSlotsByName(ParamsWindow)

    def retranslateUi(self, ParamsWindow):
        _translate = QtCore.QCoreApplication.translate
        ParamsWindow.setWindowTitle(_translate(
            "ParamsWindow", "Configuraci??n Costo Itermedio"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ParamsWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(ParamsWindow)
    ParamsWindow.show()
    sys.exit(app.exec_())
