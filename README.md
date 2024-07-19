# Piano Tiles Auto Player

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact](#contact)

## Introduction

The **Piano Tiles Auto Player** is a Python script designed to automatically play the game [Magic Piano Tiles](https://www.agame.com/game/magic-piano-tiles). The script uses `pyautogui` to detect and click the black tiles, enabling high scores without manual effort.

## Features

- Automatically detects and clicks black tiles on the screen.
- Simple and easy-to-use script.
- Adjustable delay for different game speeds.

## Requirements

- Python 3.8
- `pyautogui` library
- `keyboard` library
- `pywin32` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/alphaXcosmo/Piano-Tiles-Auto-Player.git
    ```

2. Navigate to the project directory:
    ```sh
    cd Piano-Tiles-Auto-Player
    ```

3. Install the required libraries:
    ```sh
    pip install pywin32
    pip install keyboard
    pip install pyautogui
    pip install opencv-python
    ```

## Usage

1. Open the game [Magic Piano Tiles](https://www.agame.com/game/magic-piano-tiles) in your web browser.
2. Run the Python script:
    ```sh
    python Piano-Tiles-Auto-Player.py
    ```
3. Quickly switch to the game window.
4. The script will start detecting and clicking the black tiles.
5. Press `q` to stop the script.

## Script Details

Here's the Python code for the script:

```python
from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con

# Start the code with delay to set up the game
time.sleep(0.05)

# Function to click at the coordinates
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# Loop to find the black tile
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(598, 435)[0] == 0:
        click(598, 435)
    if pyautogui.pixel(697, 435)[0] == 0:
        click(697, 435)
    if pyautogui.pixel(785, 435)[0] == 0:
        click(785, 435)
    if pyautogui.pixel(861, 435)[0] == 0:
        click(861, 435)
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit them (git commit -m 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Open a Pull Request.

## Contact

If you have any questions or suggestions, feel free to contact me at sreenath.veepattu@gmail.com.
