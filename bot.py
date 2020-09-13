from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *


class Bot:
    dinosaur = (0, 0)
    running = False

def pressSpace():
    pyautogui.keyDown("space")
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp("space")

def imageGrab():
    box = (Bot.dinosaur[0] + 15, Bot.dinosaur[1] + 15, Bot.dinosaur[0] + 57,
           Bot.dinosaur[1] + 32)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())

def stopBot():
    Bot.running = False

def runBot():
    if Bot.dinosaur == (0, 0):
        return False
    pressSpace()
    Bot.running = True

    print(Bot.dinosaur)
    while Bot.running:
        screen = str(imageGrab())
        if screen != 961:
            pressSpace()
            time.sleep(0.1)

