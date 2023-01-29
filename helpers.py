# helpers.py
# --
# Python Version: Python 3.11
# Author: Peter M. Robertson
# Date: 2023-01-29
# License: MIT
# --

class BasicCLI:
    def __init__(self):
        """
        Initializes the CLI object with default comparison values for yes, no, and quit.
        """
        self.yes: tuple = "y", "yes"
        self.no: tuple = "n", "no"
        self.quit: tuple = "q", "quit", "exit"

    def choice_prompt(self, msg: str, choices: tuple | list) -> str:
        """
        Prompts the user to make a choice from a given set of choices.

        Parameters:
        - msg (str): the message to be displayed to the user
        - choices (tuple or list): the set of valid choices for the user

        Returns:
        - str: the user's choice
        """
        choice: str = input(f"{msg} {choices}: ").lower()
        if choice in choices:
            return choice
        elif choice in self.quit:
            return "quit"
        print(f"Invalid input.  Please select from the available choices: {choices}")
        return self.choice_prompt(msg, choices)
