import pyautogui
import random
import time
import keyboard

def move_and_click():
    # Get the screen size
    screen_width, screen_height = pyautogui.size()

    # Generate random coordinates within the screen boundaries
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)

    # Move the mouse to the random coordinates
    pyautogui.moveTo(x, y, duration=0.5)

    # # Perform a left mouse click
    # pyautogui.click()

    # Press the Escape button
    keyboard.press_and_release('esc')

start_time = time.time()  # Start time

while True:
    move_and_click()
    elapsed_time = time.time() - start_time  # Calculate elapsed time
    print("Total elapsed time:", round(elapsed_time))
    time.sleep(20)

# python -m PyInstaller --onefile ./move.py
