import PySimpleGUI as gui
from pynput import mouse
from bot import *

def setUpDinosaur():
    def on_click(x, y, button, pressed):
        Bot.dinosaur = (x,y)
        if not pressed:
            return False
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

def runGUI():
    layout = [[gui.Button('Run'), gui.Button('Stop')],
              [gui.Text('Bot Setup'), gui.Button('Dinosaur Location')]]

    win = gui.Window('Window 1', layout)
    win.keep_on_top = True
    while True:
        event, values = win.read()
        if event == gui.WIN_CLOSED:
            break
        if event == 'Stop':
            stopBot()
            print('Bot Stopped')
        if event == 'Run':
            if not runBot():
                gui.Popup('Error: Please Setup Points!')
            else:
                print('Bot Started')
                runBot()

        if event == 'Dinosaur Location':
            gui.Popup('Left click on dinosaurs location during game to calibrate. Press OK to start')
            setUpDinosaur()
            gui.Popup('Calibrated!')
            print('getting dinosaur location')




runGUI()