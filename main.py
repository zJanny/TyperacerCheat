from driver_manager import DriverManager
from cheat import Cheat

if __name__ == "__main__":
    driver_manager = DriverManager("https://play.typeracer.com/?universe=lang_de")
    cheat = Cheat(driver_manager, 300, 5)

    driver_manager.connect_to_page()

    cheat.practice()

    driver_manager.close()