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

import curses
import OnionSwitch_Functions as osf
import os
from os import path
import json


version = "1.0"


class OnionSwitch_Terminal(object):

    def __init__(self, *args, **kwargs):
        try:
            super().__init__()

            osf.Functions.paramversion = version

            if path.exists(os.getenv(
                    'LOCALAPPDATA') + '\\OnionSwitch') is False:
                os.mkdir(os.getenv('LOCALAPPDATA') + '\\OnionSwitch')

            if path.exists(os.getenv(
                    'LOCALAPPDATA') + '\\OnionSwitch\\osparam') is False:
                os.mkdir(os.getenv('LOCALAPPDATA') + '\\OnionSwitch\\osparam')

            if path.exists(os.getenv(
                    'LOCALAPPDATA') + '\\OnionSwitch\\logfiles') is False:
                os.mkdir(os.getenv('LOCALAPPDATA') + '\\OnionSwitch\\logfiles')

            if path.exists(os.getenv(
                    'LOCALAPPDATA') + (
                        '\\OnionSwitch\\osparam\\Param.json')) is False:
                file = open(os.getenv('LOCALAPPDATA') +
                            '\\OnionSwitch\\osparam\\Param.json', "w+")

                data = [{"version": version, "Path_to_Tor": "",
                         "Update_available": False, "StrictNodes": 1}]

                json.dump(data, file, indent=1, sort_keys=True)
                file.close()

            if path.exists(
                    os.getenv('LOCALAPPDATA') +
                    '\\OnionSwitch\\logfiles\\oslog.txt') is False:

                file = open(os.getenv('LOCALAPPDATA') +
                            '\\OnionSwitch\\logfiles\\oslog.txt', "w+")
                file.close()

            osf.Functions.GetSettingsFromJson()

        except Exception as exc:
            osf.Functions.WriteLog(exc)

    def OnionSwitch(stdscr):
        key = 0
        recentmenu = ""
        jumponce = False
        height, width = stdscr.getmaxyx()

        stdscr.clear()
        stdscr.refresh()

        title_x = int((width // 2) - (33 // 2) - 33 % 2)
        title_y = int((height // 2) - 2)

        stdscr.addstr(
            title_y - 7, title_x, 
            "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        stdscr.addstr(
            title_y - 6, title_x, 
            "@@@@@@@@@@@@@@#(((((((@@@@@@@@@@@@@@@@@@@@@@")
        stdscr.addstr(
            title_y - 5, title_x, 
            "@@@@@@@@@@@@&((((((/((((#@@@@@@@@@@@@@@@@@@@")
        stdscr.addstr(
            title_y - 4, title_x, 
            "@@@@@@@@@@@#(((((#@@@@@@(((@@@@@@@@@@@@@@@@@")
        stdscr.addstr(
            title_y - 3, title_x, 
            "@@@@@@@@@@#(((((((@@#(((&@(((@@@@@@@@@@@@@@@")
        stdscr.addstr(
            title_y - 2, title_x, 
            "@@@@@@@@@@((((((((#@((((((%@((&@@@@@@@@@@@@@")
        stdscr.addstr(
            title_y - 1, title_x, 
            "@@@@@@@@@#(((((((((%@((#@@((&(((@@@@@@@@@@@@")
        stdscr.addstr(
            title_y, title_x,     
            "@@@@@@@@@(((((((((((#@((#@@((#@((@@@@@@@@@@@")
        stdscr.addstr(
            title_y + 1, title_x, 
            "@@@@@@@@@(((((((((((((@@((##((#@((@@@@@@@@@@")
        stdscr.addstr(
            title_y + 2, title_x, 
            "@@@@@@@@@@((((((((((((((@@(((((@@((@@@@@@@@@")
        stdscr.addstr(
            title_y + 3, title_x, 
            "@@@@@@@/((((((((((((((((((@@@@@@@(((@@@@@@@@")
        stdscr.addstr(
            title_y + 4, title_x, 
            "@@@@@@@@@(((((((((((((((((((#@@@&(((@@@@@@@@")
        stdscr.addstr(
            title_y + 5, title_x, 
            "@@@@@@//((((((((((((((((((((((((((((@@@@@@@@")
        stdscr.addstr(
            title_y + 6, title_x, 
            "@@@@@@@@@#(/((/((((((((((((((((((((@@@@@@@@@")
        stdscr.addstr(
            title_y + 7, title_x, 
            "@@@@@@@@@@@(/((#(@((((((((((((((@@@@@@@@@@@@")
        stdscr.addstr(
            title_y + 8, title_x, 
            "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

        stdscr.refresh()

        curses.napms(1000)

        stdscr.clear()
        stdscr.refresh()

        title = "OnionSwitch"
        title_2 = "Easily switch the Tor-Exit-Node Destination "
        "Country in your Tor-Browser."
        title_3 = "Copyright (C) 2019  Ned84 ned84@protonmail.com"
        title_x = int((width // 2) - (len(title) // 2) - len(title) % 2)
        title_2_x = int((width // 2) - (len(title_2) // 2) - len(title_2) % 2)
        title_3_x = int((width // 2) - (len(title_3) // 2) - len(title_3) % 2)
        title_y = int((height // 2) - 2)

        # Clear and refresh the screen for a blank canvas
        stdscr.clear()
        stdscr.refresh()

        # Introduction
        stdscr.addstr(title_y, title_x, title)
        stdscr.addstr(title_y + 1, title_2_x, title_2)
        stdscr.addstr(title_y + 2, title_3_x, title_3)
        stdscr.refresh()
        curses.napms(1000)
        stdscr.clear()
        stdscr.refresh()

        key = ord('m')

        # Loop where k is the last character pressed
        while (key != ord('Z')):

            # Initialization
            stdscr.clear()

            infobarstr = "Press 'Z' to exit| Press 'm' for Main Menu"

            # Mainview
            if key == ord('m'):
                jumponce = False
                recentmenu = "Main"
                stdscr.addstr(0, 0, "OnionSwitch: Main Menu")
                stdscr.addstr(1, 0, "----------------------")
                stdscr.addstr(2, 0, "1: Choose Node")
                stdscr.addstr(3, 0, "2: Blacklist Node")
                stdscr.addstr(4, 0, "3: Blacklist Exit Node")
                stdscr.addstr(5, 0, "----------------------")
                stdscr.addstr(6, 0, "4: Settings")
                stdscr.addstr(7, 0, "5: Help")
                stdscr.addstr(height-1, 0, infobarstr, curses.A_REVERSE)
                stdscr.refresh()

            # Settings
            if (key == ord('4') and recentmenu == "Main") or recentmenu == "Settings":
                stdscr.clear()
                recentmenu = "Settings"
                answer = ""
                jumponce = False
                stdscr.refresh()

                osf.Functions.GetTorrcFromFile()

                if osf.Functions.torrcfound is True:
                    stdscr.addstr(0, 0, "OnionSwitch: Settings | Torrc found")
                else:
                    stdscr.addstr(0, 0, "OnionSwitch: Settings | Torrc not found")
                stdscr.addstr(1, 0, "----------------------")
                stdscr.addstr(3, 0, "Path to Tor-Browser:", curses.A_REVERSE)
                stdscr.addstr(
                    5, 10, "{0}".format(osf.Functions.parampathtotor))
                stdscr.addstr(7, 0, "Do you want to change this path?(y, n)")
                stdscr.addstr(height-1, 0, infobarstr, curses.A_REVERSE)
                
                stdscr.refresh()

                answer = stdscr.getch()

                if answer == ord('y'):
                    stdscr.clear()
                    stdscr.addstr(
                        height-1, 0, infobarstr +
                        "| Enter Path to Tor-Browser", curses.A_REVERSE)
                    stdscr.refresh()
                    curses.echo()
                    input = stdscr.getstr(0, 0, 100)
                    input = "{0}".format(input)
                    input = input[2:]
                    input = input.replace("'", "")
                    input = input.replace("\\\\", "/")
                    osf.Functions.parampathtotor = "{0}".format(input)
                    osf.Functions.WriteSettingsToJson()
                    osf.Functions.GetSettingsFromJson()
                    curses.noecho()
                    key = ord('m')
                    jumponce = True
                    stdscr.refresh()
                else:
                    if answer == ord('Z'):
                        key = ord('Z')
                        jumponce = True

                    if answer == ord('m') or answer == ord('n'):
                        key = ord('m')
                        jumponce = True

            # Help Menu
            if (key == ord(
                    '5') and recentmenu == "Main") or recentmenu == "Help":
                stdscr.clear()
                recentmenu = "Help"
                jumponce = False
                stdscr.refresh()

                stdscr.addstr(0, 0, "OnionSwitch: Help")
                stdscr.addstr(1, 0, "-----------------")
                stdscr.addstr(2, 0, "1: Tor Metrics")
                stdscr.addstr(3, 0, "2: Update")
                stdscr.addstr(4, 0, "3: About")
                stdscr.addstr(height-1, 0, infobarstr, curses.A_REVERSE)
                stdscr.refresh()

            # Help Menu Tor Metrics
            if key == ord('1') and recentmenu == "Help":
                stdscr.clear()
                answer = ""
                jumponce = False
                stdscr.refresh()

                stdscr.addstr(0, 0, "OnionSwitch: Help | Tor Metrics")
                stdscr.addstr(1, 0, "-------------------------------")
                stdscr.addstr(
                    3, 10, "It is possible to copy the "
                    "Tor-Metrics URL to your clipboard,")
                stdscr.addstr(
                    4, 10, "so you can open it in the browser of your choice.")
                stdscr.addstr(6, 10, "Do you want to copy the URL? (y, n)")
                stdscr.addstr(height-1, 0, infobarstr, curses.A_REVERSE)
                stdscr.refresh()

                answer = stdscr.getch()

                if answer == ord('y'):
                    os.system('echo ' + "https://metrics."
                                        "torproject.org/rs.html"
                                        "#search/flag:exit%20country:at%20" +
                                        '| clip')

                    stdscr.clear()
                    stdscr.refresh()
                    text_x = int((
                        width // 2) - (len(title) // 2) - len(title) % 2)
                    text_y = int((height // 2) - 2)

                    stdscr.addstr(0, 0, "OnionSwitch: Help | Tor Metrics")
                    stdscr.addstr(1, 0, "-------------------------------")
                    stdscr.addstr(
                        text_y, text_x, "Tor-Metrics URL copied to "
                        "the clipboard.", curses.A_REVERSE)
                    stdscr.refresh()
                    curses.napms(3000)

                    recentmenu = "Help"
                    key = ord('5')
                    jumponce = True
                else:
                    if answer == ord('Z'):
                        key = ord('Z')
                        jumponce = True
                    else:
                        recentmenu = "Help"
                        key = ord('5')
                        jumponce = True

            # Help Menu Update
            if (key == ord('2') and recentmenu == "Help") or recentmenu == "Update":
                stdscr.clear()
                answer = ""
                jumponce = False
                recentmenu = "Update"
                stdscr.refresh()

                stdscr.addstr(0, 0, "OnionSwitch: Help | Update")
                stdscr.addstr(1, 0, "-------------------------------")
                stdscr.addstr(
                    3, 10, "Checking for Update please stand by.")
                stdscr.addstr(
                    height-1, 0, infobarstr + "| Press 'b' to return "
                    "to last menu.", curses.A_REVERSE)
                stdscr.refresh()







            # Help Menu About
            if (key == ord(
                    '3') and recentmenu == "Help") or recentmenu == "About":
                stdscr.clear()
                answer = ""
                recentmenu = "About"
                jumponce = False
                text_x = int((width // 2) - (len(title) // 2) - len(title) % 2)
                text_y = int((height // 2) - 2)
                stdscr.refresh()

                stdscr.addstr(0, 0, "OnionSwitch: Help | About")
                stdscr.addstr(1, 0, "-------------------------------")
                stdscr.addstr(text_y - 2, text_x, "Version: " + version)
                stdscr.addstr(
                    text_y - 1, text_x, "Easily switch the Tor-Exit-Node")
                stdscr.addstr(text_y, text_x, "Destination Country in your")
                stdscr.addstr(text_y + 1, text_x, "Tor-Browser.")
                stdscr.addstr(text_y + 3, text_x, "Copyright (C) 2019  Ned84")
                stdscr.addstr(text_y + 4, text_x, "ned84@protonmail.com")
                stdscr.addstr(
                    height-1, 0, infobarstr + "| Press 'b' to return "
                    "to last menu.", curses.A_REVERSE)
                stdscr.refresh()

                answer = stdscr.getch()

                if answer == ord('Z'):
                    key = ord('Z')
                    jumponce = True

                if answer == ord('b'):
                    recentmenu = "Help"
                    key = ord('5')
                    jumponce = True

                if answer == ord('m'):
                    recentmenu = "Main"
                    key = ord('m')
                    jumponce = True

            # Wait for input
            if jumponce is False:
                key = stdscr.getch()


def main():
    OnionSwitch_Terminal()
    curses.wrapper(OnionSwitch_Terminal.OnionSwitch)


if __name__ == "__main__":
    main()
