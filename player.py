import pprint
from src.utils import slowPrint

class Player:
    def __init__(self, name, starting_location):
        self.name = name
        self.current_location = starting_location
        self.inventory = []

    def move_to(self, new_location):
        self.current_location = new_location
        print(f"{self.name} has moved to {new_location}.")

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} has been added to your inventory.")

    def check_inventory(self):
        pprint.pprint(f"Your inventory contains: {self.inventory}")


def create_character():
    slowPrint("What is your name?")
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

    return player.name


the_hero = create_character()




