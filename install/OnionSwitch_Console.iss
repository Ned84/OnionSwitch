#define MyAppVersion "1.0"
#define MyName "Baumgartner Rene Mario"

[Setup]
//SignedUninstaller=yes
//SignTool=Certum
SetupIconFile=Icon\onionswitch_icon.ico
AppName=OnionSwitch_Console
AppVersion={#MyAppVersion}
AppVerName=OnionSwitch_Console {#MyAppVersion}
AppCopyright={#MyName}
WizardStyle=modern
WizardImageFile=Icon\OnionSwitch_Logo.bmp
WizardImageStretch=no
OutputBaseFilename=OnionSwitch_Console{#MyAppVersion}_setup
DefaultDirName={autopf}\OnionSwitch_Console
DefaultGroupName=OnionSwitch_Console
UninstallDisplayIcon="{commondocs}GitHub\Publish\OnionSwitch\Icon\onionswitch_icon.ico"
UninstallDisplayName=OnionSwitch_Console
Compression=lzma2
SolidCompression=yes

[Files]
Source: "OnionSwitch_V1.0_Console\*"; DestDir: "{app}"
//Source: "{commondocs}GitHub\Publish\OnionSwitch\OnionSwitch_V1.0_Console\OnionSwitch_Console.py.exe"; DestDir: "{app}"; Flags: sign


[Icons]
Name: "{group}\OnionSwitch_Console"; Filename: "{app}\OnionSwitch_Console.py.exe"; IconFilename: "C:\Users\baumg\Documents\GitHub\Publish\OnionSwitch\Icon\onionswitch_icon.ico"; IconIndex: 0
Name: "{commondesktop}\OnionSwitch_Console"; Filename: "{app}\OnionSwitch_Console.py.exe"; IconFilename: "C:\Users\baumg\Documents\GitHub\Publish\OnionSwitch\Icon\onionswitch_icon.ico"; IconIndex: 0
Name: "{commonstartup}\OnionSwitch_Console"; Filename: "{app}\OnionSwitch_Console.py.exe"; IconFilename: "C:\Users\baumg\Documents\GitHub\Publish\OnionSwitch\Icon\onionswitch_icon.ico"; IconIndex: 0


