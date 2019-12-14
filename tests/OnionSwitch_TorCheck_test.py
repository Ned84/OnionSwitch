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


import threading
import os
import stem.process
from mock import MagicMock

from stem.util import term

SOCKS_PORT = 7000


class TestTorCheck(object):

    ended_successfull = False
    connected = False

    def test_Print_Bootstrap_Lines(line):
        line = ""
        if "Bootstrapped " in line:
            print(line)
            if line.find("100%") != -1:
                TestTorCheck.connected = True

    def test_CheckNode(self):
        countrycode = ""

        TestTorCheck.connected = False
        if len(countrycode) > 0:
            print(term.format("Starting Tor:\n", term.Attr.BOLD))

            tor_process = stem.process.launch_tor_with_config(
                config={
                    'SocksPort': str(SOCKS_PORT),
                    'ExitNodes': countrycode,
                },
                init_msg_handler=TestTorCheck.Print_Bootstrap_Lines,
            )

            tor_process.kill()  # stops tor

            TestTorCheck.ended_successfull = True
            return TestTorCheck.connected

    def test_CheckTor(self):

        countrycode = ""
        tasks = os.popen('tasklist').readlines()

        for task in tasks:
            tor_index = task.find("tor.exe")
            if tor_index != -1:
                os.system("taskkill /f /im tor.exe")
        urlthread = threading.Thread(target=TestTorCheck.test_CheckNode, args=(
            self, countrycode), daemon=True)
        urlthread.start()
        urlthread.join(timeout=10)
        if TestTorCheck.ended_successfull is False:
            tasks = os.popen('tasklist').readlines()

            for task in tasks:
                tor_index = task.find("tor.exe")
                if tor_index != -1:
                    os.system("taskkill /f /im tor.exe")
