# -*- coding: utf-8 -*-
"""
OnionSwitch | Easily switch the Tor-Exit-Node Destination Country in
your Tor-Browser.
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
import json
import os
from os import path
import threading
import webbrowser
from urllib import request
import platform
from shutil import copyfile

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QFileDialog
from PyQt5.Qt import QApplication

import OnionSwitch_Functions as osf
import OnionSwitch_TorCheck as ostc
import OnionSwitchResources_rc

version = "1.1"


class Ui_MainWindow(QtWidgets.QWidget):

    serverconnection = False
    versionnew = ""
    versioncheckdone = False
    firstrun = True

    OnionSwitchResources_rc.qInitResources()

    def __init__(self, *args, **kwargs):
        try:
            super().__init__()

            osf.Functions.paramplatform = platform.system()
            osf.Functions.paramversion = version

            if osf.Functions.paramplatform == "Windows":
                osf.Functions.pathtoparam = os.getenv(
                    'LOCALAPPDATA') + '\\OnionSwitch\\osparam'
                osf.Functions.pathtolog = os.getenv(
                    'LOCALAPPDATA') + '\\OnionSwitch\\logfiles'
                osf.Functions.pathtomain = os.getenv(
                    'LOCALAPPDATA') + '\\OnionSwitch'
                osf.Functions.pathseparator = "\\"

            if osf.Functions.paramplatform == "Linux":
                osf.Functions.pathtoparam = os.path.dirname(
                    os.path.abspath(__file__)) + '/OnionSwitch/osparam'
                osf.Functions.pathtolog = os.path.dirname(
                    os.path.abspath(__file__)) + '/OnionSwitch/logfiles'
                osf.Functions.pathtomain = os.path.dirname(
                    os.path.abspath(__file__)) + '/OnionSwitch'
                osf.Functions.pathseparator = "/"

            if path.exists(osf.Functions.pathtomain) is False:
                os.mkdir(osf.Functions.pathtomain)

            if path.exists(osf.Functions.pathtoparam) is False:
                os.mkdir(osf.Functions.pathtoparam)

            if path.exists(osf.Functions.pathtolog) is False:
                os.mkdir(osf.Functions.pathtolog)

            if path.exists(
                    osf.Functions.pathtoparam + osf.Functions.pathseparator +
                    'Param.json') is False:

                with open(
                    osf.Functions.pathtoparam + osf.Functions.pathseparator +
                        'Param.json', "w+") as file:

                    data = [{"version": version, "Path_to_Tor": "",
                            "Update_available": False, "StrictNodes": 1,
                             "Platform": "", "StemCheck": False}]

                    json.dump(data, file, indent=1, sort_keys=True)

            if path.exists(
                osf.Functions.pathtolog + osf.Functions.pathseparator +
                    'oslog.txt') is False:

                with open(
                    osf.Functions.pathtolog + osf.Functions.pathseparator +
                        'oslog.txt', "w+") as file:
                    pass

            osf.Functions.GetSettingsFromJson(self)

        except Exception as exc:
            osf.Functions.WriteLog(self, exc)
        try:
            def UpdateCheck():
                link = ("https://github.com/Ned84/OnionSwitch/blob/master/" +
                        "VERSION.md")
                url = request.urlopen(link)
                readurl = url.read()
                text = readurl.decode(encoding='utf-8', errors='ignore')
                stringindex = text.find("OnionSwitchVersion")

                if stringindex != -1:
                    Ui_MainWindow.versionnew = text[stringindex +
                                                    20:stringindex + 23]
                    Ui_MainWindow.versionnew = \
                        Ui_MainWindow.versionnew.replace('_', '.')

                if version < Ui_MainWindow.versionnew:
                    Ui_MainWindow.serverconnection = True
                    osf.Functions.paramupdateavailable = True
                    Ui_MainWindow.versioncheckdone = True

                else:
                    Ui_MainWindow.serverconnection = True
                    osf.Functions.paramupdateavailable = False
                    Ui_MainWindow.versioncheckdone = True

                osf.Functions.WriteSettingsToJson(self)

            urlthread = threading.Thread(target=UpdateCheck, daemon=True)
            urlthread.start()

        except Exception:
            osf.Functions.paramupdateavailable = False
            Ui_MainWindow.versioncheckdone = True

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("OnionSwitch")
        MainWindow.resize(525, 300)
        MainWindow.setMinimumSize(QtCore.QSize(525, 300))
        MainWindow.setMaximumSize(QtCore.QSize(525, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/OnionSwitch_w_w_bgr.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chooseCountryBox = QtWidgets.QComboBox(self.centralwidget)
        self.chooseCountryBox.setGeometry(QtCore.QRect(113, 50, 300, 22))
        self.chooseCountryBox.addItems(osf.Functions.countrynames)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.chooseCountryBox.setFont(font)
        self.chooseCountryBox.setObjectName("chooseCountryBox")
        self.strictnodesCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.strictnodesCheckBox.setGeometry(QtCore.QRect(250, 81, 311, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.strictnodesCheckBox.setFont(font)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 311, 21))
        self.updatelabel = QtWidgets.QLabel(self.centralwidget)
        self.updatelabel.setGeometry(QtCore.QRect(20, 60, 100, 35))
        font2 = QtGui.QFont()
        font2.setFamily("Arial")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.updatelabel.setStyleSheet("color: rgb(89, 49, 107)")
        self.updatelabel.setFont(font2)
        self.updatelabel.hide()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(113, 80, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 110, 525, 171))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName("tabWidget")
        stylesheet = """
    QTabBar::tab:selected {color: white;}
    QTabBar::tab { height: 30px; width: 175px;
    background-color: rgb(89, 49, 107); font: 10pt Arial;
    selection-background-color: rgb(255, 255, 255);}
    """
        self.tabWidget.setStyleSheet(stylesheet)
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.chooseNodeButton = QtWidgets.QPushButton(self.tab1)
        self.chooseNodeButton.setGeometry(QtCore.QRect(264, 100, 111, 28))
        self.chooseNodeButton.setObjectName("chooseNodeButton")
        self.onionswitch_logo_frame_2 = QtWidgets.QFrame(self.tab1)
        self.onionswitch_logo_frame_2.setGeometry(QtCore.QRect(
            10, 0, 120, 110))
        self.onionswitch_logo_frame_2.setStyleSheet(
            "image: url(:/resources/OnionSwitch_Logo.png);")
        self.onionswitch_logo_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.onionswitch_logo_frame_2.setObjectName("onionswitch_logo_frame_2")
        self.startTorBrowserButton2 = QtWidgets.QPushButton(self.tab1)
        self.startTorBrowserButton2.setGeometry(QtCore.QRect(10, 100, 121, 28))
        self.startTorBrowserButton2.setObjectName("startTorBrowserButton2")
        self.tabWidget.addTab(self.tab1, "")
        self.chosenNodesTableView = QtWidgets.QTableWidget(self.tab1)
        self.chosenNodesTableView.setGeometry(QtCore.QRect(384, -1, 141, 134))
        self.chosenNodesTableView.setObjectName("chosenNodesTableView")
        self.chosenNodesTableView.setRowCount(4)
        self.chosenNodesTableView.setColumnCount(1)
        self.chosenNodesTableView.horizontalHeader().hide()
        self.chosenNodesTableView.verticalHeader().hide()
        self.chosenNodesTableView.setShowGrid(False)
        self.chosenNodesTableView.setEditTriggers(
            self.chosenNodesTableView.NoEditTriggers)
        self.chosenNodesTableView.setItem(
            0, 0, QtWidgets.QTableWidgetItem("Tor not found."))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.chosenNodesTableView.setFont(font)
        self.chosenNodesTableView.setColumnWidth(1, 141)
        self.chosenNodesTableView.resizeRowsToContents()
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.blacklistAllButton = QtWidgets.QPushButton(self.tab2)
        self.blacklistAllButton.setGeometry(QtCore.QRect(264, 100, 111, 28))
        self.blacklistAllButton.setObjectName("blacklistAllButton")
        self.blacklistAllNodesTableView = QtWidgets.QTableWidget(self.tab2)
        self.blacklistAllNodesTableView.setGeometry(QtCore.QRect(
            384, -1, 141, 134))
        self.blacklistAllNodesTableView.setObjectName(
            "blacklistAllNodesTableView")
        self.blacklistAllNodesTableView.setRowCount(4)
        self.blacklistAllNodesTableView.setColumnCount(1)
        self.blacklistAllNodesTableView.horizontalHeader().hide()
        self.blacklistAllNodesTableView.verticalHeader().hide()
        self.blacklistAllNodesTableView.setShowGrid(False)
        self.blacklistAllNodesTableView.setEditTriggers(
            self.chosenNodesTableView.NoEditTriggers)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.blacklistAllNodesTableView.setFont(font)
        self.blacklistAllNodesTableView.setColumnWidth(1, 141)
        self.blacklistAllNodesTableView.resizeRowsToContents()
        self.blacklistAllNodesTableView.setItem(
            0, 0, QtWidgets.QTableWidgetItem("Tor not found."))
        self.onionswitch_logo_frame = QtWidgets.QFrame(self.tab2)
        self.onionswitch_logo_frame.setGeometry(
            QtCore.QRect(10, 0, 120, 110))
        self.onionswitch_logo_frame.setStyleSheet(
            "image: url(:/resources/OnionSwitch_Logo.png);")
        self.onionswitch_logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.onionswitch_logo_frame.setObjectName("onionswitch_logo_frame")
        self.startTorBrowserButton = QtWidgets.QPushButton(self.tab2)
        self.startTorBrowserButton.setGeometry(QtCore.QRect(10, 100, 121, 28))
        self.startTorBrowserButton.setObjectName("startTorBrowserButton")
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.blacklistExitNodesTableView = QtWidgets.QTableWidget(self.tab3)
        self.blacklistExitNodesTableView.setGeometry(QtCore.QRect(
            384, -1, 141, 134))
        self.blacklistExitNodesTableView.setObjectName(
            "blacklistExitNodesTableView")
        self.blacklistExitNodesTableView.setRowCount(4)
        self.blacklistExitNodesTableView.setColumnCount(1)
        self.blacklistExitNodesTableView.horizontalHeader().hide()
        self.blacklistExitNodesTableView.verticalHeader().hide()
        self.blacklistExitNodesTableView.setShowGrid(False)
        self.blacklistExitNodesTableView.setEditTriggers(
            self.chosenNodesTableView.NoEditTriggers)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.blacklistExitNodesTableView.setFont(font)
        self.blacklistExitNodesTableView.setColumnWidth(1, 141)
        self.blacklistExitNodesTableView.resizeRowsToContents()
        self.blacklistExitNodesTableView.setItem(
            0, 0, QtWidgets.QTableWidgetItem("Tor not found."))
        self.blacklistExitButton = QtWidgets.QPushButton(self.tab3)
        self.blacklistExitButton.setGeometry(QtCore.QRect(264, 100, 111, 28))
        self.blacklistExitButton.setObjectName("blacklistExitButton")
        self.startTorBrowserButton3 = QtWidgets.QPushButton(self.tab3)
        self.startTorBrowserButton3.setGeometry(QtCore.QRect(10, 100, 121, 28))
        self.startTorBrowserButton3.setObjectName("startTorBrowserButton")
        self.onionswitch_logo_frame3 = QtWidgets.QFrame(self.tab3)
        self.onionswitch_logo_frame3.setGeometry(QtCore.QRect(
            10, 0, 120, 110))
        self.onionswitch_logo_frame3.setStyleSheet(
            "image: url(:/resources/OnionSwitch_Logo.png);")
        self.onionswitch_logo_frame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.onionswitch_logo_frame3.setObjectName("onionswitch_logo_frame")
        self.tabWidget.addTab(self.tab3, "")
        self.faultLabel = QtWidgets.QLabel(self.centralwidget)
        self.faultLabel.setGeometry(QtCore.QRect(140, 150, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.faultLabel.setFont(font)
        self.faultLabel.setObjectName("faultLabel")
        self.sameNodeInMultiArrayFaultLabel = QtWidgets.QLabel(
            self.centralwidget)
        self.sameNodeInMultiArrayFaultLabel.setGeometry(
            QtCore.QRect(140, 150, 200, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sameNodeInMultiArrayFaultLabel.setFont(font)
        self.sameNodeInMultiArrayFaultLabel.setObjectName(
            "sameNodeInMultiArrayFaultLabel")
        self.sameNodeInMultiArrayFaultLabel.hide()
        self.cantConnectToNodeFaultLabel = QtWidgets.QLabel(
            self.centralwidget)
        self.cantConnectToNodeFaultLabel.setGeometry(
            QtCore.QRect(140, 150, 200, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cantConnectToNodeFaultLabel.setFont(font)
        self.cantConnectToNodeFaultLabel.setObjectName(
            "cantConnectToNodeFaultLabel")
        self.cantConnectToNodeFaultLabel.hide()
        self.standbyLabel = QtWidgets.QLabel(
            self.tab1)
        self.standbyLabel.setGeometry(
            QtCore.QRect(175, 10, 200, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.standbyLabel.setFont(font)
        self.standbyLabel.setObjectName(
            "standbyLabel")
        self.resettorrcButton = QtWidgets.QPushButton(self.centralwidget)
        self.resettorrcButton.setGeometry(QtCore.QRect(267, 241, 111, 28))
        self.resettorrcButton.hide()
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
        self.actionMetrics = QtWidgets.QAction(MainWindow)
        self.actionMetrics.setObjectName("actionMetrics")
        self.actionResetTorrc = QtWidgets.QAction(MainWindow)
        self.actionResetTorrc.setObjectName("actionResetTorrc")
        self.menuHelp.addAction(self.actionMetrics)
        self.menuHelp.addAction(self.actionResetTorrc)
        self.menuHelp.addAction(self.actionUpdate)
        self.menuHelp.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionSettings)
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tabWidget.setCurrentWidget(self.tabWidget.findChild(
            QtWidgets.QWidget, "tab1"))

        @pyqtSlot()
        def ResetTorrc():
            try:
                if osf.Functions.torrcfound is True:

                    self.lineEdit.setText("")

                    if osf.Functions.paramplatform == "Windows":
                        if path.exists(osf.Functions.pathtoparam + '\\rccy')\
                             is True:
                            os.remove(osf.Functions.torrcfilepath)

                            copyfile(osf.Functions.pathtoparam + '\\rccy',
                                     osf.Functions.torrcfilepath)

                    if osf.Functions.paramplatform == "Linux":
                        if path.exists(osf.Functions.pathtoparam + '/rccy')\
                             is True:
                            os.remove(osf.Functions.torrcfilepath)

                            copyfile(osf.Functions.pathtoparam + '/rccy',
                                     osf.Functions.torrcfilepath)

                    osf.Functions.GetTorrcFromFile(self)
                    AddNodeToChosenNodeTableView()
                    AddNodeToBlackListAllTableView()
                    AddNodeToBlackListExitTableView()

            except Exception as exc:
                osf.Functions.WriteLog(self, exc)

        @pyqtSlot()
        def ChangeStrictNodes():
            # Change the strictnodes in the torrc file
            # depending on the checkbox
            if self.strictnodesCheckBox.isChecked() is True:
                osf.Functions.torrcstrictnodes = True
                osf.Functions.paramstrictnodes = 1
            else:
                osf.Functions.torrcstrictnodes = False
                osf.Functions.paramstrictnodes = 0
            osf.Functions.ChangeTorrcStrictNodes(self)
            osf.Functions.WriteSettingsToJson(self)

        @pyqtSlot()
        def ChangeCountry():
            # Change the display in the LineEdit after a Country is
            # chosen in the dropdown.
            self.lineEdit.setText("{0}".format(
                osf.Functions.ChangeCountrynameToCountrycode(
                    self, self.chooseCountryBox.currentText())))

        @pyqtSlot()
        def AddNodeToChosenNodeTableView():
            # Write the countrycodes in the ChosenNodesTableView and Torrc
            if osf.Functions.torrcfound is True:
                found = False
                countrycode = osf.Functions.ChangeCountrycodeToCountryname(
                    self, self.lineEdit.text())
                for code in osf.Functions.torrcexcludedexitnodes:
                    if code == countrycode:
                        found = True
                for code in osf.Functions.torrcexcludednodes:
                    if code == countrycode:
                        found = True

                if found is False:
                    for code in osf.Functions.torrcexitnodes:
                        if code == countrycode:
                            found = True

                    if found is False:
                        if (Ui_MainWindow.firstrun is False) and (
                                osf.Functions.settingschanged is False):
                            connection_count = 0

                            ostc.TorCheck.CheckTor(
                                self, self.lineEdit.text(),
                                osf.Functions.paramplatform,
                                osf.Functions.paramstemcheck,
                                osf.Functions.parampathtotor)

                            if ostc.TorCheck.connected is False:
                                connection_count = 0
                            else:
                                connection_count += 1
                        else:
                            connection_count = 1
                            Ui_MainWindow.firstrun = False

                        if connection_count != 0:
                            self.sameNodeInMultiArrayFaultLabel.hide()

                            osf.Functions.torrcexitnodes = \
                                osf.Functions.AddCountryToArray(
                                    self,
                                    osf.Functions.
                                    ChangeCountrycodeToCountryname(
                                        self, self.lineEdit.text()),
                                    osf.Functions.torrcexitnodes)

                            i = 0
                            self.chosenNodesTableView.setRowCount(len(
                                osf.Functions.torrcexitnodes))
                            for nodes in osf.Functions.torrcexitnodes:
                                self.chosenNodesTableView.setItem(
                                    0, i, QtWidgets.QTableWidgetItem(
                                        osf.Functions.torrcexitnodes[i]))
                                i += 1
                            self.chosenNodesTableView.resizeRowsToContents()

                            osf.Functions.WriteNodesToTorrc(
                                self,
                                "ExitNodes", osf.Functions.torrcexitnodes)
                        else:
                            self.cantConnectToNodeFaultLabel.show()
                            self.standbyLabel.hide()

                else:
                    self.sameNodeInMultiArrayFaultLabel.show()
                    self.standbyLabel.hide()

        @pyqtSlot()
        def AddNodeToBlackListExitTableView():
            if osf.Functions.torrcfound is True:
                found = False
                countrycode = osf.Functions.ChangeCountrycodeToCountryname(
                    self, self.lineEdit.text())
                for code in osf.Functions.torrcexitnodes:
                    if code == countrycode:
                        found = True

                if found is False:
                    self.sameNodeInMultiArrayFaultLabel.hide()

                    osf.Functions.torrcexcludedexitnodes = \
                        osf.Functions.AddCountryToArray(
                            self, osf.Functions.ChangeCountrycodeToCountryname(
                                self, self.lineEdit.text()),
                            osf.Functions.torrcexcludedexitnodes)

                    i = 0
                    self.blacklistExitNodesTableView.setRowCount(len(
                        osf.Functions.torrcexcludedexitnodes))
                    for nodes in osf.Functions.torrcexcludedexitnodes:
                        self.blacklistExitNodesTableView.setItem(
                            0, i, QtWidgets.QTableWidgetItem(
                                osf.Functions.torrcexcludedexitnodes[i]))
                        i += 1
                    self.blacklistExitNodesTableView.resizeRowsToContents()

                    osf.Functions.WriteNodesToTorrc(
                        self, "ExcludeExitNodes",
                        osf.Functions.torrcexcludedexitnodes)

                else:
                    self.sameNodeInMultiArrayFaultLabel.show()
                    self.standbyLabel.hide()

        @pyqtSlot()
        def AddNodeToBlackListAllTableView():
            if osf.Functions.torrcfound is True:

                found = False
                countrycode = osf.Functions.ChangeCountrycodeToCountryname(
                    self, self.lineEdit.text())
                for code in osf.Functions.torrcexitnodes:
                    if code == countrycode:
                        found = True

                if found is False:
                    self.sameNodeInMultiArrayFaultLabel.hide()

                    osf.Functions.torrcexcludednodes = \
                        osf.Functions.AddCountryToArray(
                            self, osf.Functions.ChangeCountrycodeToCountryname(
                                self, self.lineEdit.text()),
                            osf.Functions.torrcexcludednodes)

                    i = 0
                    self.blacklistAllNodesTableView.setRowCount(len(
                        osf.Functions.torrcexcludednodes))
                    for nodes in osf.Functions.torrcexcludednodes:
                        self.blacklistAllNodesTableView.setItem(
                            0, i, QtWidgets.QTableWidgetItem(
                                osf.Functions.torrcexcludednodes[i]))
                        i += 1
                    self.blacklistAllNodesTableView.resizeRowsToContents()

                    osf.Functions.WriteNodesToTorrc(
                        self, "ExcludeNodes", osf.Functions.torrcexcludednodes)

                else:
                    self.sameNodeInMultiArrayFaultLabel.show()
                    self.standbyLabel.hide()

        @pyqtSlot()
        def DeleteNodeFromchosenNodeTableView():
            if osf.Functions.torrcfound is True:
                for currentQTableWidgetItem in \
                        self.chosenNodesTableView.selectedItems():
                    osf.Functions.torrcexitnodes = \
                        osf.Functions.DeleteCountryFromArray(
                            self, currentQTableWidgetItem.text(),
                            osf.Functions.torrcexitnodes)

                i = 0
                self.chosenNodesTableView.setRowCount(
                    len(osf.Functions.torrcexitnodes))
                for nodes in osf.Functions.torrcexitnodes:
                    self.chosenNodesTableView.setItem(
                        0, i, QtWidgets.QTableWidgetItem(
                            osf.Functions.torrcexitnodes[i]))
                    i += 1
                self.chosenNodesTableView.resizeRowsToContents()

                osf.Functions.WriteNodesToTorrc(
                    self, "ExitNodes", osf.Functions.torrcexitnodes)

                countrycode = osf.Functions.ChangeCountrycodeToCountryname(
                    self, self.lineEdit.text())
                self.sameNodeInMultiArrayFaultLabel.hide()
                self.standbyLabel.show()
                self.cantConnectToNodeFaultLabel.hide()
                for code in osf.Functions.torrcexcludednodes:
                    if code == countrycode:
                        self.sameNodeInMultiArrayFaultLabel.show()
                        self.standbyLabel.hide()
                for code in osf.Functions.torrcexcludedexitnodes:
                    if code == countrycode:
                        self.sameNodeInMultiArrayFaultLabel.show()
                        self.standbyLabel.hide()

        @pyqtSlot()
        def DeleteNodeFromBlacklistExitTableView():
            if osf.Functions.torrcfound is True:
                for currentQTableWidgetItem in \
                        self.blacklistExitNodesTableView.selectedItems():
                    osf.Functions.torrcexcludedexitnodes = \
                        osf.Functions.DeleteCountryFromArray(
                            self, currentQTableWidgetItem.text(),
                            osf.Functions.torrcexcludedexitnodes)

                i = 0
                self.blacklistExitNodesTableView.setRowCount(
                    len(osf.Functions.torrcexcludedexitnodes))
                for nodes in osf.Functions.torrcexcludedexitnodes:
                    self.blacklistExitNodesTableView.setItem(
                        0, i, QtWidgets.QTableWidgetItem(
                            osf.Functions.torrcexcludedexitnodes[i]))
                    i += 1
                self.blacklistExitNodesTableView.resizeRowsToContents()

                osf.Functions.WriteNodesToTorrc(
                    self, "ExcludeExitNodes",
                    osf.Functions.torrcexcludedexitnodes)

                countrycode = osf.Functions.ChangeCountrycodeToCountryname(
                    self, self.lineEdit.text())
                self.sameNodeInMultiArrayFaultLabel.hide()
                self.standbyLabel.show()
                self.cantConnectToNodeFaultLabel.hide()
                for code in osf.Functions.torrcexitnodes:
                    if code == countrycode:
                        self.sameNodeInMultiArrayFaultLabel.show()
                        self.standbyLabel.hide()

        @pyqtSlot()
        def DeleteNodeFromBlacklistAllTableView():
            if osf.Functions.torrcfound is True:
                for currentQTableWidgetItem in \
                        self.blacklistAllNodesTableView.selectedItems():
                    osf.Functions.torrcexcludednodes = \
                        osf.Functions.DeleteCountryFromArray(
                            self, currentQTableWidgetItem.text(),
                            osf.Functions.torrcexcludednodes)

                i = 0
                self.blacklistAllNodesTableView.setRowCount(
                    len(osf.Functions.torrcexcludednodes))
                for nodes in osf.Functions.torrcexcludednodes:
                    self.blacklistAllNodesTableView.setItem(
                        0, i, QtWidgets.QTableWidgetItem(
                            osf.Functions.torrcexcludednodes[i]))
                    i += 1
                self.blacklistAllNodesTableView.resizeRowsToContents()

                osf.Functions.WriteNodesToTorrc(
                    self, "ExcludeNodes", osf.Functions.torrcexcludednodes)

                countrycode = osf.Functions.ChangeCountrycodeToCountryname(
                    self, self.lineEdit.text())
                self.sameNodeInMultiArrayFaultLabel.hide()
                self.standbyLabel.show()
                self.cantConnectToNodeFaultLabel.hide()
                for code in osf.Functions.torrcexitnodes:
                    if code == countrycode:
                        self.sameNodeInMultiArrayFaultLabel.show()
                        self.standbyLabel.hide()

        @pyqtSlot()
        def OpenDialogAbout():
            self.window = QtWidgets.QDialog()
            self.ui = Ui_AboutDialog()
            self.ui.setupUi(self.window)
            self.window.show()

        @pyqtSlot()
        def OpenDialogSettings():
            self.window = QtWidgets.QDialog()
            self.ui = Ui_SettingsDialog()
            self.ui.setupUi(self.window)
            self.window.show()

        @pyqtSlot()
        def OpenDialogUpdate():
            self.window = QtWidgets.QDialog()
            self.ui = Ui_UpdateDialog()
            self.ui.setupUi(self.window)
            self.window.show()

        @pyqtSlot()
        def OpenDialogFault():
            self.window = QtWidgets.QDialog()
            self.ui = Ui_Tor_Metrics_Dialog()
            self.ui.setupUi(self.window)
            self.window.show()

        @pyqtSlot()
        def StartTorBrowser():
            try:
                if osf.Functions.paramplatform == "Windows":
                    torbrowserpath = osf.Functions.parampathtotor + \
                        "\\Start Tor Browser.lnk"
                    os.system('"' + torbrowserpath + '"')

                if osf.Functions.paramplatform == "Linux":

                    torbrowserpath = """sh -c '""" + '"' +\
                        osf.Functions.parampathtotor +\
                        """/Browser/start-tor-browser" --detach || ([ ! -x """\
                        + '"' + osf.Functions.parampathtotor +\
                        """/Browser/start-tor-browser" ] && "$(dirname "$*")"/Browser/"
                        "start-tor-browser --detach)' dummy %k"""

                    os.system(torbrowserpath)

            except Exception as exc:
                osf.Functions.WriteLog(self, exc)

        @pyqtSlot()
        def StartTorMetrics():
            try:
                clip = QApplication.clipboard()
                clip.clear(mode=clip.Clipboard)
                clip.setText("https://metrics."
                             "torproject.org/rs.html"
                             "#search/flag:exit%20"
                             "country:at%20", mode=clip.Clipboard)

            except Exception as exc:
                osf.Functions.WriteLog(self, exc)

        @pyqtSlot()
        def WriteBracetsInLineEdit():
            # Embrace countrycode in bracets (Line-Edit) only if its
            # a valid input
            found = False
            if len(self.lineEdit.text()) == 2:
                if self.lineEdit.text().isalpha():
                    withbracets = "{" + self.lineEdit.text() + "}"
                    for code in osf.Functions.countrycodes:
                        if code == withbracets:
                            self.lineEdit.setText(withbracets)
                            found = True
                        else:
                            if found is False:
                                self.lineEdit.setText("")
                else:
                    self.lineEdit.setText("")
            else:
                if len(self.lineEdit.text()) == 4:
                    for code in osf.Functions.countrycodes:
                        if code == self.lineEdit.text():
                            found = True
                    if found is False:
                        self.lineEdit.setText("")
                else:
                    self.lineEdit.setText("")

        @pyqtSlot()
        def InitializeTableViews():
            # Initialize TableViews on Startup
            osf.Functions.ChangeTorrcStrictNodes(self)
            if osf.Functions.paramstrictnodes == 0:
                self.strictnodesCheckBox.setChecked(False)
                osf.Functions.torrcstrictnodes = False
            else:
                self.strictnodesCheckBox.setChecked(True)
                osf.Functions.torrcstrictnodes = True

            osf.Functions.ChangeTorrcStrictNodes(self)
            AddNodeToChosenNodeTableView()
            AddNodeToBlackListExitTableView()
            AddNodeToBlackListAllTableView()

        # GUI Label shown if Update is available
        if osf.Functions.paramupdateavailable is True:
            self.updatelabel.show()

        def InitializeGUI():
            # Initialize GUI depending on if torrc is found or not
            osf.Functions.GetSettingsFromJson(self)
            osf.Functions.GetTorrcFromFile(self)
            self.cantConnectToNodeFaultLabel.hide()
            self.standbyLabel.show()

            if osf.Functions.paramupdateavailable is False:
                self.updatelabel.hide()

            if osf.Functions.settingschanged is True:
                self.chooseCountryBox.setCurrentIndex(0)
                self.lineEdit.setText("")
                InitializeTableViews()
                osf.Functions.settingschanged = False

            if osf.Functions.torrcfound is True:
                self.cantConnectToNodeFaultLabel.hide()
                self.faultLabel.hide()
                self.startTorBrowserButton.setEnabled(True)
                self.startTorBrowserButton2.setEnabled(True)
                self.startTorBrowserButton3.setEnabled(True)
                self.resettorrcButton.hide()
                self.standbyLabel.show()
                self.sameNodeInMultiArrayFaultLabel.hide()
                self.chooseNodeButton.show()
                self.blacklistAllButton.show()
                self.blacklistExitButton.show()
            else:
                self.faultLabel.show()
                self.standbyLabel.hide()
                self.startTorBrowserButton.setEnabled(False)
                self.startTorBrowserButton2.setEnabled(False)
                self.startTorBrowserButton3.setEnabled(False)
                self.resettorrcButton.show()
                self.chooseNodeButton.hide()
                self.blacklistAllButton.hide()
                self.blacklistExitButton.hide()

                i = 0
                for item in osf.Functions.torrcexitnodes:
                    self.chosenNodesTableView.setItem(
                        i, 0, QtWidgets.QTableWidgetItem("Tor not found."))
                    if i >= 1:
                        self.chosenNodesTableView.setItem(
                            i, 0, QtWidgets.QTableWidgetItem(" "))
                    i += 1

                i = 0
                for item in osf.Functions.torrcexcludednodes:
                    self.blacklistAllNodesTableView.setItem(
                        i, 0, QtWidgets.QTableWidgetItem("Tor not found."))
                    if i >= 1:
                        self.blacklistAllNodesTableView.setItem(
                            i, 0, QtWidgets.QTableWidgetItem(" "))
                    i += 1

                i = 0
                for item in osf.Functions.torrcexcludedexitnodes:
                    self.blacklistExitNodesTableView.setItem(
                        0, 0, QtWidgets.QTableWidgetItem("Tor not found."))
                    if i >= 1:
                        self.blacklistExitNodesTableView.setItem(
                            i, 0, QtWidgets.QTableWidgetItem(" "))
                    i += 1

        InitializeGUI()
        InitializeTableViews()

        self.lineEdit.editingFinished.connect(InitializeGUI)
        self.lineEdit.editingFinished.connect(WriteBracetsInLineEdit)

        self.chooseCountryBox.currentTextChanged.connect(InitializeGUI)
        self.chooseCountryBox.currentTextChanged.connect(ChangeCountry)

        self.chosenNodesTableView.doubleClicked.connect(
            DeleteNodeFromchosenNodeTableView)

        self.blacklistExitNodesTableView.doubleClicked.connect(
            DeleteNodeFromBlacklistExitTableView)

        self.blacklistAllNodesTableView.doubleClicked.connect(
            DeleteNodeFromBlacklistAllTableView)

        self.resettorrcButton.clicked.connect(InitializeGUI)

        self.chooseNodeButton.clicked.connect(InitializeGUI)
        self.chooseNodeButton.clicked.connect(AddNodeToChosenNodeTableView)

        self.blacklistExitButton.clicked.connect(InitializeGUI)
        self.blacklistExitButton.clicked.connect(
            AddNodeToBlackListExitTableView)

        self.blacklistAllButton.clicked.connect(InitializeGUI)
        self.blacklistAllButton.clicked.connect(AddNodeToBlackListAllTableView)

        self.strictnodesCheckBox.clicked.connect(ChangeStrictNodes)

        self.actionAbout.triggered.connect(OpenDialogAbout)
        self.actionSettings.triggered.connect(OpenDialogSettings)
        self.actionUpdate.triggered.connect(OpenDialogUpdate)

        self.actionMetrics.triggered.connect(StartTorMetrics)
        self.actionMetrics.triggered.connect(OpenDialogFault)

        self.actionResetTorrc.triggered.connect(ResetTorrc)

        self.startTorBrowserButton.clicked.connect(StartTorBrowser)
        self.startTorBrowserButton2.clicked.connect(StartTorBrowser)
        self.startTorBrowserButton3.clicked.connect(StartTorBrowser)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OnionSwitch"))
        self.label.setText(_translate(
            "MainWindow", "Choose your Node-Country here:"))
        self.blacklistExitButton.setText(_translate("MainWindow", "Blacklist"))
        self.chooseNodeButton.setText(_translate("MainWindow", "Choose Node"))
        self.startTorBrowserButton2.setText(_translate(
            "MainWindow", "Start Tor-Browser"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab1), _translate("MainWindow", "Choose Node"))
        self.blacklistAllButton.setText(_translate("MainWindow", "Blacklist"))
        self.startTorBrowserButton.setText(_translate(
            "MainWindow", "Start Tor-Browser"))
        self.strictnodesCheckBox.setText(_translate(
            "MainWindow", "StrictNodes 0/1"))
        self.resettorrcButton.setText(_translate("MainWindow", "Reset Torrc"))
        self.startTorBrowserButton3.setText(_translate(
            "MainWindow", "Start Tor-Browser"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab2), _translate("MainWindow", "Blacklist all Nodes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab3), _translate("MainWindow", "Blacklist Exit Nodes"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionResetTorrc.setText(_translate("MainWindow", "Reset Tor"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionMetrics.setText(_translate("MainWindow", "Tor Metrics"))
        self.updatelabel.setText(_translate("MainWindow", "Update\n"
                                            "available"))
        self.faultLabel.setText(_translate(
                                "MainWindow",
                                "Could not find Tor.\n"
                                "Please ensure the correct Path\n"
                                "in the settings."))
        self.sameNodeInMultiArrayFaultLabel.setText(_translate(
                                                    "MainWindow",
                                                    "Chosen Node cant be the\n"
                                                    "same as Excluded Node."))
        self.cantConnectToNodeFaultLabel.setText(_translate(
                                                    "MainWindow",
                                                    "Your chosen\n"
                                                    "Node cant be reached."))
        self.standbyLabel.setText(_translate(
                                        "MainWindow",
                                        "Adding node can take.\n"
                                        "up to 10 seconds.\n"
                                        "Please stand by."))


class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(400, 250)
        AboutDialog.setMinimumSize(QtCore.QSize(400, 250))
        AboutDialog.setMaximumSize(QtCore.QSize(400, 250))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            ":/resources/Ned84_Logo.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutDialog.setWindowIcon(icon)
        self.closeButton = QtWidgets.QPushButton(AboutDialog)
        self.closeButton.setGeometry(QtCore.QRect(290, 210, 93, 28))
        self.closeButton.setObjectName("closeButton")
        self.ned84_logo_frame = QtWidgets.QFrame(AboutDialog)
        self.ned84_logo_frame.setGeometry(QtCore.QRect(10, 50, 141, 131))
        self.ned84_logo_frame.setStyleSheet(
            "image: url(:/resources/Ned84_Logo.png);")
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

        self.closeButton.clicked.connect(AboutDialog.close)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "About"))
        self.closeButton.setText(_translate("AboutDialog", "Close"))
        self.label.setText(_translate("AboutDialog", "OnionSwitch"))
        self.label_2.setText(_translate(
            "AboutDialog", "Version: " + version + "\n"
            "\n"
            "Easily switch the Tor-Exit-Node\n"
            "Destination Country in your\n"
            "Tor-Browser.\n"
            "\n"
            "Copyright (C) 2019  Ned84\n"
            "ned84@protonmail.com"))


