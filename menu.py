from simple_term_menu import TerminalMenu


def create_menu(title, options):
    """Helper function to create and display menu"""
    menu = TerminalMenu(options, title=title)
    choice_index = menu.show()
    return choice_index
