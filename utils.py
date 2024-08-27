import os
import platform
from colorama import Fore, Back, Style


def clear_screen():
    """Clears the terminal screen so it's all nice and neat."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def go_back_to_results_menu():
    """Function to go back to Results Menu"""
    input("\nPress the ENTER key to return to the menu...")
    from data_analysis import data_results
    data_results()


def print_section(title, data):
    """ Prints a section with a title and key-value pairs."""
    print(f"\n{title}:\n")
    for label, value in data.items():
        print(f"{label}: {value}")


def greetings_msg():
    """Function to display the Survey Greetings"""
    greetings_txt = """
    Greetings to the Sci-Fi Survey!"""
    print(greetings_txt)
    print(Fore.MAGENTA, Style.BRIGHT + r"""
  _________      .__         __________.__
 /   _____/ ____ |__|        \_   _____|__|
 \_____  \_/ ___\|  |  ______ |    __) |  |
 /        \  \___|  | /_____/ |     \  |  |
/_______  /\___  |__|         \___  /  |__|
   _____\/_ ___\/_______  __ ____ \/_.__.
  /  ___|  |  \_  __ \  \/ _/ __ <   |  |
  \___ \|  |  /|  | \/\   /\  ___/\___  |
 /____  |____/ |__|    \_/  \___  / ____|
      \/                        \/\/
""" + Style.RESET_ALL)
