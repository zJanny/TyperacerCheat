from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Firefox()
driver.get("https://play.typeracer.com/?universe=lang_de")

def writeText(driver, text):
    for char in text:
        ActionChains(driver).send_keys(char).perform()
        sleep(0.25)
sleep(3)
print("getting button...")
button = driver.execute_script('return document.getElementsByClassName("gwt-Anchor prompt-button bkgnd-blue")')
if len(button) > 0 and button != None:
    print("Found button")
    button[0].click()
    sleep(2)
    text_elements = driver.execute_script('return document.querySelectorAll("[unselectable=\'on\']")')
    final_text = ""
    for text in text_elements:
        final_text += text.get_attribute('innerHTML')
    print("Found text:")
    print(final_text)
    sleep(2)
    input_box = driver.execute_script("return document.getElementsByClassName('txtInput')")
    input_box[0].click()
    writeText(driver, final_text)
else:
    print("Could not find button")

driver.close()