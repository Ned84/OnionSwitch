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


class Functions(object):

    paramversion = ""
    parampathtotor = ""
    paramupdateavailable = False

    torrcexitnodes = []
    torrcexcludednodes = []
    torrcexcludedexitnodes = []

    countrynames = ["",
                    "ASCENSION ISLAND",
                    "AFGHANISTAN",
                    "ALAND",
                    "ALBANIA",
                    "ALGERIA",
                    "ANDORRA",
                    "ANGOLA",
                    "ANGUILLA",
                    "ANTARCTICA",
                    "ANTIGUA AND BARBUDA",
                    "ARGENTINA REPUBLIC",
                    "ARMENIA",
                    "ARUBA",
                    "AUSTRALIA",
                    "AUSTRIA",
                    "AZERBAIJAN",
                    "BAHAMAS",
                    "BAHRAIN",
                    "BANGLADESH",
                    "BARBADOS",
                    "BELARUS",
                    "BELGIUM",
                    "BELIZE",
                    "BENIN",
                    "BERMUDA",
                    "BHUTAN",
                    "BOLIVIA",
                    "BOSNIA AND HERZEGOVINA",
                    "BOTSWANA",
                    "BOUVET ISLAND",
                    "BRAZIL",
                    "BRITISH INDIAN OCEAN TERR.",
                    "BRITISH VIRGIN ISLANDS",
                    "BRUNEI DARUSSALAM",
                    "BULGARIA",
                    "BURKINA FASO",
                    "BURUNDI",
                    "CAMBODIA",
                    "CAMEROON",
                    "CANADA",
                    "CAPE VERDE",
                    "CAYMAN ISLANDS",
                    "CENTRAL AFRICAN REPUBLIC",
                    "CHAD",
                    "CHILE",
                    "PEOPLE’S REPUBLIC OF CHINA",
                    "CHRISTMAS ISLANDS",
                    "COCOS ISLANDS",
                    "COLOMBIA",
                    "COMORAS",
                    "CONGO",
                    "CONGO (DEMOCRATIC REPUBLIC)",
                    "COOK ISLANDS",
                    "COSTA RICA",
                    "COTE D IVOIRE",
                    "CROATIA",
                    "CUBA",
                    "CYPRUS",
                    "CZECH REPUBLIC",
                    "DENMARK",
                    "DJIBOUTI",
                    "DOMINICA",
                    "DOMINICAN REPUBLIC",
                    "EAST TIMOR",
                    "ECUADOR",
                    "EGYPT",
                    "EL SALVADOR",
                    "EQUATORIAL GUINEA",
                    "ESTONIA",
                    "ETHIOPIA",
                    "FALKLAND ISLANDS",
                    "FAROE ISLANDS",
                    "FIJI",
                    "FINLAND",
                    "FRANCE",
                    "FRANCE METROPOLITAN",
                    "FRENCH GUIANA",
                    "FRENCH POLYNESIA",
                    "FRENCH SOUTHERN TERRITORIES",
                    "GABON",
                    "GAMBIA",
                    "GEORGIA",
                    "GERMANY",
                    "GHANA",
                    "GIBRALTER",
                    "GREECE",
                    "GREENLAND",
                    "GRENADA",
                    "GUADELOUPE",
                    "GUAM",
                    "GUATEMALA",
                    "GUINEA",
                    "GUINEA-BISSAU",
                    "GUYANA",
                    "HAITI",
                    "HEARD & MCDONALD ISLAND",
                    "HONDURAS",
                    "HONG KONG",
                    "HUNGARY",
                    "ICELAND",
                    "INDIA",
                    "INDONESIA",
                    "IRAN, ISLAMIC REPUBLIC OF",
                    "IRAQ",
                    "IRELAND",
                    "ISLE OF MAN",
                    "ISRAEL",
                    "ITALY",
                    "JAMAICA",
                    "JAPAN",
                    "JORDAN",
                    "KAZAKHSTAN",
                    "KENYA",
                    "KIRIBATI",
                    "KOREA, DEM. PEOPLES REP OF",
                    "KOREA, REPUBLIC OF",
                    "KUWAIT",
                    "KYRGYZSTAN",
                    "LAO PEOPLE’S DEM. REPUBLIC",
                    "LATVIA",
                    "LEBANON",
                    "LESOTHO",
                    "LIBERIA",
                    "LIBYAN ARAB JAMAHIRIYA",
                    "LIECHTENSTEIN",
                    "LITHUANIA",
                    "LUXEMBOURG",
                    "MACAO",
                    "MACEDONIA",
                    "MADAGASCAR",
                    "MALAWI",
                    "MALAYSIA",
                    "MALDIVES",
                    "MALI",
                    "MALTA",
                    "MARSHALL ISLANDS",
                    "MARTINIQUE",
                    "MAURITANIA",
                    "MAURITIUS",
                    "MAYOTTE",
                    "MEXICO",
                    "MICRONESIA",
                    "MOLDAVA REPUBLIC OF",
                    "MONACO",
                    "MONGOLIA",
                    "MONTENEGRO",
                    "MONTSERRAT",
                    "MOROCCO",
                    "MOZAMBIQUE",
                    "MYANMAR",
                    "NAMIBIA",
                    "NAURU",
                    "NEPAL",
                    "NETHERLANDS ANTILLES",
                    "NETHERLANDS, THE",
                    "NEW CALEDONIA",
                    "NEW ZEALAND",
                    "NICARAGUA",
                    "NIGER",
                    "NIGERIA",
                    "NIUE",
                    "NORFOLK ISLAND",
                    "NORTHERN MARIANA ISLANDS",
                    "NORWAY",
                    "OMAN",
                    "PAKISTAN",
                    "PALAU",
                    "PALESTINE",
                    "PANAMA",
                    "PAPUA NEW GUINEA",
                    "PARAGUAY",
                    "PERU",
                    "PHILIPPINES (REPUBLIC OF THE)",
                    "PITCAIRN",
                    "POLAND",
                    "PORTUGAL",
                    "PUERTO RICO",
                    "QATAR",
                    "REUNION",
                    "ROMANIA",
                    "RUSSIAN FEDERATION",
                    "RWANDA",
                    "SAMOA",
                    "SAN MARINO",
                    "SAO TOME/PRINCIPE",
                    "SAUDI ARABIA",
                    "SCOTLAND",
                    "SENEGAL",
                    "SERBIA",
                    "SEYCHELLES",
                    "SIERRA LEONE",
                    "SINGAPORE",
                    "SLOVAKIA",
                    "SLOVENIA",
                    "SOLOMON ISLANDS",
                    "SOMALIA",
                    "SOMOA,GILBERT,ELLICE ISLANDS",
                    "SOUTH AFRICA",
                    "SOUTH GEORGIA, SOUTH SANDWICH ISLANDS",
                    "SOVIET UNION",
                    "SPAIN",
                    "SRI LANKA",
                    "ST. HELENA",
                    "ST. KITTS AND NEVIS",
                    "ST. LUCIA",
                    "ST. PIERRE AND MIQUELON",
                    "ST. VINCENT & THE GRENADINES",
                    "SUDAN",
                    "SURINAME",
                    "SVALBARD AND JAN MAYEN",
                    "SWAZILAND",
                    "SWEDEN",
                    "SWITZERLAND",
                    "SYRIAN ARAB REPUBLIC",
                    "TAIWAN",
                    "TAJIKISTAN",
                    "TANZANIA, UNITED REPUBLIC OF",
                    "THAILAND",
                    "TOGO",
                    "TOKELAU",
                    "TONGA",
                    "TRINIDAD AND TOBAGO",
                    "TUNISIA",
                    "TURKEY",
                    "TURKMENISTAN",
                    "TURKS AND CALCOS ISLANDS",
                    "TUVALU",
                    "UGANDA",
                    "UKRAINE",
                    "UNITED ARAB EMIRATES",
                    "UNITED KINGDOM (no new registrations)",
                    "UNITED KINGDOM",
                    "UNITED STATES",
                    "UNITED STATES MINOR OUTL.IS.",
                    "URUGUAY",
                    "UZBEKISTAN",
                    "VANUATU",
                    "VATICAN CITY STATE",
                    "VENEZUELA",
                    "VIET NAM",
                    "VIRGIN ISLANDS (USA)",
                    "WALLIS AND FUTUNA ISLANDS",
                    "WESTERN SAHARA",
                    "YEMEN",
                    "ZAMBIA",
                    "ZIMBABWE"]
    countrycodes = ["",
                    "{ac}",
                    "{af}",
                    "{ax}",
                    "{al}",
                    "{dz}",
                    "{ad}",
                    "{ao}",
                    "{ai}",
                    "{aq}",
                    "{ag}",
                    "{ar}",
                    "{am}",
                    "{aw}",
                    "{au}",
                    "{at}",
                    "{az}",
                    "{bs}",
                    "{bh}",
                    "{bd}",
                    "{bb}",
                    "{by}",
                    "{be}",
                    "{bz}",
                    "{bj}",
                    "{bm}",
                    "{bt}",
                    "{bo}",
                    "{ba}",
                    "{bw}",
                    "{bv}",
                    "{br}",
                    "{io}",
                    "{vg}",
                    "{bn}",
                    "{bg}",
                    "{bf}",
                    "{bi}",
                    "{kh}",
                    "{cm}",
                    "{ca}",
                    "{cv}",
                    "{ky}",
                    "{cf}",
                    "{td}",
                    "{cl}",
                    "{cn}",
                    "{cx}",
                    "{cc}",
                    "{co}",
                    "{km}",
                    "{cg}",
                    "{cd}",
                    "{ck}",
                    "{cr}",
                    "{ci}",
                    "{hr}",
                    "{cu}",
                    "{cy}",
                    "{cz}",
                    "{dk}",
                    "{dj}",
                    "{dm}",
                    "{do}",
                    "{tp}",
                    "{ec}",
                    "{eg}",
                    "{sv}",
                    "{gq}",
                    "{ee}",
                    "{et}",
                    "{fk}",
                    "{fo}",
                    "{fj}",
                    "{fi}",
                    "{fr}",
                    "{fx}",
                    "{gf}",
                    "{pf}",
                    "{tf}",
                    "{ga}",
                    "{gm}",
                    "{ge}",
                    "{de}",
                    "{gh}",
                    "{gi}",
                    "{gr}",
                    "{gl}",
                    "{gd}",
                    "{gp}",
                    "{gu}",
                    "{gt}",
                    "{gn}",
                    "{gw}",
                    "{gy}",
                    "{ht}",
                    "{hm}",
                    "{hn}",
                    "{hk}",
                    "{hu}",
                    "{is}",
                    "{in}",
                    "{id}",
                    "{ir}",
                    "{iq}",
                    "{ie}",
                    "{im}",
                    "{il}",
                    "{it}",
                    "{jm}",
                    "{jp}",
                    "{jo}",
                    "{kz}",
                    "{ke}",
                    "{ki}",
                    "{kp}",
                    "{kr}",
                    "{kw}",
                    "{kg}",
                    "{la}",
                    "{lv}",
                    "{lb}",
                    "{ls}",
                    "{lr}",
                    "{ly}",
                    "{li}",
                    "{lt}",
                    "{lu}",
                    "{mo}",
                    "{mk}",
                    "{mg}",
                    "{mw}",
                    "{my}",
                    "{mv}",
                    "{ml}",
                    "{mt}",
                    "{mh}",
                    "{mq}",
                    "{mr}",
                    "{mu}",
                    "{yt}",
                    "{mx}",
                    "{fm}",
                    "{md}",
                    "{mc}",
                    "{mn}",
                    "{me}",
                    "{ms}",
                    "{ma}",
                    "{mz}",
                    "{mm}",
                    "{na}",
                    "{nr}",
                    "{np}",
                    "{an}",
                    "{nl}",
                    "{nc}",
                    "{nz}",
                    "{ni}",
                    "{ne}",
                    "{ng}",
                    "{nu}",
                    "{nf}",
                    "{mp}",
                    "{no}",
                    "{om}",
                    "{pk}",
                    "{pw}",
                    "{ps}",
                    "{pa}",
                    "{pg}",
                    "{py}",
                    "{pe}",
                    "{ph}",
                    "{pn}",
                    "{pl}",
                    "{pt}",
                    "{pr}",
                    "{qa}",
                    "{re}",
                    "{ro}",
                    "{ru}",
                    "{rw}",
                    "{ws}",
                    "{sm}",
                    "{st}",
                    "{sa}",
                    "{uk}",
                    "{sn}",
                    "{rs}",
                    "{sc}",
                    "{sl}",
                    "{sg}",
                    "{sk}",
                    "{si}",
                    "{sb}",
                    "{so}",
                    "{as}",
                    "{za}",
                    "{gs}",
                    "{su}",
                    "{es}",
                    "{lk}",
                    "{sh}",
                    "{kn}",
                    "{lc}",
                    "{pm}",
                    "{vc}",
                    "{sd}",
                    "{sr}",
                    "{sj}",
                    "{sz}",
                    "{se}",
                    "{ch}",
                    "{sy}",
                    "{tw}",
                    "{tj}",
                    "{tz}",
                    "{th}",
                    "{tg}",
                    "{tk}",
                    "{to}",
                    "{tt}",
                    "{tn}",
                    "{tr}",
                    "{tm}",
                    "{tc}",
                    "{tv}",
                    "{ug}",
                    "{ua}",
                    "{ae}",
                    "{gb}",
                    "{uk}",
                    "{us}",
                    "{um}",
                    "{uy}",
                    "{uz}",
                    "{vu}",
                    "{va}",
                    "{ve}",
                    "{vn}",
                    "{vi}",
                    "{wf}",
                    "{eh}",
                    "{ye}",
                    "{zm}",
                    "{zw}"]

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

            #  Get Torrc Exit Node configuration
            index_1 = torrc_readfile.find("ExitNodes")
            if index_1 != -1:
                index_2 = torrc_readfile.find("\n", index_1)
                index_1 = index_1 + len("ExitNodes")
                sliceobject = slice(index_1, index_2)
                exitnodes = torrc_readfile[sliceobject]

                exitnodes = re.findall('{+[a-z]+}', exitnodes)

                Functions.torrcexitnodes.clear()

                exitnodename = ""
                for exitnode in exitnodes:
                    i = 0
                    for countrycode in Functions.countrycodes:
                        if countrycode == exitnode:
                            exitnodename = Functions.countrynames[i]
                        i += 1
                    Functions.torrcexitnodes.append(exitnodename)
            else:
                Functions.torrcexitnodes.clear()
                Functions.torrcexitnodes.append("No Country chosen.")

            #  Get Torrc Blacklist Exit Nodes configuration
            index_1 = torrc_readfile.find("ExcludeExitNodes")
            if index_1 != -1:
                index_2 = torrc_readfile.find("\n", index_1)
                index_1 = index_1 + len("ExcludeExitNodes")
                sliceobject = slice(index_1, index_2)
                nodes = torrc_readfile[sliceobject]

                nodes = re.findall('{+[a-z]+}', nodes)

                Functions.torrcexcludedexitnodes.clear()

                exitnodename = ""
                for exitnode in exitnodes:
                    i = 0
                    for countrycode in Functions.countrycodes:
                        if countrycode == exitnode:
                            exitnodename = Functions.countrynames[i]
                        i += 1
                    Functions.torrcexcludedexitnodes.append(exitnodename)
            else:
                Functions.torrcexcludedexitnodes.clear()
                Functions.torrcexcludedexitnodes.append("No Country chosen.")

            #  Get Torrc Blacklist All Nodes configuration
            index_1 = torrc_readfile.find("ExcludeNodes")
            if index_1 != -1:
                index_2 = torrc_readfile.find("\n", index_1)
                index_1 = index_1 + len("ExcludeNodes")
                sliceobject = slice(index_1, index_2)
                nodes = torrc_readfile[sliceobject]

                nodes = re.findall('{+[a-z]+}', nodes)

                Functions.torrcexcludednodes.clear()

                exitnodename = ""
                for exitnode in exitnodes:
                    i = 0
                    for countrycode in Functions.countrycodes:
                        if countrycode == exitnode:
                            exitnodename = Functions.countrynames[i]
                        i += 1
                    Functions.tor.append(exitnodename)
            else:
                Functions.torrcexcludednodes.clear()
                Functions.torrcexcludednodes.append("No Country chosen.")

            file.close()
        except Exception as exc:
            Functions.WriteLog(self, exc)

    def BUildModelForListView(self, listView, nodeList):
        try:

            model = QStandardItemModel(listView)

            for node in nodeList:
                modelpart = QStandardItem(node)
                modelpart.setEditable(False)
                model.appendRow(modelpart)

            return model

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
