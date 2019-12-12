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

import io
import pycurl
import certifi
import threading
import os


import stem.process

import OnionSwitch_Functions as osf

from stem.util import term

SOCKS_PORT = 7000




class TorCheck(object):

    ended_successfull = False

    def query(url):
        """
        Uses pycurl to fetch a site using the proxy on the SOCKS_PORT.
        """

        output = io.BytesIO()

        query = pycurl.Curl()
        query.setopt(pycurl.URL, url)
        query.setopt(pycurl.CAINFO, certifi.where())
        query.setopt(pycurl.PROXY, 'localhost')
        query.setopt(pycurl.PROXYPORT, SOCKS_PORT)
        query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5_HOSTNAME)
        query.setopt(pycurl.WRITEFUNCTION, output.write)
        query.setopt(pycurl.TIMEOUT, 10)

        try:
            query.perform()
            return output.getvalue()
        except pycurl.error as exc:
            return "Unable to reach %s (%s)" % (url, exc)

    def Print_Bootstrap_Lines(line):

        if "Bootstrapped " in line:
            print(line)

    def CheckNode(self, countrycode):
       # try:
            website_string = ""
            found = False

            if len(countrycode) > 0:
                print(term.format("Starting Tor:\n", term.Attr.BOLD))

                tor_process = stem.process.launch_tor_with_config(
                    config={
                        'SocksPort': str(SOCKS_PORT),
                        'ExitNodes': countrycode,
                    },
                    init_msg_handler=TorCheck.Print_Bootstrap_Lines,
                )

                print(term.format(
                    "\nChecking our endpoint:\n", term.Attr.BOLD))
                website_string = term.format(TorCheck.query(
                    "https://check.torproject.org/"))
                print(term.format(
                    "\nDone!\n", term.Attr.BOLD))

                index = website_string.find(
                    "Congratulations. This browser is configured to use Tor.")

                tor_process.kill()  # stops tor
                

                if index != -1:
                    found = True
                else:
                    found = False

                TorCheck.ended_successfull = True
                return found

       # except BaseException as exc:
       #     print(exc)

    def CheckTor(self, countrycode):

        try:
            urlthread = threading.Thread(target=TorCheck.CheckNode,args=(self, countrycode), daemon=True)
            urlthread.start()
            urlthread.join(timeout=10)
            if TorCheck.ended_successfull is False:
                tasks = os.popen('tasklist').readlines()

                for task in tasks:
                    tor_index = task.find("tor.exe")
                    if tor_index != -1:
                        os.system("taskkill /f /im tor.exe")
        except Exception as exc:
            print(exc)

       
