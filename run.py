import time
from menu import create_menu
from survey import sci_fi_survey
from data_analysis import data_results
from utils import clear_screen, greetings_msg


def main():
    """Function to display greetings and the main menu"""
    clear_screen()
    greetings_msg()

    options = [
        'About Sci-Fi Survey',
        'Sci-Fi Survey',
        'Data & Results',
        'Exit'
    ]

    menu_entry_index = create_menu("MAIN MENU:\n", options)

    if menu_entry_index == 0:
        print("Made by Valleyberg")
        time.sleep(1)
        main()
    elif menu_entry_index == 1:
        sci_fi_survey()
    elif menu_entry_index == 2:
        data_results()
        # print("Data Results")
    elif menu_entry_index == 3:
        print("""
        Live Long and Prosper!
        """)
        exit()


if __name__ == '__main__':
    main()
