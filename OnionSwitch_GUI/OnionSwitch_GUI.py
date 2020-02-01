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

version = "1.2"


class Fonts():

    def Choose_Fonts(self, bold, size, font_type):
        font = QtGui.QFont()
        font.setFamily(font_type)
        if osf.Functions.paramplatform == "Windows":
            if bold is True:
                font.setBold(True)
                font.setWeight(75)
            else:
                pass

            font.setPointSize(size)
        else:
            if bold is True:
                font.setBold(True)
                font.setWeight(75)
            else:
                pass

            font.setPointSize(size + 2)

        return font


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
                             "Platform": "", "StemCheck": False,
                             "StemCheck_Time": 10}]

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
        MainWindow.setStyleSheet(
            "QMainWindow#OnionSwitch {background-color: qlineargradient("
            "spread:pad, x1:1, y1:0, x2:, y2:1, stop:0 rgb(200,200,200),"
            " stop:1 rgb(253,253,253));}")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/OnionSwitch_w_w_bgr.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chooseCountryBox = QtWidgets.QComboBox(self.centralwidget)
        self.chooseCountryBox.setGeometry(QtCore.QRect(113, 50, 300, 22))
        self.chooseCountryBox.addItems(osf.Functions.countrynames)
        font = Fonts.Choose_Fonts(self, False, 10, "Arial")
        self.chooseCountryBox.setFont(font)
        self.chooseCountryBox.setObjectName("chooseCountryBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 311, 21))
        self.updatelabel = QtWidgets.QLabel(self.centralwidget)
        self.updatelabel.setGeometry(QtCore.QRect(20, 60, 100, 35))
        font = Fonts.Choose_Fonts(self, True, 10, "Arial")
        self.updatelabel.setStyleSheet("color: rgb(89, 49, 107)")
        self.updatelabel.setFont(font)
        self.updatelabel.hide()
        font = Fonts.Choose_Fonts(self, True, 10, "Arial")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(113, 80, 80, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 110, 525, 171))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName("tabWidget")
    #     stylesheet = """
    # QTabBar::tab:selected {color: white;}
    # QTabBar::tab { height: 30px; width: 175px;
    # background-color: rgb(89, 49, 107); font: 10pt Arial;
    # selection-background-color: rgb(255, 255, 255);}
    # """
        if osf.Functions.paramplatform == "Windows":
            font = "10pt Arial"
        else:
            font = "12pt Arial"

        stylesheet = """
        QTabBar::tab:selected {color: white;}
        QTabBar::tab { height: 30px; width: 175px;
        background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:, y2:1,
        stop:0 rgb(139,99,157), stop:1 rgb(39,0,57));
        font: """ + font + """;
        color : qlineargradient(spread:pad, x1:1, y1:0, x2:, y2:1,
        stop:0 rgb(100,100,100), stop:1 rgb(200,200,200));
        selection-background-color: rgb(255, 255, 255);}
        """

        # (89,49,107)
        self.tabWidget.setStyleSheet(stylesheet)
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.tab1.setStyleSheet("QWidget#tab1 {background-color: "
                                "qlineargradient(spread:pad, x1:1, y1:0, x2:,"
                                "y2:1, stop:0 rgb("
                                "200,200,200), stop:1 rgb(253,253,253));}")
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
        if osf.Functions.paramplatform == "Windows":
            width = 121
        else:
            width = 130
        self.startTorBrowserButton2.setGeometry(QtCore.QRect(
            10, 100, width, 28))
        self.startTorBrowserButton2.setObjectName("startTorBrowserButton2")
        self.tabWidget.addTab(self.tab1, "")
        self.chosenNodesTableView = QtWidgets.QTableWidget(self.tab1)
        self.chosenNodesTableView.setGeometry(QtCore.QRect(384, -1, 141, 134))
        self.chosenNodesTableView.setObjectName("chosenNodesTableView")
        self.chosenNodesTableView.setStyleSheet(
            "QTableWidget#chosenNodesTableView {background-color: "
            "qlineargradient(spread:pad, x1:1, y1:0, x2:, y2:1, stop:0 rgb("
            "200,200,200), stop:1 rgb(253,253,253));}")
        self.chosenNodesTableView.setRowCount(4)
        self.chosenNodesTableView.setColumnCount(1)
        self.chosenNodesTableView.horizontalHeader().hide()
        self.chosenNodesTableView.verticalHeader().hide()
        self.chosenNodesTableView.setShowGrid(False)
        self.chosenNodesTableView.setEditTriggers(
            self.chosenNodesTableView.NoEditTriggers)
        self.chosenNodesTableView.setItem(
            0, 0, QtWidgets.QTableWidgetItem("Tor not found."))
        font = Fonts.Choose_Fonts(self, False, 9, "Segoe UI")
        self.chosenNodesTableView.setFont(font)
        self.chosenNodesTableView.setColumnWidth(1, 141)
        self.chosenNodesTableView.resizeRowsToContents()
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.tab2.setStyleSheet(
            "QWidget#tab2 {background-color: qlineargradient("
            "spread:pad, x1:1, y1:0, x2:, y2:1, stop:0 rgb("
            "200,200,200), stop:1 rgb(253,253,253));}")

        self.blacklistAllButton = QtWidgets.QPushButton(self.tab2)
        self.blacklistAllButton.setGeometry(QtCore.QRect(264, 100, 111, 28))
        self.blacklistAllButton.setObjectName("blacklistAllButton")
        self.blacklistAllNodesTableView = QtWidgets.QTableWidget(self.tab2)
        self.blacklistAllNodesTableView.setGeometry(QtCore.QRect(
            384, -1, 141, 134))
        self.blacklistAllNodesTableView.setObjectName(
            "blacklistAllNodesTableView")
        self.blacklistAllNodesTableView.setStyleSheet(
            "QTableWidget#blacklistAllNodesTableView {background-color: "
            "qlineargradient(spread:pad, x1:1, y1:0, x2:, y2:1, stop:0 rgb("
            "200,200,200), stop:1 rgb(253,253,253));}")
        self.blacklistAllNodesTableView.setRowCount(4)
        self.blacklistAllNodesTableView.setColumnCount(1)
        self.blacklistAllNodesTableView.horizontalHeader().hide()
        self.blacklistAllNodesTableView.verticalHeader().hide()
        self.blacklistAllNodesTableView.setShowGrid(False)
        self.blacklistAllNodesTableView.setEditTriggers(
            self.chosenNodesTableView.NoEditTriggers)
        font = Fonts.Choose_Fonts(self, False, 9, "Segoe UI")
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
        if osf.Functions.paramplatform == "Windows":
            width = 121
        else:
            width = 130
        self.startTorBrowserButton.setGeometry(
            QtCore.QRect(10, 100, width, 28))
        self.startTorBrowserButton.setObjectName("startTorBrowserButton")
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.tab3.setStyleSheet(
            "QWidget#tab3 {background-color: qlineargradient("
            "spread:pad, x1:1, y1:0, x2:, y2:1, stop:0 rgb("
            "200,200,200), stop:1 rgb(253,253,253));}")
        self.blacklistExitNodesTableView = QtWidgets.QTableWidget(self.tab3)
        self.blacklistExitNodesTableView.setGeometry(QtCore.QRect(
            384, -1, 141, 134))
        self.blacklistExitNodesTableView.setObjectName(
            "blacklistExitNodesTableView")
        self.blacklistExitNodesTableView.setStyleSheet(
            "QTableWidget#blacklistExitNodesTableView {background-color: "
            "qlineargradient(spread:pad, x1:1, y1:0, x2:, y2:1, stop:0 rgb("
            "200,200,200), stop:1 rgb(253,253,253));}")
        self.blacklistExitNodesTableView.setRowCount(4)
        self.blacklistExitNodesTableView.setColumnCount(1)
        self.blacklistExitNodesTableView.horizontalHeader().hide()
        self.blacklistExitNodesTableView.verticalHeader().hide()
        self.blacklistExitNodesTableView.setShowGrid(False)
        self.blacklistExitNodesTableView.setEditTriggers(
            self.chosenNodesTableView.NoEditTriggers)
        font = Fonts.Choose_Fonts(self, False, 9, "Segoe UI")
        self.blacklistExitNodesTableView.setFont(font)
        self.blacklistExitNodesTableView.setColumnWidth(1, 141)
        self.blacklistExitNodesTableView.resizeRowsToContents()
        self.blacklistExitNodesTableView.setItem(
            0, 0, QtWidgets.QTableWidgetItem("Tor not found."))
        self.blacklistExitButton = QtWidgets.QPushButton(self.tab3)
        self.blacklistExitButton.setGeometry(QtCore.QRect(264, 100, 111, 28))
        self.blacklistExitButton.setObjectName("blacklistExitButton")
        self.startTorBrowserButton3 = QtWidgets.QPushButton(self.tab3)
        if osf.Functions.paramplatform == "Windows":
            width = 121
        else:
            width = 130
        self.startTorBrowserButton3.setGeometry(QtCore.QRect(
            10, 100, width, 28))
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
        font = Fonts.Choose_Fonts(self, True, 10, "Arial")
        self.faultLabel.setFont(font)
        self.faultLabel.setObjectName("faultLabel")
        self.sameNodeInMultiArrayFaultLabel = QtWidgets.QLabel(
            self.centralwidget)
        self.sameNodeInMultiArrayFaultLabel.setGeometry(
            QtCore.QRect(140, 150, 200, 71))
        font = Fonts.Choose_Fonts(self, True, 10, "Arial")
        self.sameNodeInMultiArrayFaultLabel.setFont(font)
        self.sameNodeInMultiArrayFaultLabel.setObjectName(
            "sameNodeInMultiArrayFaultLabel")
        self.sameNodeInMultiArrayFaultLabel.hide()
        self.cantConnectToNodeFaultLabel = QtWidgets.QLabel(
            self.centralwidget)
        self.cantConnectToNodeFaultLabel.setGeometry(
            QtCore.QRect(140, 150, 200, 71))
        font = Fonts.Choose_Fonts(self, True, 10, "Arial")
        self.cantConnectToNodeFaultLabel.setFont(font)
        self.cantConnectToNodeFaultLabel.setObjectName(
            "cantConnectToNodeFaultLabel")
        self.cantConnectToNodeFaultLabel.hide()
        self.standbyLabel = QtWidgets.QLabel(
            self.tab1)
        self.standbyLabel.setGeometry(
            QtCore.QRect(175, 10, 200, 71))
        font = Fonts.Choose_Fonts(self, True, 10, "Arial")
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

        def ResetTorrc_thread():
            try:
                while True:
                    if osf.Functions.torrc_reset_dialog_closed is True:
                        break
                if osf.Functions.reset_torrc_ok is True:
                    if osf.Functions.torrcfound is True:

                        self.lineEdit.setText("")

                        if osf.Functions.paramplatform == "Windows":
                            if path.exists(
                                osf.Functions.pathtoparam + '\\rccy')\
                                 is True:
                                os.remove(osf.Functions.torrcfilepath)

                                copyfile(osf.Functions.pathtoparam + '\\rccy',
                                         osf.Functions.torrcfilepath)

                        if osf.Functions.paramplatform == "Linux":
                            if path.exists(
                                osf.Functions.pathtoparam + '/rccy')\
                                 is True:
                                os.remove(osf.Functions.torrcfilepath)

                                copyfile(osf.Functions.pathtoparam + '/rccy',
                                         osf.Functions.torrcfilepath)

                        osf.Functions.reset_torrc_ok = False

                        osf.Functions.GetTorrcFromFile(self)
                        AddNodeToChosenNodeTableView()
                        AddNodeToBlackListAllTableView()
                        AddNodeToBlackListExitTableView()
                        InitializeTableViews()
                        self.cantConnectToNodeFaultLabel.hide()

                    osf.Functions.window_torrc_reset_open = False

            except Exception as exc:
                osf.Functions.WriteLog(self, exc)

        @pyqtSlot()
        def ResetTorrc():
            try:
                if osf.Functions.window_torrc_reset_open is False:
                    self.window = QtWidgets.QDialog()
                    self.window.setWindowFlags(
                        self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
                    self.window.setWindowFlags(
                        self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
                    self.ui = Ui_Tor_Reset_Dialog()
                    self.ui.setupUi(self.window)
                    self.window.show()
                    osf.Functions.window_torrc_reset_open = True
                    osf.Functions.torrc_reset_dialog_closed = False

                    checkthread = threading.Thread(
                        target=ResetTorrc_thread, daemon=True)
                    checkthread.start()

            except Exception as exc:
                osf.Functions.WriteLog(self, exc)

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
                                osf.Functions.parampathtotor,
                                osf.Functions.paramstemchecktime)

                            if ostc.TorCheck.connected is False:
                                connection_count = 0
                            else:
                                connection_count += 1

                            if osf.Functions.resettorrc_changed is True:
                                connection_count += 1
                                osf.Functions.resettorrc_changed = False
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
            if osf.Functions.window_about_open is False:
                self.window = QtWidgets.QDialog()
                self.window.setWindowFlags(
                    self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
                self.window.setWindowFlags(
                    self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
                self.ui = Ui_AboutDialog()
                self.ui.setupUi(self.window)
                self.window.show()
                osf.Functions.window_about_open = True

        def CheckSettings():
            # Check if Settings change to write eye countries into tableview.

            InitializeTableViews()
            self.blacklistAllNodesTableView.resizeRowsToContents()
            InitializeGUI()

        @pyqtSlot()
        def OpenDialogSettings():
            if osf.Functions.window_settings_open is False:
                self.lineEdit.setText("")
                self.window_settings = QtWidgets.QDialog()
                self.window_settings.setWindowFlags(
                    self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
                self.window_settings.setWindowFlags(
                    self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
                self.window_settings.installEventFilter(self)
                # self.ui = Ui_SettingsDialog()
                self.ui = Ui_SettingsNewDialog()
                self.ui.setupUi(self.window_settings)
                self.window_settings.finished.connect(CheckSettings)
                self.window_settings.show()
                osf.Functions.window_settings_open = True

        @pyqtSlot()
        def OpenDialogUpdate():
            if osf.Functions.window_update_open is False:
                self.window = QtWidgets.QDialog()
                self.window.setWindowFlags(
                    self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
                self.window.setWindowFlags(
                    self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
                self.ui = Ui_UpdateDialog()
                self.ui.setupUi(self.window)
                self.window.show()
                osf.Functions.window_update_open = True

        @pyqtSlot()
        def OpenDialogFault():
            self.window = QtWidgets.QDialog()
            self.window.setWindowFlags(
                self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
            self.window.setWindowFlags(
                self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
            self.ui = Ui_Tor_Metrics_Dialog()
            self.ui.setupUi(self.window)
            self.window.show()

        @pyqtSlot()
        def StartTorBrowser():
            osf.Functions.StartTorBrowser(self)

        @pyqtSlot()
        def StartTorMetrics():
            osf.Functions.TorMetrics_to_Clipboard(
                self, QApplication, self.lineEdit.text())

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

            osf.Functions.GetTorrcFromFile(self)
            osf.Functions.ChangeTorrcStrictNodes(self)
            if osf.Functions.paramstrictnodes == 0:
                osf.Functions.torrcstrictnodes = False
            else:
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

            if osf.Functions.paramstemcheck is False:
                self.standbyLabel.setText("")
            else:
                self.standbyLabel.setText(
                    "Adding node can take.\n"
                    "up to "
                    "{0}".format(
                        osf.Functions.paramstemchecktime) +
                    " seconds.\n"
                    "Please stand by.")

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
                                        "up to "
                                        "{0}".format(
                                            osf.Functions.paramstemchecktime) +
                                        "seconds.\n"
                                        "Please stand by."))


class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(400, 250)
        AboutDialog.setMinimumSize(QtCore.QSize(400, 250))
        AboutDialog.setMaximumSize(QtCore.QSize(400, 250))
        AboutDialog.setStyleSheet(
            "QDialog#AboutDialog {background-color: qlineargradient("
            "spread:pad, x1:1, y1:0, x2:, y2:1, stop:0 rgb("
            "200,200,200), stop:1 rgb(253,253,253));}")
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
        font = Fonts.Choose_Fonts(self, True, 10, "Arial")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AboutDialog)
        self.label_2.setGeometry(QtCore.QRect(190, 70, 190, 130))
        font = Fonts.Choose_Fonts(self, False, 8, "MS Shell Dlg 2")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

        @pyqtSlot()
        def Close_About():
            osf.Functions.window_about_open = False
            AboutDialog.close()

        self.closeButton.clicked.connect(Close_About)

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
        Tor_Metrics_Dialog.setStyleSheet(
            "QDialog#Tor_Metrics_Dialog {background-color: qlineargradient("
            "spread:pad, x1:1, y1:0, x2:, y2:1, stop:0 rgb("
            "200,200,200), stop:1 rgb(253,253,253));}")
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
        font = Fonts.Choose_Fonts(self, False, 10, "Arial")
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
        SettingsDialog.resize(400, 300)
        SettingsDialog.setMinimumSize(QtCore.QSize(400, 300))
        SettingsDialog.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            ":/resources/OnionSwitch_Logo.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SettingsDialog.setWindowIcon(icon)
        self.okButton = QtWidgets.QPushButton(SettingsDialog)
        self.okButton.setGeometry(QtCore.QRect(180, 260, 93, 28))
        self.okButton.setObjectName("okButton")
        self.cancelButton = QtWidgets.QPushButton(SettingsDialog)
        self.cancelButton.setGeometry(QtCore.QRect(290, 260, 93, 28))
        self.cancelButton.setObjectName("cancelButton")
        self.lineEdit = QtWidgets.QLineEdit(SettingsDialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 361, 22))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.stemcheckCheckBox = QtWidgets.QCheckBox(SettingsDialog)
        self.stemcheckCheckBox.setGeometry(QtCore.QRect(20, 80, 150, 21))

        font = Fonts.Choose_Fonts(self, True, 8, "Arial")
        self.stemcheckCheckBox.setFont(font)
        self.stemchecktime_lineedit = QtWidgets.QLineEdit(SettingsDialog)
        self.stemchecktime_lineedit.setGeometry(QtCore.QRect(15, 105, 25, 22))
        self.stemchecktime_lineedit.setObjectName("stemchecktime_lineedit")
        self.stemchecktime_lineedit.setAlignment(QtCore.Qt.AlignCenter)
        self.stemchecktime_lineedit.setFont(font)
        self.stemchecktime_lineedit.setMaxLength(2)
        self.stemchecktime_label = QtWidgets.QLabel(SettingsDialog)
        self.stemchecktime_label.setGeometry(QtCore.QRect(43, 105, 150, 22))
        self.stemchecktime_label.setObjectName("stemchecktime_label")
        self.stemchecktime_label.setFont(font)
        self.fiveEyesCheckBox = QtWidgets.QCheckBox(SettingsDialog)
        self.fiveEyesCheckBox.setGeometry(QtCore.QRect(180, 145, 190, 21))
        self.fiveEyesCheckBox.setFont(font)
        self.nineEyesCheckBox = QtWidgets.QCheckBox(SettingsDialog)
        self.nineEyesCheckBox.setGeometry(QtCore.QRect(180, 175, 190, 21))
        self.nineEyesCheckBox.setFont(font)
        self.fourteenEyesCheckBox = QtWidgets.QCheckBox(SettingsDialog)
        self.fourteenEyesCheckBox.setGeometry(QtCore.QRect(180, 205, 190, 21))
        self.fourteenEyesCheckBox.setFont(font)
        self.label = QtWidgets.QLabel(SettingsDialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 171, 21))
        font = Fonts.Choose_Fonts(self, True, 10, "Arial")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.openButton = QtWidgets.QPushButton(SettingsDialog)
        self.openButton.setGeometry(QtCore.QRect(290, 80, 93, 28))
        self.openButton.setObjectName("openButton")
        self.onionswitch_logo_frame = QtWidgets.QFrame(SettingsDialog)
        self.onionswitch_logo_frame.setGeometry(
            QtCore.QRect(10, 160, 141, 131))
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

        if self.stemcheckCheckBox.isChecked():
            self.stemchecktime_lineedit.setEnabled(True)
            self.stemchecktime_label.setEnabled(True)
        else:
            self.stemchecktime_lineedit.setEnabled(False)
            self.stemchecktime_label.setEnabled(False)

        self.lineEdit.setText(osf.Functions.parampathtotor)

        self.stemchecktime_lineedit.setText(
            "{0}".format(osf.Functions.paramstemchecktime))

        def OpenFilePicker():
            try:
                folderName = QFileDialog.getExistingDirectory(
                    self, "Select Tor Directory")
                if folderName:
                    self.lineEdit.setText(folderName)

            except Exception as exc:
                osf.Functions.WriteLog(self, exc)

        @pyqtSlot()
        def Change_StemCheckTime():

            if self.stemchecktime_lineedit.text().isdigit():
                if (int)(self.stemchecktime_lineedit.text()) > 60:
                    self.stemchecktime_lineedit.setText("60")

                if (int)(self.stemchecktime_lineedit.text()) <= 5:
                    self.stemchecktime_lineedit.setText("5")
            else:
                self.stemchecktime_lineedit.setText(
                    "{0}".format(osf.Functions.paramstemchecktime))

        @pyqtSlot()
        def fiveeyes_changed():
            self.nineEyesCheckBox.setChecked(False)
            self.fourteenEyesCheckBox.setChecked(False)
            osf.Functions.eyes_changed = True

        @pyqtSlot()
        def nineeyes_changed():
            self.fiveEyesCheckBox.setChecked(False)
            self.fourteenEyesCheckBox.setChecked(False)
            osf.Functions.eyes_changed = True

        @pyqtSlot()
        def fourteeneyes_changed():
            self.fiveEyesCheckBox.setChecked(False)
            self.nineEyesCheckBox.setChecked(False)
            osf.Functions.eyes_changed = True

        @pyqtSlot()
        def okButtonPress():
            try:
                if self.stemcheckCheckBox.isChecked() is True:
                    osf.Functions.paramstemcheck = True
                else:
                    osf.Functions.paramstemcheck = False

                osf.Functions.parampathtotor = self.lineEdit.text()

                osf.Functions.paramstemchecktime = (int)(
                    self.stemchecktime_lineedit.text())

                if self.fiveEyesCheckBox.isChecked() is True:
                    osf.Functions.Add_Eyes_ToArray(
                        self, osf.Functions.five_eye_countries)

                if self.nineEyesCheckBox.isChecked() is True:
                    osf.Functions.Add_Eyes_ToArray(
                        self, osf.Functions.five_eye_countries)

                    osf.Functions.Add_Eyes_ToArray(
                        self, osf.Functions.nine_eye_countries)

                    osf.Functions.Add_Eyes_ToArray(
                        self, osf.Functions.nine_eye_countries)

                if self.fourteenEyesCheckBox.isChecked() is True:
                    osf.Functions.Add_Eyes_ToArray(
                        self, osf.Functions.five_eye_countries)

                    osf.Functions.Add_Eyes_ToArray(
                        self, osf.Functions.nine_eye_countries)

                    osf.Functions.Add_Eyes_ToArray(
                        self, osf.Functions.fourteen_eye_countries)

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

                osf.Functions.window_settings_open = False

            except Exception as exc:
                osf.Functions.WriteLog(self, exc)

            osf.Functions.settingschanged = True
            if path.exists(osf.Functions.torrcfilepath) is False:
                osf.Functions.torrcfound = False
            else:
                osf.Functions.torrcfound = True

            osf.Functions.settings_closed = True
            SettingsDialog.close

        @pyqtSlot()
        def StemCheckTime_Label_Visibility():
            if self.stemcheckCheckBox.isChecked():
                self.stemchecktime_lineedit.setEnabled(True)
                self.stemchecktime_label.setEnabled(True)
            else:
                self.stemchecktime_lineedit.setEnabled(False)
                self.stemchecktime_label.setEnabled(False)

        @pyqtSlot()
        def Close_Settings():
            osf.Functions.window_settings_open = False
            osf.Functions.settings_closed = True
            SettingsDialog.close()

        self.cancelButton.clicked.connect(Close_Settings)

        self.openButton.clicked.connect(OpenFilePicker)

        self.fiveEyesCheckBox.clicked.connect(fiveeyes_changed)

        self.nineEyesCheckBox.clicked.connect(nineeyes_changed)

        self.fourteenEyesCheckBox.clicked.connect(fourteeneyes_changed)

        self.okButton.clicked.connect(okButtonPress)
        self.okButton.clicked.connect(SettingsDialog.close)

        self.stemchecktime_lineedit.editingFinished.connect(
            Change_StemCheckTime)

        self.stemcheckCheckBox.clicked.connect(StemCheckTime_Label_Visibility)

        if osf.Functions.torrcfound is True:
            self.fiveEyesCheckBox.show()
            self.nineEyesCheckBox.show()
            self.fourteenEyesCheckBox.show()
            self.stemcheckCheckBox.show()
            self.stemchecktime_lineedit.show()
            self.stemchecktime_label.show()
        else:
            self.fiveEyesCheckBox.hide()
            self.nineEyesCheckBox.hide()
            self.fourteenEyesCheckBox.hide()
            self.stemcheckCheckBox.hide()
            self.stemchecktime_lineedit.hide()
            self.stemchecktime_label.hide()

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
        self.fiveEyesCheckBox.setText(_translate(
            "SettingsDialog", "Block '5-Eyes' Countries"))
        self.nineEyesCheckBox.setText(_translate(
            "SettingsDialog", "Block '9-Eyes' Countries"))
        self.fourteenEyesCheckBox.setText(_translate(
            "SettingsDialog", "Block '14-Eyes' Countries"))
        self.stemchecktime_label.setText(_translate(
            "SettingsDialog", "Stem Check max. Time"))


class Ui_SettingsNewDialog(QtWidgets.QWidget):
    def setupUi(self, SettingsNewDialog):
        SettingsNewDialog.setObjectName("SettingsNewDialog")
        SettingsNewDialog.resize(400, 300)
        SettingsNewDialog.setMinimumSize(QtCore.QSize(400, 300))
        SettingsNewDialog.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            ":/resources/OnionSwitch_Logo.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SettingsNewDialog.setWindowIcon(icon)
        font = Fonts.Choose_Fonts(self, False, 10, "Arial")
        self.cancel_Button = QtWidgets.QPushButton(SettingsNewDialog)
        self.cancel_Button.setGeometry(QtCore.QRect(300, 260, 90, 28))
        self.cancel_Button.setObjectName("cancel_Button")
        self.ok_Button = QtWidgets.QPushButton(SettingsNewDialog)
        self.ok_Button.setGeometry(QtCore.QRect(200, 260, 90, 28))
        self.ok_Button.setObjectName("ok_Button")
        self.main_listWidget = QtWidgets.QListWidget(SettingsNewDialog)
        self.main_listWidget.setGeometry(QtCore.QRect(0, 0, 150, 300))
        self.main_listWidget.setObjectName("main_listview")
        self.main_listWidget.setFont(font)
        self.main_listWidget.addItem("General")
        self.main_listWidget.addItem("Nodes")
        self.main_listWidget.addItem("Eyes - Countries")
        self.main_listWidget.setStyleSheet(
            "background-color: qlineargradient("
            "spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgb("
            "0, 0, 0), stop:1 rgb(60, 60, 60));")
        self.main_listWidget.item(0).setForeground(QtCore.Qt.white)
        self.main_listWidget.item(1).setForeground(QtCore.Qt.white)
        self.main_listWidget.item(2).setForeground(QtCore.Qt.white)
        self.general_groupbox = QtWidgets.QGroupBox(SettingsNewDialog)
        self.general_groupbox.setGeometry(QtCore.QRect(150, 0, 250, 300))
        self.general_groupbox.setObjectName("general_groupbox")
        self.general_groupbox.setStyleSheet(
            "QGroupBox#general_groupbox {background-color: qlineargradient("
            "spread:pad, x1:1, y1:0, x2:, y2:1, stop:0 rgb("
            "60, 60, 60), stop:1 rgb(60,60,60))};")
        self.setObjectName("general_groupbox")
        self.lineEdit = QtWidgets.QLineEdit(self.general_groupbox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 230, 22))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.openButton = QtWidgets.QPushButton(self.general_groupbox)
        self.openButton.setGeometry(QtCore.QRect(147, 70, 93, 28))
        self.openButton.setObjectName("openButton")
        self.pathtotorLabel = QtWidgets.QLabel(self.general_groupbox)
        self.pathtotorLabel.setGeometry(QtCore.QRect(10, 10, 171, 21))
        self.pathtotorLabel.setFont(font)
        self.pathtotorLabel.setObjectName("pathtotorLabel")
        self.pathtotorLabel.setStyleSheet("color:white")
        self.nodes_groupbox = QtWidgets.QGroupBox(SettingsNewDialog)
        self.nodes_groupbox.setGeometry(QtCore.QRect(150, 0, 250, 300))
        self.nodes_groupbox.setObjectName("nodes_groupbox")
        self.nodes_groupbox.setStyleSheet(
            "QGroupBox#nodes_groupbox {background-color: qlineargradient("
            "spread:pad, x1:1, y1:0, x2:, y2:1, stop:0 rgb("
            "60, 60, 60), stop:1 rgb(60,60,60))};")
        self.stemcheck_groupbox = QtWidgets.QGroupBox(self.nodes_groupbox)
        self.stemcheck_groupbox.setGeometry(0, 0, 250, 70)
        self.strictnodes_groupbox = QtWidgets.QGroupBox(self.nodes_groupbox)
        self.strictnodes_groupbox.setGeometry(0, 65, 250, 70)
        self.stemcheckCheckBox = QtWidgets.QCheckBox(self.stemcheck_groupbox)
        self.stemcheckCheckBox.setGeometry(QtCore.QRect(12, 10, 150, 21))
        font = Fonts.Choose_Fonts(self, True, 9, "Arial")
        self.stemcheckCheckBox.setFont(font)
        self.stemcheckCheckBoxLabel = QtWidgets.QLabel(self.stemcheck_groupbox)
        self.stemcheckCheckBoxLabel.setObjectName("stemcheckCheckBoxLabel")
        self.stemcheckCheckBoxLabel.setGeometry(35, 10, 150, 21)
        self.stemcheckCheckBoxLabel.setFont(font)
        self.stemcheckCheckBoxLabel.setStyleSheet("color: white")
        self.stemchecktime_lineedit = QtWidgets.QLineEdit(
            self.stemcheck_groupbox)
        self.stemchecktime_lineedit.setGeometry(QtCore.QRect(5, 40, 25, 22))
        self.stemchecktime_lineedit.setObjectName("stemchecktime_lineedit")
        self.stemchecktime_lineedit.setAlignment(QtCore.Qt.AlignCenter)
        self.stemchecktime_lineedit.setFont(font)
        self.stemchecktime_lineedit.setMaxLength(2)
        self.stemchecktime_label = QtWidgets.QLabel(self.nodes_groupbox)
        self.stemchecktime_label.setGeometry(QtCore.QRect(35, 40, 170, 22))
        self.stemchecktime_label.setObjectName("stemchecktime_label")
        self.stemchecktime_label.setFont(font)
        self.stemchecktime_label.setStyleSheet("color:white")
        self.strictnodesCheckBox = QtWidgets.QCheckBox(
            self.strictnodes_groupbox)
        self.strictnodesCheckBox.setGeometry(QtCore.QRect(12, 10, 311, 21))
        font = Fonts.Choose_Fonts(self, True, 9, "Arial")
        self.strictnodesCheckBox.setFont(font)
        self.strictnodesCheckBoxLabel = QtWidgets.QLabel(
            self.strictnodes_groupbox)
        self.strictnodesCheckBoxLabel.setObjectName("strictnodesCheckBoxLabel")
        self.strictnodesCheckBoxLabel.setGeometry(35, 10, 150, 21)
        self.strictnodesCheckBoxLabel.setFont(font)
        self.strictnodesCheckBoxLabel.setStyleSheet("color: white")
        self.nodes_groupbox.hide()
        self.eyes_groupbox = QtWidgets.QGroupBox(SettingsNewDialog)
        self.eyes_groupbox.setGeometry(QtCore.QRect(150, 0, 250, 300))
        self.eyes_groupbox.setObjectName("eyes_groupbox")
        self.eyes_groupbox.setStyleSheet(
            "QGroupBox#eyes_groupbox {background-color: qlineargradient("
            "spread:pad, x1:1, y1:0, x2:, y2:1, stop:0 rgb("
            "60, 60, 60), stop:1 rgb(60,60,60))};")
        self.fiveEyesCheckBox = QtWidgets.QCheckBox(self.eyes_groupbox)
        self.fiveEyesCheckBox.setGeometry(QtCore.QRect(12, 10, 190, 21))
        self.fiveEyesCheckBox.setFont(font)
        self.fiveEyesCheckBoxLabel = QtWidgets.QLabel(self.eyes_groupbox)
        self.fiveEyesCheckBoxLabel.setObjectName("fiveEyesCheckBoxLabel")
        self.fiveEyesCheckBoxLabel.setGeometry(35, 10, 190, 21)
        self.fiveEyesCheckBoxLabel.setFont(font)
        self.fiveEyesCheckBoxLabel.setStyleSheet("color: white")
        self.nineEyesCheckBox = QtWidgets.QCheckBox(self.eyes_groupbox)
        self.nineEyesCheckBox.setGeometry(QtCore.QRect(12, 40, 190, 21))
        self.nineEyesCheckBox.setFont(font)
        self.nineEyesCheckBoxLabel = QtWidgets.QLabel(self.eyes_groupbox)
        self.nineEyesCheckBoxLabel.setObjectName("nineEyesCheckBoxLabel")
        self.nineEyesCheckBoxLabel.setGeometry(35, 40, 190, 21)
        self.nineEyesCheckBoxLabel.setFont(font)
        self.nineEyesCheckBoxLabel.setStyleSheet("color: white")
        self.fourteenEyesCheckBox = QtWidgets.QCheckBox(self.eyes_groupbox)
        self.fourteenEyesCheckBox.setGeometry(QtCore.QRect(12, 70, 190, 21))
        self.fourteenEyesCheckBox.setFont(font)
        self.fourteenEyesCheckBoxLabel = QtWidgets.QLabel(self.eyes_groupbox)
        self.fourteenEyesCheckBoxLabel.setObjectName(
            "fourteenEyesCheckBoxLabel")
        self.fourteenEyesCheckBoxLabel.setGeometry(35, 70, 190, 21)
        self.fourteenEyesCheckBoxLabel.setFont(font)
        self.fourteenEyesCheckBoxLabel.setStyleSheet("color: white")
        self.eyes_groupbox.hide()
        self.ok_Button.raise_()
        self.cancel_Button.raise_()

        self.retranslateUi(SettingsNewDialog)
        QtCore.QMetaObject.connectSlotsByName(SettingsNewDialog)

        if osf.Functions.paramstemcheck is True:
            self.stemcheckCheckBox.setChecked(True)
        else:
            self.stemcheckCheckBox.setChecked(False)

        if self.stemcheckCheckBox.isChecked():
            self.stemchecktime_lineedit.setEnabled(True)
            self.stemchecktime_label.setEnabled(True)
        else:
            self.stemchecktime_lineedit.setEnabled(False)
            self.stemchecktime_label.setEnabled(False)

        self.lineEdit.setText(osf.Functions.parampathtotor)

        self.stemchecktime_lineedit.setText(
            "{0}".format(osf.Functions.paramstemchecktime))

        if osf.Functions.torrcstrictnodes is True:
            self.strictnodesCheckBox.setChecked(True)
        else:
            self.strictnodesCheckBox.setChecked(False)

        @pyqtSlot()
        def Change_StemCheckTime():

            if self.stemchecktime_lineedit.text().isdigit():
                if (int)(self.stemchecktime_lineedit.text()) > 60:
                    self.stemchecktime_lineedit.setText("60")

                if (int)(self.stemchecktime_lineedit.text()) <= 5:
                    self.stemchecktime_lineedit.setText("5")
            else:
                self.stemchecktime_lineedit.setText(
                    "{0}".format(osf.Functions.paramstemchecktime))

        @pyqtSlot()
        def fiveeyes_changed():
            self.nineEyesCheckBox.setChecked(False)
            self.fourteenEyesCheckBox.setChecked(False)
            osf.Functions.eyes_changed = True

        @pyqtSlot()
        def nineeyes_changed():
            self.fiveEyesCheckBox.setChecked(False)
            self.fourteenEyesCheckBox.setChecked(False)
            osf.Functions.eyes_changed = True

        @pyqtSlot()
        def fourteeneyes_changed():
            self.fiveEyesCheckBox.setChecked(False)
            self.nineEyesCheckBox.setChecked(False)
            osf.Functions.eyes_changed = True

        @pyqtSlot()
        def Cancel_Clicked():
            osf.Functions.window_settings_open = False
            SettingsNewDialog.close()

        @pyqtSlot()
        def okButtonPress():
            try:
                if self.stemcheckCheckBox.isChecked() is True:
                    osf.Functions.paramstemcheck = True
                else:
                    osf.Functions.paramstemcheck = False

                osf.Functions.parampathtotor = self.lineEdit.text()

                osf.Functions.paramstemchecktime = (int)(
                    self.stemchecktime_lineedit.text())

                if self.fiveEyesCheckBox.isChecked() is True:
                    osf.Functions.Add_Eyes_ToArray(
                        self, osf.Functions.five_eye_countries)

                if self.nineEyesCheckBox.isChecked() is True:
                    osf.Functions.Add_Eyes_ToArray(
                        self, osf.Functions.five_eye_countries)

                    osf.Functions.Add_Eyes_ToArray(
                        self, osf.Functions.nine_eye_countries)

                    osf.Functions.Add_Eyes_ToArray(
                        self, osf.Functions.nine_eye_countries)

                if self.fourteenEyesCheckBox.isChecked() is True:
                    osf.Functions.Add_Eyes_ToArray(
                        self, osf.Functions.five_eye_countries)

                    osf.Functions.Add_Eyes_ToArray(
                        self, osf.Functions.nine_eye_countries)

                    osf.Functions.Add_Eyes_ToArray(
                        self, osf.Functions.fourteen_eye_countries)

                if self.strictnodesCheckBox.isChecked() is True:
                    osf.Functions.torrcstrictnodes = True
                    osf.Functions.paramstrictnodes = 1
                else:
                    osf.Functions.torrcstrictnodes = False
                    osf.Functions.paramstrictnodes = 0

                osf.Functions.ChangeTorrcStrictNodes(self)
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

                osf.Functions.window_settings_open = False

            except Exception as exc:
                osf.Functions.WriteLog(self, exc)

            osf.Functions.settingschanged = True
            if path.exists(osf.Functions.torrcfilepath) is False:
                osf.Functions.torrcfound = False
            else:
                osf.Functions.torrcfound = True

            osf.Functions.settings_closed = True
            SettingsNewDialog.close()

        @pyqtSlot()
        def StemCheckTime_Label_Visibility():
            if self.stemcheckCheckBox.isChecked():
                self.stemchecktime_lineedit.setEnabled(True)
                self.stemchecktime_label.setEnabled(True)
            else:
                self.stemchecktime_lineedit.setEnabled(False)
                self.stemchecktime_label.setEnabled(False)

        @pyqtSlot()
        def OpenFilePicker():
            try:
                folderName = QFileDialog.getExistingDirectory(
                    self, "Select Tor Directory")
                if folderName:
                    self.lineEdit.setText(folderName)

            except Exception as exc:
                osf.Functions.WriteLog(self, exc)

        @pyqtSlot()
        def Main_SelectionChanged():

            if self.main_listWidget.currentItem().text() == "General":
                self.eyes_groupbox.hide()
                self.nodes_groupbox.hide()
                self.general_groupbox.show()
                self.ok_Button.raise_()
                self.cancel_Button.raise_()

            if self.main_listWidget.currentItem().text() == "Nodes":
                self.eyes_groupbox.hide()
                self.general_groupbox.hide()
                self.nodes_groupbox.show()
                self.ok_Button.raise_()
                self.cancel_Button.raise_()

            if self.main_listWidget.currentItem().text() == "Eyes - Countries":
                self.general_groupbox.hide()
                self.nodes_groupbox.hide()
                self.eyes_groupbox.show()
                self.ok_Button.raise_()
                self.cancel_Button.raise_()

        def fiveeye_label_clicked():
            self.fiveEyesCheckBox.setChecked(
                self.fiveEyesCheckBox.isChecked() ^ True)
            fiveeyes_changed()

        def nineeye_label_clicked():
            self.nineEyesCheckBox.setChecked(
                self.nineEyesCheckBox.isChecked() ^ True)
            nineeyes_changed()

        def fourteeneye_label_clicked():
            self.fourteenEyesCheckBox.setChecked(
                self.fourteenEyesCheckBox.isChecked() ^ True)
            fourteeneyes_changed()

        def stemcheckCheckBox_Label_clicked():
            self.stemcheckCheckBox.setChecked(
                self.stemcheckCheckBox.isChecked() ^ True)
            StemCheckTime_Label_Visibility()

        def strictnodes_label_clicked():
            self.strictnodesCheckBox.setChecked(
                self.strictnodesCheckBox.isChecked() ^ True)

        self.cancel_Button.clicked.connect(Cancel_Clicked)
        self.ok_Button.clicked.connect(okButtonPress)

        self.openButton.clicked.connect(OpenFilePicker)

        self.main_listWidget.currentItemChanged.connect(Main_SelectionChanged)

        clickable(self.strictnodesCheckBoxLabel).connect(
            strictnodes_label_clicked)

        self.stemcheckCheckBox.clicked.connect(StemCheckTime_Label_Visibility)
        clickable(self.stemcheckCheckBoxLabel).connect(
            stemcheckCheckBox_Label_clicked)

        self.stemchecktime_lineedit.editingFinished.connect(
            Change_StemCheckTime)

        self.fiveEyesCheckBox.clicked.connect(fiveeyes_changed)
        clickable(self.fiveEyesCheckBoxLabel).connect(fiveeye_label_clicked)

        self.nineEyesCheckBox.clicked.connect(nineeyes_changed)
        clickable(self.nineEyesCheckBoxLabel).connect(nineeye_label_clicked)

        self.fourteenEyesCheckBox.clicked.connect(fourteeneyes_changed)
        clickable(self.fourteenEyesCheckBoxLabel).connect(
            fourteeneye_label_clicked)

        if osf.Functions.torrcfound is False:
            self.main_listWidget.takeItem(2)
            self.main_listWidget.takeItem(1)

    def retranslateUi(self, SettingsNewDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsNewDialog.setWindowTitle(_translate(
            "SettingsNewDialog", "Settings"))
        self.ok_Button.setText(_translate("SettingsNewDialog", "OK"))
        self.cancel_Button.setText(_translate("SettingsNewDialog", "Cancel"))
        self.openButton.setText(_translate("SettingsNewDialog", "Open"))
        self.pathtotorLabel.setText(_translate(
            "SettingsNewDialog", "Path to Tor Browser:"))
        self.stemcheckCheckBoxLabel.setText(_translate(
            "SettingsNewDialog", "Stem Node Check"))
        self.stemchecktime_label.setText(_translate(
            "SettingsNewDialog", "Stem Check max. Time"))
        self.strictnodesCheckBoxLabel.setText(_translate(
            "SettingsNewDialog", "StrictNodes 0/1"))
        self.fiveEyesCheckBoxLabel.setText(_translate(
            "SettingsDialog", "Block '5-Eyes' Countries"))
        self.nineEyesCheckBoxLabel.setText(_translate(
            "SettingsDialog", "Block '9-Eyes' Countries"))
        self.fourteenEyesCheckBoxLabel.setText(_translate(
            "SettingsDialog", "Block '14-Eyes' Countries"))


class Ui_UpdateDialog(object):
    def setupUi(self, UpdateDialog):
        UpdateDialog.setObjectName("UpdateDialog")
        UpdateDialog.resize(400, 250)
        UpdateDialog.setMinimumSize(QtCore.QSize(400, 250))
        UpdateDialog.setMaximumSize(QtCore.QSize(400, 250))
        UpdateDialog.setStyleSheet(
            "QDialog#UpdateDialog {background-color: qlineargradient("
            "spread:pad, x1:1, y1:0, x2:, y2:1, stop:0 rgb("
            "200,200,200), stop:1 rgb(253,253,253));}")
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
        font = Fonts.Choose_Fonts(self, True, 14, "Arial")
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(UpdateDialog)
        QtCore.QMetaObject.connectSlotsByName(UpdateDialog)

        @pyqtSlot()
        def StartUpdateProc():
            osf.Functions.paramupdateavailable = False
            osf.Functions.WriteSettingsToJson(self)
            webbrowser.open('https://github.com/Ned84/OnionSwitch/releases')

        @pyqtSlot()
        def Close_Update():
            osf.Functions.window_update_open = False
            UpdateDialog.close()

        self.cancelButton.clicked.connect(Close_Update)

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
        font = Fonts.Choose_Fonts(self, False, 9, "Arial")
        self.label3.setFont(font)

        self.label4.setText(_translate(
            "UpdateDialog", "Current Version: " + version + "\n"
            "\n"
            "New Version: " + Ui_MainWindow.versionnew + "\n"
            "\n"
            "No Update available."))

        self.label4.setFont(font)

        self.label2.setFont(font)

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


class Ui_Tor_Reset_Dialog(object):
    def setupUi(self, Tor_Reset_Dialog):
        Tor_Reset_Dialog.setObjectName("Tor_Reset_Dialog")
        Tor_Reset_Dialog.resize(400, 150)
        Tor_Reset_Dialog.setMinimumSize(QtCore.QSize(400, 150))
        Tor_Reset_Dialog.setMaximumSize(QtCore.QSize(400, 150))
        Tor_Reset_Dialog.setStyleSheet(
            "QDialog#Tor_Reset_Dialog {background-color: qlineargradient("
            "spread:pad, x1:1, y1:0, x2:, y2:1, stop:0 rgb("
            "200,200,200), stop:1 rgb(253,253,253));}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            ":/resources/OnionSwitch_Logo.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Tor_Reset_Dialog.setWindowIcon(icon)
        self.yesButton = QtWidgets.QPushButton(Tor_Reset_Dialog)
        self.yesButton.setGeometry(QtCore.QRect(180, 110, 93, 28))
        self.yesButton.setObjectName("yesButton")
        self.noButton = QtWidgets.QPushButton(Tor_Reset_Dialog)
        self.noButton.setGeometry(QtCore.QRect(290, 110, 93, 28))
        self.noButton.setObjectName("noButton")
        self.label = QtWidgets.QLabel(Tor_Reset_Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 381, 71))
        font = Fonts.Choose_Fonts(self, False, 10, "Arial")
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Tor_Reset_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Tor_Reset_Dialog)

        osf.Functions.window_torrc_reset_open = True

        @pyqtSlot()
        def Close_Dialog_Yes():
            osf.Functions.window_torrc_reset_open = False
            osf.Functions.torrc_reset_dialog_closed = True
            osf.Functions.reset_torrc_ok = True
            osf.Functions.resettorrc_changed = True
            Tor_Reset_Dialog.close()

        @pyqtSlot()
        def Close_Dialog_No():
            osf.Functions.window_torrc_reset_open = False
            osf.Functions.torrc_reset_dialog_closed = True
            Tor_Reset_Dialog.close()

        self.yesButton.clicked.connect(Close_Dialog_Yes)
        self.noButton.clicked.connect(Close_Dialog_No)

    def retranslateUi(self, Tor_Reset_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Tor_Reset_Dialog.setWindowTitle(_translate(
            "Tor_Reset_Dialog", "Information"))
        self.yesButton.setText(_translate("Tor_Reset_Dialog", "Yes"))
        self.noButton.setText(_translate("Tor_Reset_Dialog", "No"))
        self.label.setText(_translate(
            "Tor_Reset_Dialog", "This will reset your torrc.\n"
            "After reset please restart the OnionSwitch.\n"
            "Do you want to reset?."))


def clickable(widget):

    class Filter(QtCore.QObject):
        clicked = QtCore.pyqtSignal()

        def eventFilter(self, obj, event):

            if obj == widget:
                if event.type() == QtCore.QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        # The developer can opt for .emit(obj) to get the
                        # object within the slot.
                        return True

            return False

    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    styles = QtWidgets.QStyleFactory.keys()
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
