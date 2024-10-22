import time
#import win32api, win32con
import pyautogui

def get_coordinates():
    print(pyautogui.position())


while (True):
  time.sleep(3)
  pyautogui.click(1696, 361)
  #get_coordinates()
  



# def click(x,y):
#     win32api.SetCursorPos((x,y))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
