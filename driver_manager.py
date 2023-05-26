from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class DriverManager():
    def __init__(self, url) -> None:
        self.url = url
        options = webdriver.FirefoxOptions()
        options.headless = True
        self.driver = webdriver.Firefox(options=options)
    
    def connect_to_page(self):
        print("Connecting to " + self.url)
        self.driver.get(self.url)

    def open_practice(self):
        print("Searching for pratice button")
        button = self.driver.execute_script('return document.getElementsByClassName("gwt-Anchor prompt-button bkgnd-blue")')
        if len(button) > 0 and button != None:
            print("Found button")
            button[0].click()
        else:
            print("Could not find button")
            self.close()

    def get_text_and_focus_input_box(self):
        text_elements = self.driver.execute_script('return document.querySelectorAll("[unselectable=\'on\']")')
        final_text = ""
        for text in text_elements:
            final_text += text.get_attribute('innerHTML')
        print("Found text:")
        print(final_text)
        print("Searching for input box")
        input_box = self.driver.execute_script("return document.getElementsByClassName('txtInput')")
        input_box[0].click()
        print("Clicked input box")

        return final_text

    def close(self):
        print("Closing driver")
        self.driver.close()

    def write_char(self, char):
        ActionChains(self.driver).send_keys(char).perform()