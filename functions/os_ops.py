import os
import subprocess as sp

paths = {
    'notepad': 'C:\\Program Files\\Notepad++\\notepad++.exe',
    'discord': 'C:\\Users\\Lenovo\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.exe',
    'calculator': 'C:\\Windows\\System32\\calc.exe'
}

# opening of camera


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

# opening of notepad and discord


def open_notepad():
    sp.startfile(paths['notepad'])


def open_discord():
    sp.startfile(paths['discord'])

# opening of cmd


def open_cmd():
    os.system('start cmd')

# opening of calculator


def open_calculator():
    sp.Popen(paths['calculator'])
