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

def OnionSwitch(stdscr):
    key = 0
    height, width = stdscr.getmaxyx()
    title = "OnionSwitch"
    title_2 = "Easily switch the Tor-Exit-Node Destination Country in your Tor-Browser."
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
            stdscr.addstr(0,0, "1: Choose Node")
            stdscr.addstr(1,0, "2: Blacklist Node")
            stdscr.addstr(2,0, "3: Blacklist Exit Node")
            stdscr.addstr(3,0, "----------------------")
            stdscr.addstr(4,0, "4: Settings")
            stdscr.addstr(5,0, "5: Help")
            stdscr.addstr(height-1, 0, infobarstr, curses.A_REVERSE)
            stdscr.refresh()

        # Settings
        if key == ord('4'):
            stdscr.clear()
            
            stdscr.refresh()
            osf.Functions.GetSettingsFromJson()
            stdscr.addstr(0,0, "Path to Tor-Browser:", curses.A_REVERSE)
            stdscr.addstr(2,10,"{0}".format(osf.Functions.parampathtotor))
            stdscr.addstr(height-1, 0, infobarstr, curses.A_REVERSE)
            stdscr.move(5,0)
            stdscr.refresh()
            curses.echo()
            input = stdscr.getstr(0, 0, 50)
            stdscr.addstr(5,0, input)
            stdscr.refresh()

            




        # Wait for next input
        key = stdscr.getch()

def main():
    curses.wrapper(OnionSwitch)


if __name__ == "__main__":
    main()
