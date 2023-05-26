from driver_manager import DriverManager
from time import sleep

class Cheat():
    def __init__(self, driver_manager: DriverManager, cpm: int, error_percentage: int) -> None:
        self.driver = driver_manager
        self.cpm = cpm
        self.error_percentage = error_percentage

    def practice(self):
        sleep(1)
        self.driver.open_practice()

        sleep(1)
        text = self.driver.get_text_and_focus_input_box()

        sleep(2.5)
        for char in text:   
            self.driver.write_char(char)
            sleep(0.25)
