
import time
from pynput.mouse import Button
from pynput.mouse import Controller as ControllerM

from pynput.keyboard import Key
from pynput.keyboard import Controller as ControllerK

from pynput import keyboard


mouse = ControllerM()

keyboardP = ControllerK()

f = open('coordinates.txt')
line = f.readlines()
settingsX = line[0]
settingsY = line[1]
movementX = line[2]
movementY = line[3]
keysX = int(line[4])
keysY = int(line[5])
okX = line[6]
okY = line[7]



def hover():
    keyboardP.press(Key.esc)
    keyboardP.release(Key.esc)
    time.sleep(0.1)
    mouse.position = (settingsX, settingsY)
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.position = (movementX, movementY)
    mouse.press(Button.left)
    mouse.release(Button.left)

    time.sleep(0.1)
    mouse.position = (keysX, keysY)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.1)
    keyboardP.press('e')
    keyboardP.release('e')

    time.sleep(0.1)
    mouse.position = (keysX, keysY+50)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.1)
    keyboardP.press('q')
    keyboardP.release('q')

    time.sleep(0.1)
    mouse.position = (keysX, keysY+210)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.1)
    keyboardP.press('w')
    keyboardP.release('w')

    time.sleep(0.1)
    mouse.position = (keysX, keysY+260)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.1)
    keyboardP.press('s')
    keyboardP.release('s')

    time.sleep(0.1)
    mouse.position = (okX, okY)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.3)
    keyboardP.press(Key.esc)
    keyboardP.release(Key.esc)


def milik():
    keyboardP.press(Key.esc)
    keyboardP.release(Key.esc)
    time.sleep(0.1)
    mouse.position = (settingsX, settingsY)
    mouse.press(Button.left)
    mouse.release(Button.left)
    mouse.position = (movementX, movementY)
    mouse.press(Button.left)
    mouse.release(Button.left)

    time.sleep(0.1)
    mouse.position = (keysX, keysY)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.1)
    keyboardP.press('w')
    keyboardP.release('w')

    time.sleep(0.1)
    mouse.position = (keysX, keysY+50)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.1)
    keyboardP.press('s')
    keyboardP.release('s')

    time.sleep(0.1)
    mouse.position = (keysX, keysY+210)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.1)
    keyboardP.press('q')
    keyboardP.release('q')

    time.sleep(0.1)
    mouse.position = (keysX, keysY+260)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.1)
    keyboardP.press('e')
    keyboardP.release('e')

    time.sleep(0.1)
    mouse.position = (okX, okY)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.3)
    keyboardP.press(Key.esc)
    keyboardP.release(Key.esc)


with keyboard.GlobalHotKeys({
        '<shift>+,': hover,
        '<shift>+.': milik}) as h:
    h.join()
