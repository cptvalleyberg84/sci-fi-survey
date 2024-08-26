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

def speculative_fiction_data():
    """Function to analyze and display Speculative Fiction Data"""
    speculative_fiction_counts = df["Likes Spec-Fi"].value_counts()

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

    """Analize/display how engagement frequency 
    correlates with liking speculative fiction"""
    engagement_vs_sf = pd.crosstab(
        df['Engagement Frequency'], df['Likes Spec-Fi'])

    print('\nEngagement Frequency vs Liking Speculative Fiction:')
    print(tabulate(engagement_vs_sf, headers='keys', tablefmt='fancy_grid'))


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