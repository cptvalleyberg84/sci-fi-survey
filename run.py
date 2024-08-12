import gspread
from google.oauth2.service_account import Credentials
from simple_term_menu import TerminalMenu
import datetime
import os
import platform
import pandas as pd
import time

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
    "Engangement Frequency",
    "Favourite Sci-Fi Medium"
])

# Print All Data from the Google Sheets file
# print(data)

def greetings_msg():
    """Function to display the Survey Greetings"""
    greetings_txt = """
    Greetings to the Sci-Fi Survey!
    """
    print(greetings_txt)

def main():

    clear_screen()

    """ The Main Menu of the Sci-fi Survey"""
    greetings_msg()

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

    options = [
        'Sci-Fi Survey', 
        'Data & Results', 
        'About Sci-FI Survey', 
        'Exit'
        ]
    
    main_menu = TerminalMenu(options)
    
    menu_entry_index = main_menu.show()
    
    # print(f"You've chosen {options[menu_entry_index]}!")

    if menu_entry_index == 0:
        sci_fi_survey()
    elif menu_entry_index == 1:
        data_results()
        # print("Data Results")
    elif menu_entry_index == 2:
        print("Made by Valleyberg")
        # Check attributes of each column in dataframe
        print(df.dtypes)
    elif menu_entry_index == 3:
        print("Live Long and Prosper!")
        exit()

df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df = df.dropna(subset=["Age"])

def  sci_fi_survey():
    """ The Sci-Fi Survey Section"""
    # data = sheet1.get_all_values()
    # print(data)

    clear_screen()
    #Question 1:
    while True:
        try:
            age = int(input("\nHow old are you? \n\n (Enter a number between 0 and 99): "))
            if 0 <= age <= 99:
                break
            else:
                print("\nPlease enter a valid age between 0 and 99.")
        except ValueError:
            print("\nInvalid input. Please enter a number between 0 and 99.")

    clear_screen()

    #Question 2:
    sci_fi_options = [
        "Space Opera", 
        "Cyberpunk", 
        "Time Travel", 
        "Dystopian", 
        "Alien Invasion"
        ]

    sci_fi_menu = TerminalMenu(sci_fi_options, title="\n2. What type of sci-fi do you like most?")
    sci_fi_choice_index = sci_fi_menu.show()
    sci_fi_type = sci_fi_options[sci_fi_choice_index]

    clear_screen()

    #Question 3:
    spec_fi_options = [
        "Yes", 
        "No"
        ]
    
    spec_fi_menu = TerminalMenu(spec_fi_options, title = "\n3. Do you like speculative fiction?")
    spec_fi_choice_index = spec_fi_menu.show()
    speculative_ficiton = spec_fi_options[spec_fi_choice_index]

    clear_screen()

    #Question 4:
    sci_fi_freq_options = [
        "Daily",
        "Weekly",
        "Monthly",
        "All the time!"
        ]

    sci_fi_freq_menu = TerminalMenu(sci_fi_freq_options, title="\n4. How often do you engage with Sci-Fi content?")
    sci_fi_freq_choice_index = sci_fi_freq_menu.show()
    sci_fi_freq = sci_fi_freq_options[sci_fi_freq_choice_index]

    clear_screen()

    #Question 5:
    sci_fi_medium_options = [
        "Books",
        "Movies",
        "TV Shows",
        "Video Games"
    ]

    sci_fi_medium_menu = TerminalMenu(sci_fi_medium_options, title="\n5. When getting into Sci-Fi you prefer to use:")
    sci_fi_medium_choice_index = sci_fi_medium_menu.show()
    sci_fi_medium = sci_fi_medium_options[sci_fi_medium_choice_index]
    
    clear_screen()

    #Current TimeStamp
    timestamp =  str(datetime.datetime.now())

    #Prepare the data to be stored
    survey_data = [timestamp, age, sci_fi_type, speculative_ficiton, sci_fi_freq, sci_fi_medium]

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
#    print(df.head())
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
        "Main Menu"
    ]

    data_results_menu = TerminalMenu(data_results_menu_options, title="\nWhich stats would you wish to reveal?\n")
    data_results_index = data_results_menu.show()

    if data_results_index == 0:
        age_data()
        print("Age Data")
    elif data_results_index == 1:
        print("Sci-Fi Type")
    elif data_results_index == 2:
        print("Speculative Fiction")
    elif data_results_index == 3:
        print("Frequency")
    elif data_results_index == 4:
        print('Medium')
    elif data_results_index == 5:
        print("Stats are awesome! You're now part of the journey! Come again :) ")
        time.sleep(1)
        main()

def age_data():
    mean_age = df["Age"].mean()
    #print(mean_age)
    median_age = df["Age"].median()
    #print(median_age)
    age_distribution = df["Age"].value_counts().sort_index()

    input("\nPress any key to return to the menu")
    data_results()
    
def clear_screen():
    """Clears the terminal screen so it's all nice and neat."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

if __name__ == '__main__':

    main()



