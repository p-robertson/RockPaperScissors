# rps.py
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
    A class representing a game of Rock, Paper, Scissors.
    """
    def __init__(self):
        """
        Initialize the game class with a basic CLI, the choices for rock-paper-scissors, the rules for winning,
        and the states for the game outcome.
        """
        self.cli = BasicCLI()
        self.choices: dict = {0: "rock", 1: "paper", 2: "scissors"}
        self.rules: tuple = (0, 2), (1, 0), (2, 1)
        self.states: dict = {0: "draw", 1: "win", 2: "lose"}
        self.exit_msg: str = "Exiting Rock Paper Scissors...\n"

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        print(self.exit_msg)

    def play(self):
        """
        Play a round of rock-paper-scissors, where the user selects a choice and the computer randomly selects a choice.
        Compare the choices to determine the outcome of the game, and display the result to the user.
        Ask the user if they want to play again, and repeat the game if they select yes.
        """
        print("\nNew Game Started!")
        player_choice = self.cli.choice_prompt("Rock, Paper, or Scissors?", tuple(self.choices.values()))
        if player_choice == "quit":
            return

        computer_choice = random.choice((0, 1, 2))
        for i, choice in self.choices.items():
            if player_choice == choice:
                player_choice = i
                break

        print(f"Player chooses {self.choices[player_choice]}, Computer chooses {self.choices[computer_choice]}")
        comparison = player_choice, computer_choice
        if player_choice == computer_choice:
            state = self.states[0]
        elif comparison in self.rules:
            state = self.states[1]
        else:
            state = self.states[2]

        print(f"You {state.upper()}!")
        if self.cli.choice_prompt("Would you like to play again?", ("y", "n")) == "y":
            self.play()


if __name__ == '__main__':
    game = Game()
    game.play()
