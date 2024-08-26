import time
import datetime
from google_sheets import sheet1
from colorama import Fore, Back, Style
from menu import create_menu
from utils import clear_screen, print_section

r = Back.RED
k = Fore.BLACK
b = Style.BRIGHT
c = Style.RESET_ALL


def sci_fi_survey():
    """ The Sci-Fi Survey Section"""

    clear_screen()

    # Question 1:
    while True:
        age_input = input(
            "\nHow old are you? \n\n (Enter a number between 7 and 99): ")
        try:
            if '.' in age_input:
                print(
                    f"{b+r}Please enter a whole number"
                    f" without any decimals.{c}"
                )
                continue
            age = int(age_input)

            if 7 <= age <= 99:
                break
            else:
                print(f"{r+b}\nPlease enter a valid age between 7 and 99.{c}")
        except ValueError:
            print(
                f"{r+b}\nInvalid input: "
                f"Please enter number between 7 and 99.{c}"
            )

    clear_screen()

    # Question 2:
    sci_fi_options = [
        "Space Opera",
        "Cyberpunk",
        "Time Travel",
        "Dystopian",
        "Alien Invasion"
    ]

    sci_fi_choice_index = create_menu(
        "\n2. What type of sci-fi do you like most?", sci_fi_options)
    sci_fi_type = sci_fi_options[sci_fi_choice_index]

    clear_screen()

    # Question 3:
    spec_fi_options = [
        "Yes",
        "No"
    ]

    spec_fi_choice_index = create_menu(
        "\n3. Do you like speculative fiction?", spec_fi_options
    )
    speculative_fiction = spec_fi_options[spec_fi_choice_index]

    clear_screen()

    # Question 4:
    sci_fi_freq_options = [
        "Daily",
        "Weekly",
        "Monthly",
        "All the time!"
    ]

    sci_fi_freq_choice_index = create_menu(
        "\n4. How often do you engage with Sci-Fi content?",
        sci_fi_freq_options
    )
    sci_fi_freq = sci_fi_freq_options[sci_fi_freq_choice_index]

    clear_screen()

    # Question 5:
    sci_fi_medium_options = [
        "Books",
        "Movies",
        "TV Shows",
        "Video Games"
    ]

    sci_fi_medium_choice_index = create_menu(
        "\n5. When getting into Sci-Fi you prefer to use:",
        sci_fi_medium_options
    )
    sci_fi_medium = sci_fi_medium_options[sci_fi_medium_choice_index]

    clear_screen()

    # Question 6:
    books_question_options = [
        "Paperbooks",
        "Audiobooks",
        "E-books",
        "I don't read books!"
    ]

    books_question_choice_index = create_menu(
        "\n6. Which type of books do you like the most?",
        books_question_options
    )
    book_question = books_question_options[books_question_choice_index]

    clear_screen()

    # Current TimeStamp
    timestamp = str(datetime.datetime.now())

    # Prepare the data to be stored
    survey_data = [
        timestamp,
        age,
        sci_fi_type,
        speculative_fiction,
        sci_fi_freq,
        sci_fi_medium,
        book_question
    ]

    clear_screen()

    print_survey_data = {
        "Age": survey_data[1],
        "Preferred Sci-Fi Type": survey_data[2],
        "Like Speculative Fiction": survey_data[3],
        "Engagement Frequency": survey_data[4],
        "Favourite Sci-Fi Medium": survey_data[5],
        "Favourite type of Book": survey_data[6],
        "Additional Comments": survey_data[0]
    }

    print_section("Your Survey reponses", print_survey_data)

    sheet1.append_row(survey_data)
    print("\nData Stored.")
    time.sleep(1)
    from run import main
    main()
