#open githubdesktop
#select right repo
#search for unsaved files
#enter a summary and description
#Click on commit button
#click on push origin button

import os
import time
import pyautogui
import pytesseract
import logging

def open_github_desktop():
    os.system('open -a "GitHub Desktop"')
    time.sleep(5)



def find_and_click_text(target_text, double_click=False):
    try:
        # Take a screenshot
        screenshot = pyautogui.screenshot()
        screenshot = screenshot.convert('RGB')

        # Debugging - Save screenshot
        screenshot.save(os.path.join(os.getcwd(), 'debug_screenshot.png'))

        # Extract text data
        data = pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)

        logging.info(f"OCR Data: {data}")
        print(f"OCR Data: {data}")

        # Iterate over detected words
        for i, word in enumerate(data['text']):
            if word.strip().lower() == target_text.strip().lower():
                x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
                center_x, center_y = x + w // 2, y + h // 2

                logging.info(f"Found '{target_text}' at ({center_x}, {center_y})")

                # Click or double-click
                if double_click:
                    pyautogui.doubleClick(center_x, center_y)
                    logging.info(f"Double-clicked on '{target_text}'.")
                else:
                    pyautogui.click(center_x, center_y)
                    logging.info(f"Clicked on '{target_text}'.")

                return True

        logging.warning(f"'{target_text}' not found.")
        return False

    except Exception as e:
        logging.error(f"Error: {e}")
        return False


def select_repo(repo_name):
    time.sleep(5)
    #maximize screen
    #v=pyautogui.hotkey('command','control','F')
    #print(v)
    
    #icon_location = pyautogui.locateOnScreen('maxi_icon.png')
    #icon_center = pyautogui.center(icon_location)
    #print(icon_center)
    #pyautogui.click('maxi_icon.png')

    #pyautogui.click('calc7key.png')

    time.sleep(2)
    #find_and_click_text("Current")     
    pyautogui.click(100, 80)
    pyautogui.write(repo_name)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(100, 730)
    pyautogui.write("hi")
    pyautogui.click(100, 895)
    #click the push origin button
    #click the commit button
    pyautogui.click(1080, 307)

print("about to open git_hub_desktop")

open_github_desktop()
print("selecting repo")

select_repo("feb25-automation-class")
