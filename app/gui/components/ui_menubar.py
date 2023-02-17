from PyQt5 import QtCore, QtGui, QtWidgets
from ..menus.ci_settings import Ui_CiSettings


class Ui_MenuBar(object):
    def __init__(self, container):
        self.container = container
        self.setupUi()

    def setUpFileMenu(self):
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")

        self.action_Import = QtWidgets.QAction(self.container)
        self.action_Import.setObjectName("action_Import")

        self.menu_File.addAction(self.action_Import)
        self.menubar.addAction(self.menu_File.menuAction())

    def setUpSettingsMenu(self):
        self.menu_Settings = QtWidgets.QMenu(self.menubar)
        self.menu_Settings.setObjectName("menu_Settings")

        self.action_SettingCi = QtWidgets.QAction(self.container)
        self.action_SettingCi.setObjectName("action_SettingCi")
        self.action_SettingCi.triggered.connect(self.showCiSettingsView)

        self.menu_Settings.addAction(self.action_SettingCi)
        self.menubar.addAction(self.menu_Settings.menuAction())

    def setupUi(self):
        self.menubar = QtWidgets.QMenuBar(self.container)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 21))
        self.menubar.setObjectName("menubar")
        self.setUpFileMenu()
        self.setUpSettingsMenu()
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.menu_File.setTitle(_translate("MainWindow", "&Archivo"))
        self.menu_Settings.setTitle(
            _translate("MainWindow", "&Configuración"))
        self.action_Import.setText(_translate("MainWindow", "Importar"))
        self.action_SettingCi.setText(
            _translate("MainWindow", "Costo intermedio"))

    def showCiSettingsView(self):
        print('intentando')
        settings = Ui_CiSettings()
        settings.show()
