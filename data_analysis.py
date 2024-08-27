import time
import emoji
import pandas as pd
from google_sheets import df
from tabulate import tabulate
from colorama import Fore, Back, Style
from age_data import age_data
from speculative_fiction_data import speculative_fiction_data
from utils import clear_screen, print_section, go_back_to_results_menu
from menu import create_menu

g = Fore.GREEN
b = Style.BRIGHT
c = Style.RESET_ALL
d = Style.DIM
m = Back.MAGENTA


def data_results():
    """Display the Data Results Menu"""

    clear_screen()

    data_greet_txt = """
    Let's analize our Sci-Fi data! :thumbs_up: \U0001f600
    """
    print(emoji.emojize(data_greet_txt))

    data_results_menu_options = [
        "1. Sci-Fi-Fans Age",
        "2. Fav Sci-Fi Type",
        "3. How many like Speculative Fiction",
        "4. Sci-Fi Frequention",
        "5. Sci-Fi Medium Style",
        "6. Favourite Book Type",
        "Main Menu"
    ]

    data_results_index = create_menu(
        "\nWhich stats would you wish to reveal?\n",
        data_results_menu_options)

    if data_results_index == 0:
        age_data()
    elif data_results_index == 1:
        sci_fi_type_data()
    elif data_results_index == 2:
        speculative_fiction_data()
    elif data_results_index == 3:
        engagement_frequency_data()
    elif data_results_index == 4:
        sci_fi_medium_data()
    elif data_results_index == 5:
        favourite_book_type()
    elif data_results_index == 6:
        print(
            f"Stats are awesome! You're now part of the journey!"
            f" Come again \U0001F604")
        time.sleep(1)
        from run import main
        main()


def sci_fi_type_data():
    """Function to analyze and display Sci-Fi Type Data"""
    sci_fi_counts = df["Sci-Fi Type"].value_counts()
    total_responses_sf_td = sci_fi_counts.sum()

    print("Sci-Fi Type Preferences:\n")
    for sci_fi_type, count in sci_fi_counts.items():
        percentage_sf_td = (count / total_responses_sf_td) * 100
        print(f"{sci_fi_type}: {count} ({percentage_sf_td:.2f}%)")

    most_popular_sf = sci_fi_counts.idxmax()

    print(f"""
        The most popular Sci-Fi type is {g}{most_popular_sf}{c} \U0001F680
        Leading the charge with {g}{b}{
            sci_fi_counts[most_popular_sf]
            } responses{c}.
        {g}{(
            sci_fi_counts[most_popular_sf] / total_responses_sf_td
            ) * 100:.2f}%{c}
    """)

    go_back_to_results_menu()


def engagement_frequency_data():
    """Function to analize and display Engagement Frequency Data"""
    engagement_frequency_counts = df["Engagement Frequency"].value_counts()
    total_responses_ef = engagement_frequency_counts.sum()
    common_ef = engagement_frequency_counts.idxmax()

    print("Engagement Frequency:\n")
    for sci_fi_freq, count in engagement_frequency_counts.items():
        percentage_ef = (count / total_responses_ef) * 100
        print(f"{sci_fi_freq}: {count} ({percentage_ef:.2f}%)")

    print(f"""
        \n\tIt seems that the most common engagement
        frequency is {g+b}{common_ef}{c}.\n
        This captures imagination of
        {g}{engagement_frequency_counts[common_ef]}{b}
        \n\tThat's {(
            engagement_frequency_counts[common_ef] / total_responses_ef
        ) * 100:.2f} % !!{c}
        \n\t  \U0001F44D \U0001FAF5
    """)

    go_back_to_results_menu()


def sci_fi_medium_data():
    """Function to analize and display Favorite Sci-Fi Medium Data"""
    sci_fi_medium_counts = df["Fav Sci-Fi Medium"].value_counts()
    total_responses_medium = sci_fi_medium_counts.sum()
    top_medium = sci_fi_medium_counts.idxmax()

    for sci_fi_medium, count in sci_fi_medium_counts.items():
        percentage_medium = (count / total_responses_medium) * 100
        print(f"{sci_fi_medium}: {count} ({percentage_medium:.2f}%)")

    print(f'''
        \n\tThe preferred medium for sci-fi adventures are:
        \n\t{g + b}{top_medium}{c}!
        \n\tWith {g + b}{sci_fi_medium_counts[top_medium]} votes{c}.
        \U0001F4DA {g + b}
        \n\t{(
            sci_fi_medium_counts[top_medium] / total_responses_medium
        ) * 100:.2f} % !{c}
    ''')

    go_back_to_results_menu()


def favourite_book_type():
    """Analize and display fav book type data"""
    fav_book_type_counts = df['Favourite Book Type'].value_counts()
    total_res_books = fav_book_type_counts.sum()
    type_book = fav_book_type_counts.idxmax()

    print("Most Liked Book Type Style:\n")
    for book_question, count in fav_book_type_counts.items():
        percentage_books = (count / total_res_books) * 100
        print(f"{book_question}: {count} ({percentage_books:.2f}%)")

    print(
        f'\nThe preferred book type is "{Fore.GREEN}{type_book}"'
        f'{Style.RESET_ALL}! '
        f'With {Fore.GREEN}{fav_book_type_counts[type_book]}'
        f' votes !! \U0001F4D6 '
        f'({(fav_book_type_counts[type_book] / total_res_books)* 100:.2f}%)'
        f'{Style.RESET_ALL}')

    go_back_to_results_menu()
