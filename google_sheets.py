import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

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
    "Likes Spec-Fi",
    "Engagement Frequency",
    "Fav Sci-Fi Medium",
    "Favourite Book Type"
])

# Convert Age data to numbers
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df = df.dropna(subset=["Age"])