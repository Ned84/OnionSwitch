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

import os
import sys
import datetime
import json
import re

from PyQt5.QtGui import QStandardItem, QStandardItemModel


class TestFunctions(object):

    paramversion = ""
    parampathtotor = ""
    paramupdateavailable = False

    torrcexitnodes = []
    torrcexcludednodes = []
    torrcexcludedexitnodes = []

    def test_GetSettingsFromJson(self):

        try:
            file = open(
                os.getenv(
                    'LOCALAPPDATA') + '\\OnionSwitch\\osparam\\Param.json')
            json_array = json.load(file)
            param_list = []

            for item in json_array:
                param_details = {}
                param_details['Path_to_Tor'] = item['Path_to_Tor']
                param_details['version'] = item['version']
                param_details['Update_available'] = item['Update_available']
                param_list.append(param_details)
            file.close()

            TestFunctions.parampathtotor = param_details['Path_to_Tor']
            TestFunctions.paramupdateavailable = \
                param_details['Update_available']

        except Exception:
            TestFunctions.test_WriteLog(self,)

    def test_WriteSettingsToJson(self):
        try:
            file = open(os.getenv(
                'LOCALAPPDATA') + '\\OnionSwitch\\osparam\\Param.json', "r")
            param_list = []

            param_details = {}
            param_details['Path_to_Tor'] = TestFunctions.parampathtotor
            param_details['version'] = TestFunctions.paramversion
            param_details['Update_available'] =\
                TestFunctions.paramupdateavailable
            param_list.append(param_details)
            file.close()

            file = open(os.getenv(
                'LOCALAPPDATA') + '\\OnionSwitch\\osparam\\Param.json', "w")
            json.dump(param_list, file, indent=1, sort_keys=True)
            file.close()

        except Exception:
            TestFunctions.test_WriteLog(self)

    def test_GetTorrcFromFile(self):

        try:
            file = open(os.getenv(
                'LOCALAPPDATA') + '\\OnionSwitch\\osparam\\torrc')
            torrc_readfile = file.read()

            index_1 = torrc_readfile.find("ExitNodes")
            index_2 = torrc_readfile.find("\n", index_1)
            index_1 = index_1 + len("ExitNodes")
            sliceobject = slice(index_1, index_2)
            exitnodes = torrc_readfile[sliceobject]

            exitnodes = re.findall('{+[a-z]+}', exitnodes)

            for exitnode in exitnodes:
                print(exitnode)

            file.close()
        except Exception as exc:
            TestFunctions.WriteLog(self, exc)

    def test_GetTorrcFromFile(self):
        try:
            file = open(os.getenv(
                'LOCALAPPDATA') + '\\OnionSwitch\\osparam\\torrc')
            torrc_readfile = file.read()

            #  Get Torrc Exit Node configuration
            index_1 = torrc_readfile.find("ExitNodes")
            if index_1 != -1:
                index_2 = torrc_readfile.find("\n", index_1)
                index_1 = index_1 + len("ExitNodes")
                sliceobject = slice(index_1, index_2)
                exitnodes = torrc_readfile[sliceobject]

                exitnodes = re.findall('{+[a-z]+}', exitnodes)

                TestFunctions.torrcexitnodes.clear()

                exitnodename = ""
                for exitnode in exitnodes:
                    i = 0
                    for countrycode in TestFunctions.countrycodes:
                        if countrycode == exitnode:
                            exitnodename = TestFunctions.countrynames[i]
                        i += 1
                    TestFunctions.torrcexitnodes.append(exitnodename)
            else:
                TestFunctions.torrcexitnodes.clear()
                TestFunctions.torrcexitnodes.append("No Country chosen.")

            #  Get Torrc Blacklist Exit Nodes configuration
            index_1 = torrc_readfile.find("ExcludeExitNodes")
            if index_1 != -1:
                index_2 = torrc_readfile.find("\n", index_1)
                index_1 = index_1 + len("ExcludeExitNodes")
                sliceobject = slice(index_1, index_2)
                nodes = torrc_readfile[sliceobject]

                nodes = re.findall('{+[a-z]+}', nodes)

                TestFunctions.torrcexcludedexitnodes.clear()

                exitnodename = ""
                for exitnode in exitnodes:
                    i = 0
                    for countrycode in TestFunctions.countrycodes:
                        if countrycode == exitnode:
                            exitnodename = TestFunctions.countrynames[i]
                        i += 1
                    TestFunctions.torrcexcludedexitnodes.append(exitnodename)
            else:
                TestFunctions.torrcexcludedexitnodes.clear()
                TestFunctions.torrcexcludedexitnodes.append("No Country chosen.")

            #  Get Torrc Blacklist All Nodes configuration
            index_1 = torrc_readfile.find("ExcludeNodes")
            if index_1 != -1:
                index_2 = torrc_readfile.find("\n", index_1)
                index_1 = index_1 + len("ExcludeNodes")
                sliceobject = slice(index_1, index_2)
                nodes = torrc_readfile[sliceobject]

                nodes = re.findall('{+[a-z]+}', nodes)

                TestFunctions.torrcexcludednodes.clear()

                exitnodename = ""
                for exitnode in exitnodes:
                    i = 0
                    for countrycode in TestFunctions.countrycodes:
                        if countrycode == exitnode:
                            exitnodename = TestFunctions.countrynames[i]
                        i += 1
                    TestFunctions.tor.append(exitnodename)
            else:
                TestFunctions.torrcexcludednodes.clear()
                TestFunctions.torrcexcludednodes.append("No Country chosen.")

            file.close()
        except Exception:
            TestFunctions.test_WriteLog(self)

    def test_BUildModelForListView(self):
        listView = ""
        nodeList = ""
        try:

            model = QStandardItemModel(listView)

            for node in nodeList:
                modelpart = QStandardItem(node)
                modelpart.setEditable(False)
                model.appendRow(modelpart)

            return model

        except Exception:
            TestFunctions.test_WriteLog(self)

    def test_WriteLog(self):
        exc = ""
        logfile = open(os.getenv(
            'LOCALAPPDATA') + '\\OnionSwitch\\Logfiles\\oslog.txt', "a")
        dt = datetime.datetime.now()
        dtwithoutmill = dt.replace(microsecond=0)
        logfile.write("{0}".format(dtwithoutmill))
        logfile.write(": ")
        logfile.write("{0}".format(sys.exc_info()[0]))
        logfile.write(" -----> ")
        logfile.write("{0}".format(exc))
        logfile.write("\n\r")
        logfile.close()
        print(sys.exc_info()[0])
        print(exc)
