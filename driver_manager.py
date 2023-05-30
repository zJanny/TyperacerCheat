from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
from exceptions import ButtonNotFoundException
from exceptions import StatsNotFoundException

class DriverManager():
    def __init__(self, url, headless: False) -> None:
        self.url = url
        options = webdriver.FirefoxOptions()
        options.headless = headless
        self.driver = webdriver.Firefox(options=options)
    
    def connect_to_page(self):
        print("Connecting to " + self.url)
        self.driver.get(self.url)

    def find_button(self, button_class):
        button = self.driver.execute_script('return document.getElementsByClassName("' + button_class + '")')
        if len(button) > 0 and button != None:
            print("Found button")
            button[0].click()
        else:
            raise ButtonNotFoundException
        
    def get_enemies(self):
        enemies = self.driver.execute_script('return document.getElementsByClassName("lblName")')

        print("\nEnemies: \033[92m")
        for i in range(1, len(enemies)):
            print(enemies[i].get_attribute('innerHTML'))
            
        print("\033[0m")
        
    def open_race(self):
        print("Searching for race button")

        try:
            self.find_button("gwt-Anchor prompt-button bkgnd-green")
        except ButtonNotFoundException:
            print("Could not find race button, trying to find race again button")
            self.find_button("xButton")
            self.find_button("raceAgainLink")

    

    def open_practice(self):
        print("Searching for pratice button")

        self.find_button("gwt-Anchor prompt-button bkgnd-blue")

    def get_stats(self):
        os.system("clear")
        print("Searching for stats")

        stats = self.driver.execute_script('return document.getElementsByClassName("tblOwnStats")')
        if len(stats) == 0:
            raise StatsNotFoundException
        html = stats[0].get_attribute('innerHTML')

        soup = BeautifulSoup(html, "html.parser")
        all_divs = soup.find_all("div")

        speed = all_divs[1].text
        time = all_divs[2].text.strip()
        accuracy = all_divs[3].text
        points = all_divs[5].text

        print("\nStats: \nCPM: \033[92m" + speed + "\n\033[0mTime: \033[92m" + time + " min\n\033[0mAccuracy: \033[92m" + accuracy + "\n\033[0mPoints: \033[92m" + points + "\n\033[0m")

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
        if char == "\b":
            ActionChains(self.driver).key_down(Keys.BACKSPACE).perform()
            sleep(0.1)
            ActionChains(self.driver).key_up(Keys.BACKSPACE).perform()
            return
        ActionChains(self.driver).send_keys(char).perform()

    def has_race_started(self):
        light_label = self.driver.execute_script("return document.getElementsByClassName('lightLabel')")

        if len(light_label) == 0:
            return True
        
        return False