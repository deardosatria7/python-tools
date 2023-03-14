"""
install pyautogui first to use this code
run pip install pyautogui
or python -m pip install pyautogui

"""

import pyautogui
import time

# cooldown for the code to run after (x) seconds initial start
time.sleep(5)

# loop to pressing key (x) times
for i in range (36):
    pyautogui.keyDown("p")
    pyautogui.keyUp("p")
    # pause for (x) seconds to next press
    time.sleep(800)