#optical character recognition
import pyautogui
import time 
time.sleep(5)

# pyautogui.click('github_icon.png')
commit= pyautogui.locateCenterOnScreen('commit_icon.png',  confidence=0.9)
print(commit)
# center= pyautogui.center(commit)
# print(center)
# pyautogui.click(center.x,center.y)

# click on the commit button
pyautogui.click(commit)

#locate image
# git_icon = pyautogui.locateCenterOnScreen('github_icon.png', confidence=0.4)
# print(git_icon)

# pyautogui.click(git_icon)
