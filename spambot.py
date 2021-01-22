import pyautogui
import time


spam_text = input("text: ")
times = int(input("How many times: "))
time.sleep(10)
for _ in range (times):
	pyautogui.typewrite(spam_text)
	pyautogui.press('enter')
	time.sleep(1)
