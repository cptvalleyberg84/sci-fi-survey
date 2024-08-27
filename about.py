import time
from colorama import Fore, Back, Style
from utils import clear_screen, go_back_to_results_menu


def about():
    """Function to display the about me section"""
    clear_screen()
    print(Fore.MAGENTA, Style.BRIGHT + """

The Sci-Fi Survey is a Python based application designed to gather
and analyze preferences related to science fiction. This tool allows users
to participate in a survey that captures various aspects of their interest in
sci-fi, including favorite genres, engagement frequency, and preferred mediums.

Instructions:
1. Take the survey.
2. be sure to check the data results.

Please be advised:

Sometimes it is possible to scroll up to see more info.
Follow the instructions on the screen.


    """ + Style.RESET_ALL)
    time.sleep(2)
    input("\nPress the ENTER key to return to the menu...")
    clear_screen()
    print("Made by Valleyberg")
    time.sleep(1)
    from run import main
    main()
