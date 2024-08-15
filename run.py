import gspread
import time
import datetime
import os
import platform
import pandas as pd
from google.oauth2.service_account import Credentials
from simple_term_menu import TerminalMenu

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('sci-fi-data')

sheet1 = SHEET.worksheet('Sheet1')

# Fetch all data from the Google Sheets from Sheet1
data = sheet1.get_all_values()

# Convert the data into a Pandas DataFrame
df = pd.DataFrame(data, columns=[
    "Timestamp",
    "Age",
    "Sci-Fi Type",
    "Likes Speculative Fiction",
    "Engagement Frequency",
    "Favourite Sci-Fi Medium"
])

# Print All Data from the Google Sheets file
# print(data)


# Convert Age data to numbers
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df = df.dropna(subset=["Age"])


def clear_screen():
    """Clears the terminal screen so it's all nice and neat."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def greetings_msg():
    """Function to display the Survey Greetings"""
    greetings_txt = """
    Greetings to the Sci-Fi Survey!
    """
    print(greetings_txt)
    print(r"""
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
""")


def create_menu(title, options):
    """Helper function to create and display menu"""
    menu = TerminalMenu(options, title=title)
    choice_index = menu.show()
    return choice_index


def sci_fi_survey():
    """ The Sci-Fi Survey Section"""
    # data = sheet1.get_all_values()
    # print(data)

    clear_screen()
    # Question 1:
    while True:
        try:
            age = int(
input("\nHow old are you? \n\n (Enter a number between 7 and 99): "))
            if 7 <= age <= 99:
                break
            else:
                print("\nPlease enter a valid age between 7 and 99.")
        except ValueError:
            print("\nInvalid input. Please enter a number between 7 and 99.")

    clear_screen()

    # Question 2:
    sci_fi_options = [
        "Space Opera",
        "Cyberpunk",
        "Time Travel",
        "Dystopian",
        "Alien Invasion"
        ]

    sci_fi_menu = TerminalMenu(
sci_fi_options, title="\n2. What type of sci-fi do you like most?")
    sci_fi_choice_index = sci_fi_menu.show()
    sci_fi_type = sci_fi_options[sci_fi_choice_index]

    clear_screen()

    # Question 3:
    spec_fi_options = [
        "Yes",
        "No"
        ]

    spec_fi_menu = TerminalMenu(
spec_fi_options, title="\n3. Do you like speculative fiction?")
    spec_fi_choice_index = spec_fi_menu.show()
    speculative_fiction = spec_fi_options[spec_fi_choice_index]

    clear_screen()

    # Question 4:
    sci_fi_freq_options = [
        "Daily",
        "Weekly",
        "Monthly",
        "All the time!"
        ]

    sci_fi_freq_menu = TerminalMenu(
sci_fi_freq_options, title="\n4. How often do you engage with Sci-Fi content?")
    sci_fi_freq_choice_index = sci_fi_freq_menu.show()
    sci_fi_freq = sci_fi_freq_options[sci_fi_freq_choice_index]

    clear_screen()

    # Question 5:
    sci_fi_medium_options = [
        "Books",
        "Movies",
        "TV Shows",
        "Video Games"
    ]

    sci_fi_medium_menu = TerminalMenu(
sci_fi_medium_options, title="\n5. When getting into Sci-Fi you prefer to use:")
    sci_fi_medium_choice_index = sci_fi_medium_menu.show()
    sci_fi_medium = sci_fi_medium_options[sci_fi_medium_choice_index]

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
        sci_fi_medium
        ]

    clear_screen()

    print("\nYour Survey responses:")
    print(f"\nAge: {survey_data[1]}")
    print(f"Preferred Sci-Fi Type: {survey_data[2]}")
    print(f"Like Speculative Fiction: {survey_data[3]}")
    print(f"Engangement Frequency: {survey_data[4]}")
    print(f"Favourite Sci-Fi Medium: {survey_data[5]}")
    print(f"\n{survey_data[0]}")

    sheet1.append_row(survey_data)
    # store_survey_data(survey_data)
    print("Data Stored.")
    time.sleep(1)
    main()

# def store_survey_data(survey_data):
#     sheet1.append_row(survey_data)


def data_results():
    """Display the Data Results Menu"""
    # print(df.head())
    clear_screen()

    data_greet_txt = """
    Let's analize our Sci-Fi data!
    """
    print(data_greet_txt)

    data_results_menu_options = [
        "Sci-Fi-Fans Age",
        "Fav Sci-Fi Type",
        "How many like Speculative Fiction",
        "Sci-Fi Frequention",
        "Sci-Fi Medium Style",
        "Engagement vs Speculative Fiction",
        "Favourite Sci-Fi by Age Group",
        "Main Menu"    
    ]

#     data_results_menu = TerminalMenu(
# data_results_menu_options, title="\nWhich stats would you wish to reveal?\n")
#     data_results_index = data_results_menu.show()

    data_results_index = create_menu(
        "\nWhich stats would you wish to reveal?\n", 
        data_results_menu_options)

    if data_results_index == 0:
        age_data()
        print("Age Data")
    elif data_results_index == 1:
        sci_fi_type_data()
        print("Sci-Fi Type")
    elif data_results_index == 2:
        speculative_fiction_data()
        print("Speculative Fiction")
    elif data_results_index == 3:
        engagement_frequency_data()
        print("Frequency")
    elif data_results_index == 4:
        sci_fi_medium_data()
        print('Medium')
    elif data_results_index == 5:
        engagement_vs_speculative_fiction()
    elif data_results_index == 6:
        favourite_sci_fi_by_age_group()
    elif data_results_index == 7:
        print(
"Stats are awesome! You're now part of the journey! Come again :)")
        time.sleep(1)
        main()


def age_data():
    """Function to analize and display Age Data"""
    mean_age = df["Age"].mean()
    youngest_age = df["Age"].min()
    oldest_age = df["Age"].max()

    # Display calculated values
    print("Age Data Analysis:\n")
    print(f"Mean Age: {mean_age:.2f}")
    print(f"Youngest Participant: {youngest_age}")
    print(f"Oldest Participant: {oldest_age}")

    # Pause to allow the user to see the results
    go_back_to_results_menu()
    

def sci_fi_type_data():
    """Function to analyze and display Sci-Fi Type Data"""
    sci_fi_counts = df["Sci-Fi Type"].value_counts()

    print("Sci-Fi Type Preferences:\n")
    for sci_fi_type, count in sci_fi_counts.items():
        print(f"{sci_fi_type}: {count}")

    go_back_to_results_menu()


def speculative_fiction_data():
    """Function to analyze and display Speculative Fiction Data"""
    speculative_fiction_counts = df["Likes Speculative Fiction"].value_counts()

    print("Likes Speculative Fiction:\n")
    for speculative_fiction, count in speculative_fiction_counts.items():
        print(f"{speculative_fiction}: {count}")

    # Add additional percentage to liking or disliking speculative fiction
    total_responses_sf  = speculative_fiction_counts.sum()

    yes_sf_count = speculative_fiction_counts.get("Yes", 0)
    no_sf_count = speculative_fiction_counts.get("No", 0)

    # Calculate %%% of yes and no answers
    yes_sf_percentage = (yes_sf_count / total_responses_sf) * 100
    no_sf_percentage = (no_sf_count / total_responses_sf) * 100

    # Determine Majority
    if yes_sf_count > no_sf_count:
        print(
f"\nMajority ({yes_sf_percentage:.2f}%) likes speculative fiction! <3 <3 <3"
)
    else:
        print(
f"\nMajority ({no_sf_percentage:.2f}%) don't like speculative fiction. :( </3)")

    go_back_to_results_menu()


def engagement_frequency_data():
    """Function to analize and display Engagement Frequency Data"""
    engagement_frequency_counts = df["Engagement Frequency"].value_counts()

    print("Engangement Frequency:\n")
    for sci_fi_freq, count in engagement_frequency_counts.items():
        print(f"{sci_fi_freq}: {count}")

    go_back_to_results_menu()

def sci_fi_medium_data():
    """Function to analize and display Favourite Sci-Fi Medium Data"""
    sci_fi_medium_counts = df["Favourite Sci-Fi Medium"].value_counts()

    for sci_fi_medium, count in sci_fi_medium_counts.items():
        print(f"{sci_fi_medium}: {count}")

    go_back_to_results_menu()


def engagement_vs_speculative_fiction():
    """Analize/display how engagement frequency 
    correlates with liking speculative fiction"""
    engagement_vs_sf = pd.crosstab(
        df['Engagement Frequency'], df['Likes Speculative Fiction'])

    print('\nEngagement Frequency vs Liking Speculative Fiction:\n')
    print(engagement_vs_sf)

    go_back_to_results_menu()

def favourite_sci_fi_by_age_group():
    """Function to analize and display Favourite Sci-Fi type by Age Group"""
    #Define Groups
    bins = [7, 18, 30, 45, 60, 100]
    groups = ['7-18','19-30','31-45','46-60','61+']
    df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=groups, right=False)

    # Group by Age Group and Sci-Fi Type
    age_grouped = df.groupby(["Age Group", 'Sci-Fi Type']).size().unstack().fillna(0)

    print("\nFavorite Sci-Fi Type by Age Group:\n")
    print(age_grouped)

    go_back_to_results_menu()


def go_back_to_results_menu():
    """Function to go back to Results Menu"""
    input("\nPress the ENTER key to return to the menu...")
    data_results()


def main():
    """Function to display greetings and the main menu"""
    clear_screen()
    greetings_msg()

    options = [
        'About Sci-FI Survey',
        'Sci-Fi Survey',
        'Data & Results',
        'Exit'
        ]

    # main_menu = TerminalMenu(options)
    # menu_entry_index = main_menu.show()

    menu_entry_index = create_menu("\nMAIN MENU:\n", options)

# EXAMPLE
        # data_results_index = create_menu(
        # "\nWhich stats would you wish to reveal?\n", 
        # data_results_menu_options)

        #     data_results_menu = TerminalMenu(data_results_menu_options, title="\nWhich stats would you wish to reveal?\n")
#     data_results_index = data_results_menu.show()

    # print(f"You've chosen {options[menu_entry_index]}!")

    if menu_entry_index == 0:
        print("Made by Valleyberg")
        # Check attributes of each column in dataframe
        # print(df.dtypes)
        time.sleep(1)
        main()
    elif menu_entry_index == 1:
        sci_fi_survey()
    elif menu_entry_index == 2:
        data_results()
        # print("Data Results")
    elif menu_entry_index == 3:
        print("Live Long and Prosper!")
        exit()


if __name__ == '__main__':
    main()
