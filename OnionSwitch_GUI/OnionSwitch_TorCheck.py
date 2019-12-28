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
import signal
from subprocess import check_output


import stem.process

from stem.util import term

SOCKS_PORT = 7000


class TorCheck(object):

    ended_successfull = False
    connected = False

    def Print_Bootstrap_Lines(line):
        # print or process msg handler and check for msg "100%! done"

        if "Bootstrapped " in line:
            print(line)
            if line.find("100%") != -1:
                TorCheck.connected = True

    def CheckNode(self, countrycode, platform, pathtotor):
        try:
            # Start tor_process and check if Node is available
            if len(countrycode) > 0:
                print(term.format("Starting Tor:\n", term.Attr.BOLD))

                if platform == "Windows":
                    tor_process = stem.process.launch_tor_with_config(
                        config={
                            'SocksPort': str(SOCKS_PORT),
                            'ExitNodes': countrycode,
                        },
                        tor_cmd=pathtotor +
                        "\\Browser\\TorBrowser\\Tor\\tor.exe",
                        init_msg_handler=TorCheck.Print_Bootstrap_Lines,
                    )

                    tor_process.kill()  # stops tor

                    TorCheck.ended_successfull = True
                    return TorCheck.connected

                if platform == "Linux":
                    tor_process = stem.process.launch_tor_with_config(
                        config={
                            'SocksPort': str(SOCKS_PORT),
                            'ExitNodes': countrycode,
                        },
                        # tor_cmd=pathtotor + "/Browser/TorBrowser/Tor/tor",
                        init_msg_handler=TorCheck.Print_Bootstrap_Lines,
                    )

                    tor_process.kill()  # stops tor

                    TorCheck.ended_successfull = True
                    return TorCheck.connected

        except Exception:
            TorCheck.ended_successfull = False

    def CheckTor(self, countrycode, platform, stemcheck, pathtotor):

        try:
            # If tor.exe is already started, quit it and start a new thread to
            # check Nodes.
            # Thread timeouts after 10 sec.
            # Check again if tor.exe is still running (because of possible
            # timeout) and delete it if so.

            if countrycode != "":
                TorCheck.connected = False

                if stemcheck is True:
                    if platform == "Windows":
                        tasks = os.popen('tasklist').readlines()

                        for task in tasks:
                            tor_index = task.find("tor.exe")
                            if tor_index != -1:
                                if tor_index == 0:
                                    os.system("taskkill /f /im tor.exe")

                    if platform == "Linux":
                        try:
                            pid = check_output(["pidof", "tor"])
                            pid = pid.split()
                            for id in pid:
                                os.kill(int(id), signal.SIGKILL)
                        except Exception:
                            pass

                    torcheck_thread = threading.Thread(
                        target=TorCheck.CheckNode, args=(
                            self, countrycode,
                            platform, pathtotor), daemon=True)

                    torcheck_thread.start()

                    torcheck_thread.join(timeout=10)

                    if TorCheck.ended_successfull is False:
                        if platform == "Windows":
                            tasks = os.popen('tasklist').readlines()

                            for task in tasks:
                                tor_index = task.find("tor.exe")
                                if tor_index != -1:
                                    if tor_index == 0:
                                        os.system("taskkill /f /im tor.exe")

                        if platform == "Linux":
                            try:
                                pid = check_output(["pidof", "tor"])
                                os.kill(int(pid), signal.SIGKILL)
                            except Exception:
                                pass
                else:
                    TorCheck.connected = True
        except Exception as exc:
            print(exc)
