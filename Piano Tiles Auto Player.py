from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# Start the code with delay to set up the game
time.sleep(0.05)

# Function to click at the cordinates
def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# Loop to find the black tile 
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(598, 435) [0] == 0:
        click(598, 435)
    if pyautogui.pixel(697, 435) [0] == 0:
        click(697, 435) 
    if pyautogui.pixel(785, 435) [0] == 0:
        click(785, 435) 
    if pyautogui.pixel(861, 435) [0] == 0:
        click(861, 435) 