from driver_manager import DriverManager
from cheat import Cheat

if __name__ == "__main__":
    driver_manager = DriverManager("https://play.typeracer.com/?universe=lang_de", headless=False)
    cheat = Cheat(driver_manager, 500, 0.1)

    driver_manager.connect_to_page()

    cheat.start()

    driver_manager.close()