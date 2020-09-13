from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *


class Coordinates:
    replayBtn = (0, 0)
    dinosaur = (0, 0)


def restartGame():
    pyautogui.click(Coordinates.replayBtn)


def pressSpace():
    pyautogui.keyDown("space")
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp("space")


def imageGrab():
    box = (Coordinates.dinosaur[0] + 15, Coordinates.dinosaur[1] + 15, Coordinates.dinosaur[0] + 57,
           Coordinates.dinosaur[1] + 32)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())


gay = str(imageGrab())


def main():
    restartGame()
    while True:
        if gay != 961:
            pressSpace()
            time.sleep(0.1)
