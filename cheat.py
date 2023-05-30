from driver_manager import DriverManager
from progress.bar import IncrementalBar
from progress.spinner import Spinner
from time import sleep
import random
import time
import math
import os

class Cheat():
    def __init__(self, driver_manager: DriverManager, cpm: int, error_percentage: int) -> None:
        self.driver = driver_manager
        self.cpm = cpm
        self.error_percentage = error_percentage

    def add_errors(self, text):
        print("Adding errors")
        random.seed(time.time() * 1000)
        new_text = []
        
        for char in text:
            if math.floor( random.uniform(0, 1/(1-self.error_percentage))):
                new_text.append("a")
                new_text.append("\b")
            
            new_text.append(char)

        print("Added " + str(len(new_text) - len(text)) + " errors")
        return new_text
    
    def start(self):
        sleep(2)
        self.driver.open_race()

        sleep(1)
        self.driver.check_for_popup()
        text = self.driver.get_text_and_focus_input_box()
        text = self.add_errors(text)
        spinner = Spinner("Waiting for race to start ")

        while not self.driver.has_race_started():
            sleep(0.15)
            spinner.next()
        sleep(0.25)
        os.system("clear")
        print("Race has started")
        self.driver.get_enemies()
        bar = IncrementalBar('Typing', max=len(text), suffix='%(percent).1f%% - %(eta)ds')
        for char in text:   
            self.driver.write_char(char)
            bar.next()
            sleep((60 / self.cpm))
        print("\nFinished typing")
        sleep(2)
        self.driver.get_stats()
        self.driver.get_game_status()

        again = input("Start new race? y/n \n")

        if again == "y":
            self.start()
