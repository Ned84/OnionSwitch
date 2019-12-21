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

def OnionSwitch(stdscr):
    key = 0
    screen = curses.initscr()

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Loop where k is the last character pressed
    while (key != ord('q')):

        # Initializationq
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Refresh the screen
        stdscr.refresh()


        # Wait for next input
        key = stdscr.getch()

def main():
    curses.wrapper(OnionSwitch)


if __name__ == "__main__":
    main()
