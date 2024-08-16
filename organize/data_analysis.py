from google_sheets import df
from utils import clear_screen, print_section, go_back_to_results_menu
from menu import create_menu
from tabulate import tabulate
from colorama import Fore, Back, Style
import pandas as pd
import time
import emoji

g = Fore.GREEN 
b = Style.BRIGHT
c = Style.RESET_ALL
d = Style.DIM
m = Back.MAGENTA

def data_results():
    """Display the Data Results Menu"""
    # print(df.head())
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
        "7. Engagement vs Speculative Fiction",
        "8. Favourite Sci-Fi by Age Group",
        "9. MEGA RESULTS",
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
        engagement_vs_speculative_fiction()
    elif data_results_index == 7:
        favourite_sci_fi_by_age_group()
    elif data_results_index == 8:
        mega_results()
    elif data_results_index == 9:
        print(
"Stats are awesome! You're now part of the journey! Come again \U0001F604")
        time.sleep(1)
        from main import main
        main()


def age_data():
    """Function to analize and display Age Data"""
    mean_age = df["Age"].mean()
    youngest_age = df["Age"].min()
    oldest_age = df["Age"].max()

    print_age_data = {
        "Mean Age": int(mean_age),
        "Youngest Participant:": int(youngest_age),
        "Oldest Participant:": int(oldest_age)
    }
    print_section("Age Data Analysis", print_age_data)

    print("\nAnalysis Insight:")
    if youngest_age < 18:
        print(f"""
        Young guns on board! \U0001F978
        
        Our youngest participant is just {g}{b}{int(youngest_age)} years old{c}.
        On average, participants are {g}{b}{int(mean_age)} years old{c}.
        """)
    if oldest_age > 60:
        print(f"""
        The oldest participant is {g}{b}{int(oldest_age)} years old{c}, proving 
        that {g}sci-fi is timeless{c} and spans across generations!\U0001F920
        """)

    # Pause to allow the user to see the results
    go_back_to_results_menu()
    

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
    Leading the charge with {g}{b}{sci_fi_counts[most_popular_sf]} responses{c}. 
    {g}{(sci_fi_counts[most_popular_sf] / total_responses_sf_td) * 100:.2f}%
    {c}""")

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
        print(f"""
    {m}{b}Speculative Fiction is a Hit!{c} 
    {g}{yes_sf_percentage:.2f}% likes speculative fiction!{c} \U0001F304
    \U0001F496 \U0001F496 \U0001F496 	
    """)
    else:
        print(f"""{g}{d}
    Surprisingly, ({no_sf_percentage:.2f}%) don't like speculative fiction.{c} 
    \U0001F62D \U0001F494""")

    go_back_to_results_menu()


def engagement_frequency_data():
    """Function to analize and display Engagement Frequency Data"""
    engagement_frequency_counts = df["Engagement Frequency"].value_counts()
    total_responses_ef = engagement_frequency_counts.sum()
    common_ef = engagement_frequency_counts.idxmax()

    print("Engangement Frequency:\n")
    for sci_fi_freq, count in engagement_frequency_counts.items():
        percentage_ef = (count / total_responses_ef) * 100
        print(f"{sci_fi_freq}: {count} ({percentage_ef:.2f}%)")


    print(
        f'\nIt seems that the most common engagement' 
        f'frequency is {g+b}{common_ef}{c}.\n'
        f'This captures imagination of' 
        f" {g}{engagement_frequency_counts[common_ef]}{b}\nThat's "
f'{(engagement_frequency_counts[common_ef] / total_responses_ef)*100:.2f}%!!{c}'
f'  \n  \U0001F44D \U0001FAF5'
    )

    go_back_to_results_menu()

def sci_fi_medium_data():
    """Function to analize and display Favourite Sci-Fi Medium Data"""
    sci_fi_medium_counts = df["Favourite Sci-Fi Medium"].value_counts()
    total_responses_medium = sci_fi_medium_counts.sum()
    top_medium = sci_fi_medium_counts.idxmax()

    for sci_fi_medium, count in sci_fi_medium_counts.items():
        percentage_medium = (count / total_responses_medium) * 100
        print(f"{sci_fi_medium}: {count} ({percentage_medium:.2f}%)")

    print(f'''
    \tThe preferred medium for sci-fi adventures is {g+b}{top_medium}{c}!
    \tWith {g+b}{sci_fi_medium_counts[top_medium]} votes{c}. \U0001F4DA {g+b}
    \t{(sci_fi_medium_counts[top_medium] / total_responses_medium) * 100:.2f}%!
    {c}''')

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
f'\nThe preferred book type is "{Fore.GREEN}{type_book}"{Style.RESET_ALL}! '
f'With {Fore.GREEN}{fav_book_type_counts[type_book]} votes !! \U0001F4D6 '
f'({(fav_book_type_counts[type_book] / total_res_books)* 100:.2f}%)'
f'{Style.RESET_ALL}')

    go_back_to_results_menu()


def engagement_vs_speculative_fiction():
    """Analize/display how engagement frequency 
    correlates with liking speculative fiction"""
    engagement_vs_sf = pd.crosstab(
        df['Engagement Frequency'], df['Likes Speculative Fiction'])

    print('\nEngagement Frequency vs Liking Speculative Fiction:\n')
    print(engagement_vs_sf)

    if engagement_vs_sf.shape[1] == 2:
        if engagement_vs_sf["Yes"].sum() > engagement_vs_sf["No"].sum():
            print(f"""
        It seems that those who frequently engage with sci-fi are
        more likely to enjoy speculative fiction - no surprise here! 
        {Fore.GREEN+b}
        Deeper engagement often means love for all things speculative!
        {Style.RESET_ALL}    \U0001F93C
        """)
        else:
            print(f"""{g+d}
        Interestingly, frequent engagement with sci-fi does not
        necessarily correlate with a liking for speculative fiction.
            {c}""")
    else:
        print(f"{g+d}Data is cloudy. Get back later to see if this changed.{c}")

    go_back_to_results_menu()

def favourite_sci_fi_by_age_group():
    """Function to analize and display Favourite Sci-Fi type by Age Group"""
    #Define Groups
    bins = [7, 18, 30, 45, 60, 100]
    groups = ['7-18','19-30','31-45','46-60','61+']
    df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=groups, right=False)

    # Group by Age Group and Sci-Fi Type
    age_grouped = df.groupby(
        ["Age Group", 'Sci-Fi Type'], observed=False).size().unstack().fillna(0)

    print("\nFavorite Sci-Fi Type by Age Group: \U0001F938\n")
    # print(age_grouped)
    print(tabulate(age_grouped, headers='keys', tablefmt='fancy_grid'))

    for age_group in groups:
        if age_group in age_grouped.index:
            most_popular_genre = age_grouped.loc[age_group].idxmax()
            most_pupular_count = age_grouped.loc[age_group].max()
            total_in_group = age_grouped.loc[age_group].sum()
            percentage = (most_pupular_count / total_in_group) * 100
    
            print(
f"For the {Fore.GREEN}{age_group}{Style.RESET_ALL} age group," 
f"'{Fore.GREEN}{most_popular_genre}{Style.RESET_ALL}' is the most popular genre"
f" \nwith {Fore.GREEN}{most_pupular_count}{Style.RESET_ALL} votes," 
f" making up {Fore.GREEN}{percentage:.2f}%{Style.RESET_ALL} of their choices.\n"
            )
        else:
            print(f"""
        \U000026A0 No data available for the {age_group} age group.
            """)

    print(f"""{b+g}
    It appears that different age groups 
    gravitate toward different sci-fi genres {c}\U0001F913

    {g}You can scroll up to view the full data.{c}""")

    go_back_to_results_menu()


# def mega_results():
