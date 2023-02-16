from PyQt5 import QtCore, QtGui, QtWidgets


class UiMenuBar(object):
    def __init__(self, container):
        self.container = container
        self.setupUi()

    def setupUi(self):
        self.menubar = QtWidgets.QMenuBar(self.container)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 21))
        self.menubar.setObjectName("menubar")

        self.menu_Archivo = QtWidgets.QMenu(self.menubar)
        self.menu_Archivo.setObjectName("menu_Archivo")

        self.actionImportar = QtWidgets.QAction(self.container)
        self.actionImportar.setObjectName("actionImportar")
        self.menu_Archivo.addAction(self.actionImportar)
        self.menubar.addAction(self.menu_Archivo.menuAction())

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.menu_Archivo.setTitle(_translate("MainWindow", "&Archivo"))
        self.actionImportar.setText(_translate("MainWindow", "Importar"))