class Ui_Tor_Metrics_Dialog(object):
    def setupUi(self, Tor_Metrics_Dialog):
        Tor_Metrics_Dialog.setObjectName("Tor_Metrics_Dialog")
        Tor_Metrics_Dialog.resize(400, 150)
        Tor_Metrics_Dialog.setMinimumSize(QtCore.QSize(400, 150))
        Tor_Metrics_Dialog.setMaximumSize(QtCore.QSize(400, 150))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            ":/resources/OnionSwitch_Logo.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Tor_Metrics_Dialog.setWindowIcon(icon)
        self.okButton = QtWidgets.QPushButton(Tor_Metrics_Dialog)
        self.okButton.setGeometry(QtCore.QRect(290, 110, 93, 28))
        self.okButton.setObjectName("okButton")
        self.label = QtWidgets.QLabel(Tor_Metrics_Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Tor_Metrics_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Tor_Metrics_Dialog)

        self.okButton.clicked.connect(Tor_Metrics_Dialog.close)

    def retranslateUi(self, Tor_Metrics_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Tor_Metrics_Dialog.setWindowTitle(_translate(
            "Tor_Metrics_Dialog", "Information"))
        self.okButton.setText(_translate("Tor_Metrics_Dialog", "OK"))
        self.label.setText(_translate(
            "Tor_Metrics_Dialog", "URL to Tor Metrics is "
            "copied to the Clipboard.\n"
            "Please open it in the Browser of your choice."))


class Ui_SettingsDialog(QtWidgets.QWidget):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(400, 250)
        SettingsDialog.setMinimumSize(QtCore.QSize(400, 250))
        SettingsDialog.setMaximumSize(QtCore.QSize(400, 250))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            ":/resources/OnionSwitch_Logo.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.stemcheckCheckBox = QtWidgets.QCheckBox(SettingsDialog)
        self.stemcheckCheckBox.setGeometry(QtCore.QRect(20, 80, 150, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.stemcheckCheckBox.setFont(font)
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
        self.onionswitch_logo_frame.setGeometry(
            QtCore.QRect(10, 110, 141, 131))
        self.onionswitch_logo_frame.setStyleSheet(
            "image: url(:/resources/OnionSwitch_Logo.png);")
        self.onionswitch_logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.onionswitch_logo_frame.setObjectName("onionswitch_logo_frame")

        self.retranslateUi(SettingsDialog)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

        if osf.Functions.paramstemcheck is True:
            self.stemcheckCheckBox.setChecked(True)
        else:
            self.stemcheckCheckBox.setChecked(False)

        self.lineEdit.setText(osf.Functions.parampathtotor)

        def OpenFilePicker():
            try:
                folderName = QFileDialog.getExistingDirectory(
                    self, "Select Tor Directory")
                if folderName:
                    self.lineEdit.setText(folderName)

            except Exception as exc:
                osf.Functions.WriteLog(self, exc)

        @pyqtSlot()
        def okButtonPress():
            try:
                if self.stemcheckCheckBox.isChecked() is True:
                    osf.Functions.paramstemcheck = True
                else:
                    osf.Functions.paramstemcheck = False

                osf.Functions.parampathtotor = self.lineEdit.text()

                osf.Functions.WriteSettingsToJson(self)

                if osf.Functions.paramplatform == "Windows":
                    osf.Functions.torrcfilepath =\
                        osf.Functions.parampathtotor +\
                        "\\Browser\\TorBrowser\\Data\\Tor\\torrc"

                    if osf.Functions.parampathtotor != "":
                        if path. exists(osf.Functions.torrcfilepath) is True:
                            if path.exists(
                                 osf.Functions.pathtoparam + '\\rccy')\
                                     is False:
                                copyfile(
                                    osf.Functions.torrcfilepath,
                                    osf.Functions.pathtoparam + '\\rccy')

                if osf.Functions.paramplatform == "Linux":
                    osf.Functions.torrcfilepath = \
                        osf.Functions.parampathtotor + \
                        "/Browser/TorBrowser/Data/Tor/torrc"

                    if osf.Functions.parampathtotor != "":
                        if path. exists(osf.Functions.torrcfilepath) is True:
                            if path.exists(
                                 osf.Functions.pathtoparam + '/rccy') is False:
                                copyfile(osf.Functions.torrcfilepath,
                                         osf.Functions.pathtoparam + '/rccy')

            except Exception as exc:
                osf.Functions.WriteLog(self, exc)

            osf.Functions.settingschanged = True
            if path.exists(osf.Functions.torrcfilepath) is False:
                osf.Functions.torrcfound = False
            else:
                osf.Functions.torrcfound = True
            SettingsDialog.close

        self.cancelButton.clicked.connect(SettingsDialog.close)

        self.openButton.clicked.connect(OpenFilePicker)

        self.okButton.clicked.connect(okButtonPress)
        self.okButton.clicked.connect(SettingsDialog.close)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Settings"))
        self.okButton.setText(_translate("SettingsDialog", "OK"))
        self.cancelButton.setText(_translate("SettingsDialog", "Cancel"))
        self.label.setText(_translate(
            "SettingsDialog", "Path to Tor-Browser:"))
        self.stemcheckCheckBox.setText(_translate(
            "SettingsDialog", "Stem Node Check"))
        self.openButton.setText(_translate("SettingsDialog", "Open"))


class Ui_UpdateDialog(object):
    def setupUi(self, UpdateDialog):
        UpdateDialog.setObjectName("UpdateDialog")
        UpdateDialog.resize(400, 250)
        UpdateDialog.setMinimumSize(QtCore.QSize(400, 250))
        UpdateDialog.setMaximumSize(QtCore.QSize(400, 250))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/resources/OnionSwitch_Logo.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UpdateDialog.setWindowIcon(icon)
        self.cancelButton = QtWidgets.QPushButton(UpdateDialog)
        self.cancelButton.setGeometry(QtCore.QRect(290, 210, 93, 28))
        self.cancelButton.setObjectName("Cancel")
        self.updateButton = QtWidgets.QPushButton(UpdateDialog)
        self.updateButton.setGeometry(QtCore.QRect(180, 210, 93, 28))
        self.updateButton.setObjectName("updateButton")
        self.onionswitch_logo_frame = QtWidgets.QFrame(UpdateDialog)
        self.onionswitch_logo_frame.setGeometry(QtCore.QRect(10, 50, 141, 131))
        self.onionswitch_logo_frame.setStyleSheet(
            "image: url(:/resources/OnionSwitch_Logo.png);")
        self.onionswitch_logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.onionswitch_logo_frame.setObjectName("onionswitch_logo_frame")
        self.label = QtWidgets.QLabel(UpdateDialog)
        self.label.setGeometry(QtCore.QRect(190, 20, 181, 31))
        self.label2 = QtWidgets.QLabel(UpdateDialog)
        self.label2.setGeometry(QtCore.QRect(170, 60, 301, 131))
        self.label3 = QtWidgets.QLabel(UpdateDialog)
        self.label3.setGeometry(QtCore.QRect(170, 60, 301, 131))
        self.label4 = QtWidgets.QLabel(UpdateDialog)
        self.label4.setGeometry(QtCore.QRect(170, 60, 301, 131))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(UpdateDialog)
        QtCore.QMetaObject.connectSlotsByName(UpdateDialog)

        @pyqtSlot()
        def StartUpdateProc():
            osf.Functions.paramupdateavailable = False
            osf.Functions.WriteSettingsToJson(self)
            webbrowser.open('https://github.com/Ned84/OnionSwitch/releases')

        self.cancelButton.clicked.connect(UpdateDialog.close)

        self.updateButton.clicked.connect(StartUpdateProc)

    def retranslateUi(self, UpdateDialog):
        _translate = QtCore.QCoreApplication.translate
        UpdateDialog.setWindowTitle(_translate("UpdateDialog", "Update"))
        self.cancelButton.setText(_translate("UpdateDialog", "Cancel"))
        self.updateButton.setText(_translate("UpdateDialog", "Update"))
        self.label.setText(_translate("UpdateDialog", "OnionSwitch"))
        self.label2.setText(_translate(
            "UpdateDialog", "Current Version: " + version + "\n"
            "\n"
            "New Version: " + Ui_MainWindow.versionnew + "\n"
            "\n"
            "Do you want to Update\n"
            "this Program?"))

        self.label3.setText(_translate(
            "UpdateDialog", "No connection to Github."))
        self.label3.setFont(QtGui.QFont("Arial", 9))

        self.label4.setText(_translate(
            "UpdateDialog", "Current Version: " + version + "\n"
            "\n"
            "New Version: " + Ui_MainWindow.versionnew + "\n"
            "\n"
            "No Update available."))

        self.label4.setFont(QtGui.QFont("Arial", 9))

        self.label2.setFont(QtGui.QFont("Arial", 9))

        if Ui_MainWindow.serverconnection is False:
            self.updateButton.setEnabled(False)
            self.label2.hide()
            self.label4.hide()
            self.label3.show()
        else:
            if osf.Functions.paramupdateavailable is True:
                self.updateButton.setEnabled(True)
                self.label2.show()
                self.label4.hide()
                self.label3.hide()
            else:
                self.updateButton.setEnabled(False)
                self.label2.hide()
                self.label4.show()
                self.label3.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
