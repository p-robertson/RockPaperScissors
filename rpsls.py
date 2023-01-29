# rpsls.py
# --
# Python Version: Python 3.11
# Author: Peter M. Robertson
# Date: 2023-01-29
# License: MIT
# --

import random
from helpers import BasicCLI


class Game:
    """
    A class representing a game of Rock, Paper, Scissors, Lizard, Spock.
    """

    def __init__(self):
        """
        Initialize the game with necessary attributes such as the choices for the game,
        the rules for winning and losing, and the states for the game.
        """
        self.cli = BasicCLI()
        self.choices: dict = {0: "rock", 1: "paper", 2: "scissors", 3: "lizard", 4: "spock"}
        self.rules: dict = {0: (2, 3), 1: (0, 4), 2: (1, 3), 3: (1, 4), 4: (0, 2)}
        self.states: dict = {0: "draw", 1: "win", 2: "lose"}
        self.exit_msg: str = "Exiting Rock Paper Scissors Lizard Spock...\n"

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        print(self.exit_msg)

    def play(self):
        """
        Play the game and prompt the user for their choice, generate a random choice for the computer,
        compare the choices and declare the winner, and prompt the user to play again if desired.
        """
        print("\nNew Game Started!")
        player_choice = self.cli.choice_prompt("Rock, Paper, Scissors, Lizard, Spock?",
                                               tuple(self.choices.values()))
        if player_choice == "quit":
            return

        computer_choice = random.choice(tuple(self.choices.keys()))
        for i, choice in self.choices.items():
            if player_choice == choice:
                player_choice = i
                break
        print(f"Player chooses {self.choices[player_choice]}, "
              f"Computer chooses {self.choices[computer_choice]}")
        if player_choice == computer_choice:
            state = self.states[0]
        elif computer_choice in self.rules[player_choice]:
            state = self.states[1]
        else:
            state = self.states[2]

        print(f"You {state.upper()}!")
        # play again?
        if self.cli.choice_prompt("Would you like to play again?", ("y", "n")) == "y":
            self.play()


if __name__ == '__main__':
    game = Game()
    game.play()
