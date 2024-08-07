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

# data = sheet1.get_all_values()

# print(data)



def main():
    options = ['Sci-Fi Survey', 'Data & Results', 'About', 'Exit']
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You've chosen {options[menu_entry_index]}!")

if __name__ == '__main__':
    main()