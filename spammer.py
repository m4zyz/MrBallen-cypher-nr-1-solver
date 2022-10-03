import pyautogui, time
time.sleep(8)
text = open("spam text")
for each_line in text:
    pyautogui.typewrite(each_line)
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')


