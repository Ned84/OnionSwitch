# -*- coding: utf-8 -*-
"""
OnionSwitch | Easily switch the Tor-Exit-Node Destination Country in your Tor-Browser.
Copyright (C) 2019  Ned84 ned84@protonmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""



from PyQt5 import QtCore, QtGui, QtWidgets


version = "0.1"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 300)
        MainWindow.setMinimumSize(QtCore.QSize(450, 300))
        MainWindow.setMaximumSize(QtCore.QSize(450, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/OnionSwitch_Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chooseCountryBox = QtWidgets.QComboBox(self.centralwidget)
        self.chooseCountryBox.setGeometry(QtCore.QRect(20, 50, 411, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.chooseCountryBox.setFont(font)
        self.chooseCountryBox.setObjectName("chooseCountryBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 80, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 110, 450, 171))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName("tabWidget")
        #self.tabWidget.setStyleSheet("QTabBar::tab:selected {background: white;}")
        #self.tabWidget.setStyleSheet("QTabBar::tab { height: 30px; width: 150px; background-color: rgb(89, 49, 107); font: 8pt Arial; selection-background-color: rgb(255, 255, 255);}")  
        stylesheet = """ 
    QTabBar::tab:selected {color: white;}
    QTabBar::tab { height: 30px; width: 150px; background-color: rgb(89, 49, 107); font: 8pt Arial; selection-background-color: rgb(255, 255, 255);}
    """
        self.tabWidget.setStyleSheet(stylesheet)
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.chooseNodeButton = QtWidgets.QPushButton(self.tab1)
        self.chooseNodeButton.setGeometry(QtCore.QRect(190, 100, 111, 28))
        self.chooseNodeButton.setObjectName("chooseNodeButton")
        self.chosenNodeslistView = QtWidgets.QListView(self.tab1)
        self.chosenNodeslistView.setGeometry(QtCore.QRect(310, 0, 141, 141))
        self.chosenNodeslistView.setObjectName("chosenNodeslistView")
        self.onionswitch_logo_frame_2 = QtWidgets.QFrame(self.tab1)
        self.onionswitch_logo_frame_2.setGeometry(QtCore.QRect(10, -10, 120, 110))
        self.onionswitch_logo_frame_2.setStyleSheet("image: url(:/resources/OnionSwitch_Logo.png);")
        self.onionswitch_logo_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.onionswitch_logo_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.onionswitch_logo_frame_2.setObjectName("onionswitch_logo_frame_2")
        self.startTorBrowserButton2 = QtWidgets.QPushButton(self.tab1)
        self.startTorBrowserButton2.setGeometry(QtCore.QRect(10, 100, 121, 28))
        self.startTorBrowserButton2.setObjectName("startTorBrowserButton2")
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.blacklistAllButton = QtWidgets.QPushButton(self.tab2)
        self.blacklistAllButton.setGeometry(QtCore.QRect(190, 100, 111, 28))
        self.blacklistAllButton.setObjectName("blacklistAllButton")
        self.blacklistAllNodeslistView = QtWidgets.QListView(self.tab2)
        self.blacklistAllNodeslistView.setGeometry(QtCore.QRect(310, 0, 141, 141))
        self.blacklistAllNodeslistView.setObjectName("blacklistAllNodeslistView")
        self.onionswitch_logo_frame = QtWidgets.QFrame(self.tab2)
        self.onionswitch_logo_frame.setGeometry(QtCore.QRect(10, -10, 120, 110))
        self.onionswitch_logo_frame.setStyleSheet("image: url(:/resources/OnionSwitch_Logo.png);")
        self.onionswitch_logo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.onionswitch_logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.onionswitch_logo_frame.setObjectName("onionswitch_logo_frame")
        self.startTorBrowserButton = QtWidgets.QPushButton(self.tab2)
        self.startTorBrowserButton.setGeometry(QtCore.QRect(10, 100, 121, 28))
        self.startTorBrowserButton.setObjectName("startTorBrowserButton")
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.blacklistExitNodeslistView = QtWidgets.QListView(self.tab3)
        self.blacklistExitNodeslistView.setGeometry(QtCore.QRect(310, 0, 141, 141))
        self.blacklistExitNodeslistView.setObjectName("blacklistExitNodeslistView")
        self.blacklistExitButton = QtWidgets.QPushButton(self.tab3)
        self.blacklistExitButton.setGeometry(QtCore.QRect(190, 100, 111, 28))
        self.blacklistExitButton.setObjectName("blacklistExitButton")
        self.startTorBrowserButton3 = QtWidgets.QPushButton(self.tab3)
        self.startTorBrowserButton3.setGeometry(QtCore.QRect(10, 100, 121, 28))
        self.startTorBrowserButton3.setObjectName("startTorBrowserButton")
        self.onionswitch_logo_frame3 = QtWidgets.QFrame(self.tab3)
        self.onionswitch_logo_frame3.setGeometry(QtCore.QRect(10, -10, 120, 110))
        self.onionswitch_logo_frame3.setStyleSheet("image: url(:/resources/OnionSwitch_Logo.png);")
        self.onionswitch_logo_frame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.onionswitch_logo_frame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.onionswitch_logo_frame3.setObjectName("onionswitch_logo_frame")
        self.tabWidget.addTab(self.tab3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 450, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.menuHelp.addAction(self.actionUpdate)
        self.menuHelp.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionSettings)
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Choose your Node-Country here:"))
        self.blacklistExitButton.setText(_translate("MainWindow", "Blacklist"))
        self.chooseNodeButton.setText(_translate("MainWindow", "Choose Node"))
        self.startTorBrowserButton2.setText(_translate("MainWindow", "Start Tor-Browser"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Choose Node"))
        self.blacklistAllButton.setText(_translate("MainWindow", "Blacklist"))
        self.startTorBrowserButton.setText(_translate("MainWindow", "Start Tor-Browser"))
        self.startTorBrowserButton3.setText(_translate("MainWindow", "Start Tor-Browser"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Blacklist all Nodes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Blacklist Exit Nodes"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(400, 250)
        AboutDialog.setMinimumSize(QtCore.QSize(400, 250))
        AboutDialog.setMaximumSize(QtCore.QSize(400, 250))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/Ned84_Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutDialog.setWindowIcon(icon)
        self.closeButton = QtWidgets.QPushButton(AboutDialog)
        self.closeButton.setGeometry(QtCore.QRect(290, 210, 93, 28))
        self.closeButton.setObjectName("closeButton")
        self.ned84_logo_frame = QtWidgets.QFrame(AboutDialog)
        self.ned84_logo_frame.setGeometry(QtCore.QRect(0, 50, 141, 131))
        self.ned84_logo_frame.setStyleSheet("image: url(:/resources/Ned84_Logo.png);")
        self.ned84_logo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ned84_logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ned84_logo_frame.setObjectName("ned84_logo_frame")
        self.label = QtWidgets.QLabel(AboutDialog)
        self.label.setGeometry(QtCore.QRect(190, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AboutDialog)
        self.label_2.setGeometry(QtCore.QRect(190, 70, 190, 130))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "Dialog"))
        self.closeButton.setText(_translate("AboutDialog", "Close"))
        self.label.setText(_translate("AboutDialog", "OnionSwitch"))
        self.label_2.setText(_translate("AboutDialog", "Version: xxx\n"
"\n"
"Easily switch the Tor-Exit-Node\n"
"Destination Country in your\n"
"Tor-Browser.\n"
"\n"
"Copyright (C) 2019  Ned84\n"
"ned84@protonmail.com"))

class Ui_FaultDialog(object):
    def setupUi(self, FaultDialog):
        FaultDialog.setObjectName("FaultDialog")
        FaultDialog.resize(400, 150)
        FaultDialog.setMinimumSize(QtCore.QSize(400, 150))
        FaultDialog.setMaximumSize(QtCore.QSize(400, 150))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/OnionSwitch_Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FaultDialog.setWindowIcon(icon)
        self.okButton = QtWidgets.QPushButton(FaultDialog)
        self.okButton.setGeometry(QtCore.QRect(290, 110, 93, 28))
        self.okButton.setObjectName("okButton")
        self.label = QtWidgets.QLabel(FaultDialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(FaultDialog)
        QtCore.QMetaObject.connectSlotsByName(FaultDialog)

    def retranslateUi(self, FaultDialog):
        _translate = QtCore.QCoreApplication.translate
        FaultDialog.setWindowTitle(_translate("FaultDialog", "Dialog"))
        self.okButton.setText(_translate("FaultDialog", "OK"))
        self.label.setText(_translate("FaultDialog", "Could not find the Tor-Browser.\n"
"Please ensure the correct Path in the settings."))

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(400, 250)
        SettingsDialog.setMinimumSize(QtCore.QSize(400, 250))
        SettingsDialog.setMaximumSize(QtCore.QSize(400, 250))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/OnionSwitch_Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SettingsDialog.setWindowIcon(icon)
        self.okButton = QtWidgets.QPushButton(SettingsDialog)
        self.okButton.setGeometry(QtCore.QRect(180, 210, 93, 28))
        self.okButton.setObjectName("okButton")
        self.cancelButton = QtWidgets.QPushButton(SettingsDialog)
        self.cancelButton.setGeometry(QtCore.QRect(290, 210, 93, 28))
        self.cancelButton.setObjectName("cancelButton")
        self.lineEdit = QtWidgets.QLineEdit(SettingsDialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 361, 22))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(SettingsDialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.openButton = QtWidgets.QPushButton(SettingsDialog)
        self.openButton.setGeometry(QtCore.QRect(290, 80, 93, 28))
        self.openButton.setObjectName("openButton")
        self.onionswitch_logo_frame = QtWidgets.QFrame(SettingsDialog)
        self.onionswitch_logo_frame.setGeometry(QtCore.QRect(10, 110, 141, 131))
        self.onionswitch_logo_frame.setStyleSheet("image: url(:/resources/OnionSwitch_Logo.png);")
        self.onionswitch_logo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.onionswitch_logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.onionswitch_logo_frame.setObjectName("onionswitch_logo_frame")

        self.retranslateUi(SettingsDialog)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Dialog"))
        self.okButton.setText(_translate("SettingsDialog", "OK"))
        self.cancelButton.setText(_translate("SettingsDialog", "Cancel"))
        self.label.setText(_translate("SettingsDialog", "Path to Tor-Browser:"))
        self.openButton.setText(_translate("SettingsDialog", "Open"))

class Ui_UpdateDialog(object):
    def setupUi(self, UpdateDialog):
        UpdateDialog.setObjectName("UpdateDialog")
        UpdateDialog.resize(400, 250)
        UpdateDialog.setMinimumSize(QtCore.QSize(400, 250))
        UpdateDialog.setMaximumSize(QtCore.QSize(400, 250))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/OnionSwitch_Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UpdateDialog.setWindowIcon(icon)
        self.Cancel = QtWidgets.QPushButton(UpdateDialog)
        self.Cancel.setGeometry(QtCore.QRect(290, 210, 93, 28))
        self.Cancel.setObjectName("Cancel")
        self.updateButton = QtWidgets.QPushButton(UpdateDialog)
        self.updateButton.setGeometry(QtCore.QRect(180, 210, 93, 28))
        self.updateButton.setObjectName("updateButton")
        self.onionswitch_logo_frame = QtWidgets.QFrame(UpdateDialog)
        self.onionswitch_logo_frame.setGeometry(QtCore.QRect(0, 50, 141, 131))
        self.onionswitch_logo_frame.setStyleSheet("image: url(:/resources/OnionSwitch_Logo.png);")
        self.onionswitch_logo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.onionswitch_logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.onionswitch_logo_frame.setObjectName("onionswitch_logo_frame")
        self.label = QtWidgets.QLabel(UpdateDialog)
        self.label.setGeometry(QtCore.QRect(190, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(UpdateDialog)
        QtCore.QMetaObject.connectSlotsByName(UpdateDialog)

    def retranslateUi(self, UpdateDialog):
        _translate = QtCore.QCoreApplication.translate
        UpdateDialog.setWindowTitle(_translate("UpdateDialog", "Dialog"))
        self.Cancel.setText(_translate("UpdateDialog", "Cancel"))
        self.updateButton.setText(_translate("UpdateDialog", "Update"))
        self.label.setText(_translate("UpdateDialog", "OnionSwitch"))



import OnionSwitchResources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())