"""

Cotação automatica do Bitcoin com pyautogui

"""
import pyautogui

pyautogui.moveTo(x=233, y=1056)
pyautogui.sleep(1)

pyautogui.click(x=233, y=1056)
pyautogui.sleep(2)

pyautogui.typewrite('Google Chrome')
pyautogui.sleep(2)

pyautogui.press('enter')
pyautogui.sleep(3)

pyautogui.typewrite('Bitcoin')
pyautogui.sleep(2)

pyautogui.press('enter')

# print(pyautogui.position())
