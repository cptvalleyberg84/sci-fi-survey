import gspread
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
    data = sheet1.get_all_values()
    print(data)


if __name__ == '__main__':
    main()



