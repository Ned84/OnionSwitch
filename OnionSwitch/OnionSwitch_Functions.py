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


class Functions(object):

    paramversion = ""
    parampathtotor = ""
    paramupdateavailable = False

    torrcexitnodes = []
    torrcexcludednodes = []
    torrcexcludedexitnodes = []

    def __init__(self):
        pass

    def GetSettingsFromJson(self):

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

            Functions.parampathtotor = param_details['Path_to_Tor']
            Functions.paramupdateavailable = param_details['Update_available']

        except Exception as exc:
            Functions.WriteLog(self, exc)

    def WriteSettingsToJson(self):
        try:
            file = open(os.getenv(
                'LOCALAPPDATA') + '\\OnionSwitch\\osparam\\Param.json', "r")
            param_list = []

            param_details = {}
            param_details['Path_to_Tor'] = Functions.parampathtotor
            param_details['version'] = Functions.paramversion
            param_details['Update_available'] = Functions.paramupdateavailable
            param_list.append(param_details)
            file.close()

            file = open(os.getenv(
                'LOCALAPPDATA') + '\\OnionSwitch\\osparam\\Param.json', "w")
            json.dump(param_list, file, indent=1, sort_keys=True)
            file.close()

        except Exception as exc:
            Functions.WriteLog(self, exc)

    def GetTorrcFromFile(self):

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
            Functions.WriteLog(self, exc)

    def WriteLog(self, exc):
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
