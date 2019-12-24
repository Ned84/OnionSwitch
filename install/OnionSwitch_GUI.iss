#define MyAppVersion "1.0"
#define MyName "Baumgartner Rene Mario"

[Setup]
SignedUninstaller=yes
SignTool=Certum
SetupIconFile=Icon\onionswitch_icon.ico
AppName=OnionSwitch
AppVersion={#MyAppVersion}
AppVerName=OnionSwitch {#MyAppVersion}
AppCopyright={#MyName}
WizardStyle=modern
WizardImageFile=Icon\OnionSwitch_Logo.bmp
WizardImageStretch=no
OutputBaseFilename=OnionSwitch{#MyAppVersion}_setup
DefaultDirName={autopf}\OnionSwitch
DefaultGroupName=OnionSwitch
UninstallDisplayIcon="C:\Users\baumg\Documents\GitHub\Ned84\OnionSwitch\install\Icon\onionswitch_icon.ico"
UninstallDisplayName=OnionSwitch
OutputDir="C:\Users\baumg\Documents\GitHub\Ned84\OnionSwitch\install\Output\GUI_V1.0"
Compression=lzma2
SolidCompression=yes

[Files]
Source: "GUI\OnionSwitch_V{#MyAppVersion}_GUI\OnionSwitch.py\*"; DestDir: "{app}"; Flags: recursesubdirs
Source: "GUI\OnionSwitch_V{#MyAppVersion}_GUI\OnionSwitch.py\OnionSwitch.py.exe"; DestDir: "{app}"; Flags: sign


[Icons]
Name: "{group}\OnionSwitch"; Filename: "{app}\OnionSwitch.py.exe"; IconFilename: "C:\Users\baumg\Documents\GitHub\Ned84\OnionSwitch\install\Icon\onionswitch_icon.ico"; IconIndex: 0
Name: "{commondesktop}\OnionSwitch"; Filename: "{app}\OnionSwitch.py.exe"; IconFilename: "C:\Users\baumg\Documents\GitHub\Ned84\OnionSwitch\install\Icon\onionswitch_icon.ico"; IconIndex: 0
Name: "{commonstartup}\OnionSwitch"; Filename: "{app}\OnionSwitch.py.exe"; IconFilename: "C:\Users\baumg\Documents\GitHub\Ned84\OnionSwitch\install\Icon\onionswitch_icon.ico"; IconIndex: 0