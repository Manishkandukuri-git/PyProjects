# import pywhatkit
# for _ in range(10):
#     pywhatkit.sendwhatmsg("+1XXXXXXXXXX","What's going on with you",2,17)
import pyautogui

import time
time.sleep(2)

count=0

while count<=50:
    pyautogui.typewrite("What's going on with you??")
    pyautogui.press("enter")
    count=count+1