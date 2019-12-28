# OnionSwitch

[![GitHub license](https://img.shields.io/github/license/Ned84/BreaktimeWatch?color=blue&style=plastic)](https://github.com/Ned84/OnionSwitch/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/Ned84/BreaktimeWatch?style=plastic)](https://github.com/Ned84/OnionSwitch/issues)
[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2F%2FNed84%2FOnionSwitch%2Fbadge&style=plastic)](https://actions-badge.atrox.dev//Ned84/OnionSwitch/goto)
[![CircleCI](https://circleci.com/gh/Ned84/OnionSwitch.svg?style=svg)](https://circleci.com/gh/Ned84/OnionSwitch)

* [Description](#description)
  * [StrictNodes](#strictnodes)
  * [Tor Metrics](#tor-metrics)
  * [Linux Versions](#linux-versions)
* [Dependencies](#dependencies)
  * [Windows](#windows)
  * [Linux](#linux)
  * [Tor Browser](#tor-browser)
* [License](#license)
* [Install](#install)
  * [Windows](#windows)
    * [Build executable GUI Version from .py](#build-executable-gui-version-from-py)
  * [Linux](#linux)
    * [Build .app GUI Version from .py](#build-app-gui-version-from-py)
* [Support](#support)
* [Verify Signatures](#verify-signatures)
  * [Windows](#windows)
  * [Linux](#linux)
* [Get my Public Key](#get-my-public-key)

## Description

Interface to easily switch the Tor-Exit-Node Destination Country in your Tor-Browser.
It is possible to force exit nodes to a specific country, exlude exit node countries and/or exclude countries for every Relay not only the exit relay.

Please close the Tor-Browser (if opened) before starting and using OnionSwitch

![OnionSwitch GUI](https://github.com/Ned84/OnionSwitch/blob/master/Screenshots/OnionSwitch_GUI.png)

Choose the path to your Tor-Browser in the Settings (the very first folder in the Tor-Browser structure) as shown below (in Edit -> Settings).
In the Settings its possible to turn off the Stem Node Check which connects to an exit when choosing a country to check if the exit country is available or not. If you experience problems with Stem you can turn it off here.

![OnionSwitch TorPath](https://github.com/Ned84/OnionSwitch/blob/master/Screenshots/Settings.png)

Node-Country can be chosen in the dropbox or it is possible to write the country code directly into the countrycode-box underneath the dropbox.
Only valid countrycodes work, otherwise the line will get deleted.

![OnionSwitch GUI](https://github.com/Ned84/OnionSwitch/blob/master/Screenshots/OnionSwitch_GUI2.png)

After choosing the country, its possible to add it to the torrc with clicking the button "Choose Node" or "Blacklist" respectively.

![OnionSwitch GUI](https://github.com/Ned84/OnionSwitch/blob/master/Screenshots/OnionSwitch_GUI3.png)

OnionSwitch will try to connect to an ExitNode in this country. This can take up to max. 10 seconds because OnionSwitch will try to connect to the Exitcountry you chose.
If no exitnode is found it will tell you so, otherwise your chosen country will be added to the list.

![OnionSwitch GUI](https://github.com/Ned84/OnionSwitch/blob/master/Screenshots/OnionSwitch_GUI4.png)

### StrictNodes

If StrictNodes is set to 1, Tor will treat the ExcludeNodes option as a requirement to follow for all the circuits you generate, even if doing so will break functionality for you. If StrictNodes is set to 0, Tor will still try to avoid nodes in the ExcludeNodes list, but it will err on the side of avoiding unexpected errors. Specifically, StrictNodes 0 tells Tor that it is okay to use an excluded node when it is necessary to perform relay reachability self-tests, connect to a hidden service, provide a hidden service to a client, fulfill a .exit request, upload directory information, or download directory information.

Please refer to the Tor manual [here](https://2019.www.torproject.org/docs/tor-manual.html.en) for more information.

### Tor Metrics

In the menubar under "Help" you will find the option "Tor Metrics".
If you want to search for specific or overall available Exit nodes, click on "Tor Metrics" and it will copy the URL to tor-metrics into your clipboard, so you can open it in the browser of your choice without being forced to connect to the torproject with your normal browser if you dont want to.

### Linux Versions

OnionSwitch is tested in **Ubuntu**.

## Dependencies

### Windows

Newest Python from [here](https://www.python.org/downloads/).

```pip install PyQt5```

PYQT5 information at [this link](https://pypi.org/project/PyQt5/).

```pip install Stem```

Stem information are [here](https://stem.torproject.org/).

```pip install pyinstaller```

Optional Pyinstaller. Infos are [here](https://www.pyinstaller.org/downloads.html).

```pip install tor```

Tor PyPi information from [here](https://pypi.org/project/tor/).

### Linux

Newest Python from [here](https://www.python.org/downloads/).

```pip3 install PyQt5```

PYQT5 information at [this link](https://pypi.org/project/PyQt5/).

```pip3 install Stem```

Stem information are [here](https://stem.torproject.org/).

```pip3 install pyinstaller```

Optional Pyinstaller. Infos are [here](https://www.pyinstaller.org/downloads.html).

```pip3 install tor```

Tor PyPi information from [here](https://pypi.org/project/tor/).

### Tor Browser

Get the Tor Browser from the Tor Project site [here](https://www.torproject.org/).

## License

>Copyright (C) 2019  Ned84 ned84@protonmail.com
>This program is free software: you can redistribute it and/or modify
>it under the terms of the GNU General Public License as published by
>the Free Software Foundation, either version 3 of the License, or
>(at your option) any later version.
>This program is distributed in the hope that it will be useful,
>but WITHOUT ANY WARRANTY; without even the implied warranty of
>MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
>GNU General Public License for more details.
>You should have received a copy of the GNU General Public License
>along with this program.  If not, see <https://www.gnu.org/licenses/>.

## Install

### Windows

#### Build executable GUI Version from .py

```pip install pyinstaller```

```pip install PyQt5```

```pip install Stem```

Use Pyinstaller from within the OnionSwitch_GUI folder.

```pyinstaller --windowed --icon=Icon/onionswitch_icon.ico --clean --name OnionSwitch OnionSwitch_GUI.py```

### Linux

#### Build .app GUI Version from .py

```pip3 install pyinstaller```

```pip3 install PyQt5```

```pip3 install Stem```

```pip3 install tor```

```pyinstaller --windowed --icon=Icon/onionswitch_icon.ico --clean --name OnionSwitch OnionSwitch_GUI.py```

## Support

If you require help or if you have suggestions please refer to the [Issue section](https://github.com/Ned84/OnionSwitch/issues).

## Verify Signatures

### Windows

Download the sha256sum.txt and the .asc for your OnionSwitch version.

#### Basic checksum verification

In Powershell:

```(Get-FileHash .\OnionSwitch*.*_setup.exe).Hash -eq (Get-Content .\sha256sum.txt).split(" ")[0].ToUpper()```

should show:

```True```

#### Signature verification

The programm is sign with my signature which windows checks when you run OnionSwitch setup.

It should state **"Open Source Developer, Rene Mario Baumgartner"** as Verified Publisher.

### Linux

Download the sha256sum.txt and the .asc for your OnionSwitch version.

#### Basic checksum verification:

```shasum -a 256 -c sha256sum.txt```

should show:

```OnionSwitch_V*.*.tar.xz: OK``` 

#### GPG verification

```curl https://keybase.io/ned84/pgp_keys.asc | gpg --import```

and verify with:

```gpg --verify OnionSwitch_V*.*.tar.xz.asc```

should show:

```Good signature from "Ned84 <ned84@protonmail.com>"```



## Get my Public Key

Get my public key at [Keybase](https://keybase.io/ned84).
