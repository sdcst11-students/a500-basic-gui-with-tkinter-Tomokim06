import pyautogui
count = 0
while count < 50:
    x, y = pyautogui.position()
    px = pyautogui.pixel(x, y)
    print(px)
    count = count+1
