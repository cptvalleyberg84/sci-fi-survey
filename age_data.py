import time
import emoji
import pandas as pd
from google_sheets import df
from tabulate import tabulate
from colorama import Fore, Back, Style
from utils import clear_screen, print_section, go_back_to_results_menu
from menu import create_menu

g = Fore.GREEN
b = Style.BRIGHT
c = Style.RESET_ALL
d = Style.DIM
m = Back.MAGENTA
cy = Fore.CYAN


def age_data():
    """Function to analize and display Age Data"""
    # Basic Age Stats
    mean_age = df["Age"].mean()
    youngest_age = df["Age"].min()
    oldest_age = df["Age"].max()

    print_age_data = {
        "Mean Age": int(mean_age),
        "Youngest Participant": int(youngest_age),
        "Oldest Participant": int(oldest_age)
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
    time.sleep(1)
    # Define Groups
    bins = [7, 18, 30, 45, 60, 100]
    groups = ['7-18', '19-30', '31-45', '46-60', '61+']
    df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=groups, right=False)

    # Age Vs Sci-Fi Type
    print(f'\n{cy}{b}Favorite Sci-Fi Type by Age Group:{c}\U0001F938')

    # Group by Age Group and Sci-Fi Type
    age_grouped = df.groupby(
        ["Age Group", 'Sci-Fi Type'], observed=False
    ).size().unstack().fillna(0)

    for age_group in groups:
        if age_group in age_grouped.index:
            most_popular_genre = age_grouped.loc[age_group].idxmax()
            most_pupular_count = age_grouped.loc[age_group].max()
            total_in_group = age_grouped.loc[age_group].sum()
            percentage = (most_pupular_count / total_in_group) * 100

            print(
                f"\nFor the {Fore.GREEN}{age_group}{Style.RESET_ALL} "
                f"age group,"
                f"'{Fore.GREEN}{most_popular_genre}{Style.RESET_ALL}' "
                f" is the most popular genre"
                f" \nwith {Fore.GREEN}{most_pupular_count}{Style.RESET_ALL}"
                f" votes,"
                f" making up {Fore.GREEN}{percentage:.2f}%{Style.RESET_ALL}"
                f" of their choices.\n"
            )
        else:
            print(f"""
        \U000026A0 No data available for the {age_group} age group.
            """)
    time.sleep(1)
    # Age Vs Speculative Fiction
    print(
        f'\n{cy}{b}Speculative Fiction Popularity by Age Group:{c}\U0001F52E'
    )
    s_fic_grpd = df.groupby(
        ['Age Group', 'Likes Spec-Fi'], observed=False
    ).size().unstack().fillna(0)
    print(tabulate(s_fic_grpd, headers='keys', tablefmt='fancy_grid'))

    for age_group in groups:
        if age_group in s_fic_grpd.index:
            likes_count = s_fic_grpd.loc[age_group, 'Yes']
            total_in_group = s_fic_grpd.loc[age_group].sum()
            percentage = (likes_count / total_in_group) * 100

            print(
                f'\nIn the {g}{age_group}{c} age group,'
                f' {g}{likes_count}{c} participants ({g}{percentage:.2f}%{c})'
                f' enjoy speculative fiction.\n'
            )
        else:
            print(f"""
        \U000026A0 No data available for the {age_group} age group.
            """)
    time.sleep(1)
    # Age Vs Enagagement Frequency
    print(f'\n{cy}{b}Engagement Frequency by Age Group{c} \U0001F4DA\n')
    eng_grpd = df.groupby(
        ["Age Group", 'Engagement Frequency'], observed=False
    ).size().unstack().fillna(0)
    print(tabulate(eng_grpd, headers='keys', tablefmt='fancy_grid'))

    for age_group in groups:
        if age_group in eng_grpd.index:
            most_ef = eng_grpd.loc[age_group].idxmax()
            freq_count = eng_grpd.loc[age_group].max()
            total_in_group = eng_grpd.loc[age_group].sum()
            percentage = (freq_count / total_in_group) * 100

            print(
                f'\nFor the {g}{b}{age_group}{c} age group'
                f' the most common engagement '
                f'frequency is {g}{b}{most_ef}{c}'
                f' \nchosen by {g}{freq_count}{c} participants'
                f' {g}{percentage:.2f}%{c}\n'
            )
        else:
            print(f"""
        \U000026A0 No data available for the {age_group} age group.
            """)
    time.sleep(1)
    # Age Vs Medium Preference
    print(f'\n{cy}{b}Favorite Sci-Fi Medium by Age Group:{c} \U0001F4FA\n')
    medium_grpd = df.groupby(
        ["Age Group", "Fav Sci-Fi Medium"], observed=False
    ).size().unstack().fillna(0)
    print(tabulate(medium_grpd, headers='keys', tablefmt='fancy_grid'))

    for age_group in groups:
        if age_group in medium_grpd.index:
            most_medium = medium_grpd.loc[age_group].idxmax()
            medium_count = medium_grpd.loc[age_group].max()
            total_in_group = medium_grpd.loc[age_group].sum()
            percentage = (medium_count / total_in_group) * 100

            print(

                f"\nFor the {g}{b}{age_group}{c} age group"
                f' the most common engagement frequency '
                f'is {g}{b}{most_medium}{c}'
                f' \nchosen by {g}{medium_count}{c} participants'
                f' {g}{percentage:.2f}%{c}\n'
            )
        else:
            print(f"""
        \U000026A0 No data available for the {age_group} age group.
            """)
    time.sleep(1)
    # Summary Small and Info to Scroll Up
    print(f"""{b+g}
    It appears that different age groups
    gravitate toward different sci-fi genres {c}\U0001F913

    {g}You can scroll up to view the full data.{c}""")

    # Pause to allow the user to see the results
    go_back_to_results_menu()
