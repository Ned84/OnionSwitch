# OnionSwitch

[![GitHub license](https://img.shields.io/github/license/Ned84/BreaktimeWatch?color=blue&style=plastic)](https://github.com/Ned84/OnionSwitch/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/Ned84/BreaktimeWatch?style=plastic)](https://github.com/Ned84/OnionSwitch/issues)
[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2F%2FNed84%2FOnionSwitch%2Fbadge&style=plastic)](https://actions-badge.atrox.dev//Ned84/OnionSwitch/goto)
[![CircleCI](https://circleci.com/gh/Ned84/OnionSwitch.svg?style=svg)](https://circleci.com/gh/Ned84/OnionSwitch)

* [Description](#description)
  * [StrictNodes](#strictnodes)
* [Dependencies](#dependencies)
* [License](#license)
* [Install](#install)
  * [Build executable from .py](#build-executable-from-py)
* [Support](#support)
* [Get my Public Key](#get-my-public-key)


## Description

Interface to easily switch the Tor-Exit-Node Destination Country in your Tor-Browser.
It is possible to force exit nodes to a specific country, exlude exit node countries and/or exclude countries for every Relay not only the exit relay.

### StrictNodes

If StrictNodes is set to 1, Tor will treat the ExcludeNodes option as a requirement to follow for all the circuits you generate, even if doing so will break functionality for you. If StrictNodes is set to 0, Tor will still try to avoid nodes in the ExcludeNodes list, but it will err on the side of avoiding unexpected errors. Specifically, StrictNodes 0 tells Tor that it is okay to use an excluded node when it is necessary to perform relay reachability self-tests, connect to a hidden service, provide a hidden service to a client, fulfill a .exit request, upload directory information, or download directory information.

Please refer to the Tor manual [here](https://2019.www.torproject.org/docs/tor-manual.html.en) for more information.

## Dependencies

Newest Python from [here](https://www.python.org/downloads/).

```pip install PyQt5```

PYQT5 information at [this link](https://pypi.org/project/PyQt5/).

```pip install Stem```

Stem information are [here](https://stem.torproject.org/).

```pip install pyinstaller```

Optional Pyinstaller. Infos are [here](https://www.pyinstaller.org/downloads.html).

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

### Build executable from .py

```pip install pyinstaller```

```pip install PyQt5```

```pip install Stem```

```pyinstaller --windowed --icon=Icon/onionswitch_icon.ico --clean --name OnionSwitch.py OnionSwitch_GUI.py```

## Support

If you require help or if you have suggestions please refer to the [Issue section](https://github.com/Ned84/OnionSwitch/issues).

## Get my Public Key

Get my public key at [Keybase](https://keybase.io/ned84).
