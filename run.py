import gspread
from google.oauth2.service_account import Credentials
from simple_term_menu import TerminalMenu
import datetime

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

# Print All Data from the Google Sheets file
# data = sheet1.get_all_values()
# print(data)

def greetings_msg():
    """Function to display the Survey Greetings"""
    greetings_txt = """
    Greetings to the Sci-Fi Survey!
    """
    print(greetings_txt)

def main():
    """ The Main Menu of the Sci-fi Survey"""
    greetings_msg()
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
        print("Data Results")
    elif menu_entry_index == 2:
        print("Made by Valleyberg")
    elif menu_entry_index == 3:
        print("Live Long and Prosper!")
        exit()

def  sci_fi_survey():
    """ The Sci-Fi Survey Section"""
    # data = sheet1.get_all_values()
    # print(data)

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

    #Question 3:
    yes_no_options = [
        "Yes", 
        "No"
        ]
    
    yes_no_menu = TerminalMenu(yes_no_options, title = "\n3. Do you like speculative fiction?")
    yes_no_choice_index = yes_no_menu.show()
    speculative_ficiton = yes_no_options[yes_no_choice_index]

    #Current TimeStamp
    timestamp =  str(datetime.datetime.now())

    #Prepare the data to be stored
    survey_data = [timestamp, age, sci_fi_type, speculative_ficiton]

    print("\nYour Survey responses:")
    print(f"\nAge: {survey_data[1]}")
    print(f"Preferred Sci-Fi Type: {survey_data[2]}")
    print(f"Like Speculative Fiction: {survey_data[3]}")
    print(f"\n{survey_data[0]}")


    sheet1.append_row(survey_data)
    # store_survey_data(survey_data)
    print("Data Stored.")

# def store_survey_data(survey_data):
#     sheet1.append_row(survey_data)


if __name__ == '__main__':
    main()



