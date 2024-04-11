from src.utils import fancy_print
from characters import Player


def create_character():
    fancy_print("What is your name?")
    name = input("Name: ")
    player = Player(name=name, starting_location="stage 1")

    print(f"\nWelcome {name} \n \n You can take one item on your adventure, choose wisely. \n Your options are: \n    A) Acne Studios Scarf \n    B) Chunk of clay \n    C) Bottle of wine")
    print("I choose: ")
    item = input()

    while item.lower() not in ["a", "b", "c"]:
        print("Please choose one of the items by typing the corresponding letter.")
        print("I choose: ")
        item = input()
    if item.lower() == "a":
        item = "Acne Studios Scarf"
    if item.lower() == "b":
        item = "Chunk of clay"
    if item.lower() == "c":
        item = "Bottle of wine"

    player.add_to_inventory(item=item)

    player.check_inventory()

    return player

