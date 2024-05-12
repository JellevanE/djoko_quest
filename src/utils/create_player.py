from src.utils.utils import fancy_print
from src.characters import Player


def create_player():
    fancy_print("What is your name?")
    name = input("Name: ")
    player = Player(name=name, starting_location="stage 1")
    print()
    fancy_print(f"Welcome {name}, this is how your adventure begins...")
    return player