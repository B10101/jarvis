import os
import subprocess as sp

paths = {
    'visual studio code': 'C:\\Users\\bettc\\AppData\\Local\Programs\\Microsoft VS Code\\code.exe',
    'Unreal engine':'C:\\Program Files\\Epic Games\\UE_5.0EA\\Engine\\Binaries\\Win64\\UnrealEditor.exe',
    'chrome': 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    'visual studio 2019': 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe'

}


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_chrome():
    os.startfile(paths['chrome'])


def open_cmd():
    os.system('start cmd')


def open_visualstudiocode():
    os.startfile(paths['visual studio code'])


def open_visualstudio2019():
    os.startfile(paths['visual studio 2019'])


def open_UnrealEngine():
    os.startfile(paths['Unreal engine'])
