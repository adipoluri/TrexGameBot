import PySimpleGUI as gui
from bot import *


def runGUI():
    gui.theme('DarkAmber')
    layout = [[gui.Text('Setup Bot'), gui.Button('Setup')],
              [gui.Button('Run'), gui.Button('Stop')]]

    window = gui.Window('Trex Bot', layout)
    while True:
        event, values = window.read()
        if event == 'Stop':
            stopBot()
            print('Bot Stopped')
        if event == 'Setup Bot':
            print('Bot Started')
            startBot()


    window.close()

