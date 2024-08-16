from google_sheets import df
from utils import clear_screen, print_section, go_back_to_results_menu
from menu import create_menu
import pandas as pd
import time

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
        from main import main
        main()


def age_data():
    """Function to analize and display Age Data"""
    mean_age = df["Age"].mean()
    youngest_age = df["Age"].min()
    oldest_age = df["Age"].max()

    print_age_data = {
        "Mean Age": int(mean_age),
        "Youngest Participant:": youngest_age,
        "Oldest Participant:": oldest_age
    }
    print_section("Age Data Analysis", print_age_data)

    print("\nAnalysis Insight:")
    if youngest_age < 18:
        print(f"""
        Young guns on board! 
        Our youngest participant is just {int(youngest_age)} years old.
        On average, participants are {int(mean_age)} years old
        """)
    if oldest_age > 60:
        print(f"""
        The oldest participant is {int(oldest_age)} years old, proving 
        that sci-fi is timeless and spans across generations!\n
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
    The most popular Sci-Fi type is {most_popular_sf}. 
    Leading the charge with {sci_fi_counts[most_popular_sf]} responses. 
    ({(sci_fi_counts[most_popular_sf] / total_responses_sf_td) * 100:.2f}%)
    """)

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
    \nSpeculative Fiction is a Hit! 
    ({yes_sf_percentage:.2f}%) likes speculative fiction! <3 <3 <3
""")
    else:
        print(f"""
    \nSurprisingly, ({no_sf_percentage:.2f}%) don't like speculative fiction. 
    :( </3)""")

    go_back_to_results_menu()


def engagement_frequency_data():
    """Function to analize and display Engagement Frequency Data"""
    engagement_frequency_counts = df["Engagement Frequency"].value_counts()
    total_responses_ef = engagement_frequency_counts.sum()
    most_common_ef = engagement_frequency_counts.idxmax()

    print("Engangement Frequency:\n")
    for sci_fi_freq, count in engagement_frequency_counts.items():
        percentage_ef = (count / total_responses_ef) * 100
        print(f"{sci_fi_freq}: {count} ({percentage_ef:.2f}%)")


    print(f"""
It seems that the most common engagement frequency is '{most_common_ef}'.
This captures imagination of {engagement_frequency_counts[most_common_ef]}.
({(engagement_frequency_counts[most_common_ef] / total_responses_ef)*100:.2f}%).
    """)

    go_back_to_results_menu()

def sci_fi_medium_data():
    """Function to analize and display Favourite Sci-Fi Medium Data"""
    sci_fi_medium_counts = df["Favourite Sci-Fi Medium"].value_counts()
    total_responses_medium = sci_fi_medium_counts.sum()
    top_medium = sci_fi_medium_counts.idxmax()

    for sci_fi_medium, count in sci_fi_medium_counts.items():
        percentage_medium = (count / total_responses_medium) * 100
        print(f"{sci_fi_medium}: {count} ({percentage_medium:.2f}%)")

    print(f'''The preferred medium for sci-fi adventures is "{top_medium}"!
    With {sci_fi_medium_counts[top_medium]} votes. 
    ({(sci_fi_medium_counts[top_medium] / total_responses_medium) * 100:.2f}%)
    ''')

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
            print("""
        It seems that those who frequently engage with sci-fi are
        more likely to enjoy speculative fiction - no surprise here! 
        
        Deeper engagement often means love for all things speculative!
        """)
        else:
            print("""
        Interestingly, frequent engagement with sci-fi does not
        necessarily correlate with a liking for speculative fiction.
            """)
    else:
        print("Data is cloudy. Get back later to see if this changed.")

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

    print("\nFavorite Sci-Fi Type by Age Group:\n")
    print(age_grouped)

    for age_group in groups:
        if age_group in age_grouped.index:
            most_popular_genre = age_grouped.loc[age_group].idxmax()
            most_pupular_count = age_grouped.loc[age_group].max()
            total_in_group = age_grouped.loc[age_group].sum()
            percentage = (most_pupular_count / total_in_group) * 100

            print(f"""
For the {age_group} age group, '{most_popular_genre}' is the most popular genre,
with {most_pupular_count} votes, making up {percentage:.2f}% of their choices.
            """)
        else:
            print(f"""
            No data available for the {age_group} age group.
            """)

    print("""
    It appears that different age groups 
    gravitate toward different sci-fi genres.""")

    go_back_to_results_menu()