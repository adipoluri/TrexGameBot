from PIL import ImageGrab, ImageOps
import pyautogui
import keyboard
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
    box = (Bot.dinosaur[0] + 15, Bot.dinosaur[1], Bot.dinosaur[0] + 57,
           Bot.dinosaur[1] + 15)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()

screen = imageGrab()

def stopBot():
    Bot.running = False

def runBot():
    if Bot.dinosaur == (0, 0):
        return False
    pressSpace()
    Bot.running = True
    print(Bot.dinosaur)
    while Bot.running:
        if screen != 877:
            pressSpace()
            time.sleep(0.1)
        if keyboard.is_pressed('esc'):
            break