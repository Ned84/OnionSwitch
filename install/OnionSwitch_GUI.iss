w#define MyAppVersion "1.0"
#define MyName "Baumgartner Rene Mario"

[Setup]
//SignedUninstaller=yes
//SignTool=Certum
SetupIconFile=Icon\onionswitch_icon.ico
AppName=OnionSwitch_GUI
AppVersion={#MyAppVersion}
AppVerName=OnionSwitch_GUI {#MyAppVersion}
AppCopyright={#MyName}
WizardStyle=modern
WizardImageFile=Icon\OnionSwitch_Logo.bmp
WizardImageStretch=no
OutputBaseFilename=OnionSwitch_GUI{#MyAppVersion}_setup
DefaultDirName={autopf}\OnionSwitch_GUI
DefaultGroupName=OnionSwitch_GUI
UninstallDisplayIcon="{commondocs}GitHub\Publish\OnionSwitch\Icon\onionswitch_icon.ico"
UninstallDisplayName=OnionSwitch_GUI
Compression=lzma2
SolidCompression=yes

[Files]
Source: "OnionSwitch_V1.0_GUI\*"; DestDir: "{app}"
//Source: "{commondocs}GitHub\Publish\OnionSwitch\OnionSwitch_V1.0_GUI\OnionSwitch_GUI.py.exe"; DestDir: "{app}"; Flags: sign


[Icons]
Name: "{group}\OnionSwitch_GUI"; Filename: "{app}\OnionSwitch_GUI.py.exe"; IconFilename: "C:\Users\baumg\Documents\GitHub\Publish\OnionSwitch\Icon\onionswitch_icon.ico"; IconIndex: 0
Name: "{commondesktop}\OnionSwitch_GUI"; Filename: "{app}\OnionSwitch_GUI.py.exe"; IconFilename: "C:\Users\baumg\Documents\GitHub\Publish\OnionSwitch\Icon\onionswitch_icon.ico"; IconIndex: 0
Name: "{commonstartup}\OnionSwitch_GUI"; Filename: "{app}\OnionSwitch_GUI.py.exe"; IconFilename: "C:\Users\baumg\Documents\GitHub\Publish\OnionSwitch\Icon\onionswitch_icon.ico"; IconIndex: 0