# main.py
# --
# Python Version: Python 3.11
# Author: Peter M. Robertson
# Date: 2023-01-29
# License: MIT
# --

from helpers import BasicCLI
from rps import Game as RPS
from rpsls import Game as RPSLS


def mainloop():
    cli = BasicCLI()
    game_choices: dict = {"rps": RPS, "rpsls": RPSLS}
    while True:
        print("Exit at any prompt with 'q' or 'quit'")
        game_choice = cli.choice_prompt("Hello, would you like to play Rock Paper Scissors, "
                                        "Rock Paper Scissors Lizard Spock?", ("rps", "rpsls"))

        if game_choice == "quit":
            print("Exiting game... Goodbye!")
            break
        # Maybe a context manager is too much for a goodbye message? :shrug:
        # oh well, I don't really care.
        with game_choices[game_choice]() as g:
            g.play()


if __name__ == '__main__':
    try:
        mainloop()
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt detected. Goodbye!")
