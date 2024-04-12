from characters import Player, NPC
from items import Item
from src.utils import fancy_print
from scenes_text.island_campfire import opening_wake_up, ascii_island
from test import wizard
from create_player import create_player


def enter_stage_one(player:Player):
    #write opening scene
    fancy_print(ascii_island, speed=0.01, color="YELLOW")
    fancy_print(opening_wake_up)
    player_options(player=player, locations=["fortress", "docks"], interactions=wizard, objects=[])



def player_options(player:Player, locations:list, interactions:list[NPC], objects:list[Item]):
    fancy_print("What do you do?")
    fancy_print("""
          a: move
          b: interact
          c: inspect
          d: inventory
          """)
    print("I choose: ")
    action = input()

    while action.lower() not in ["a", "b", "c", "d"]:
        fancy_print("Please choose one of the options by typing the corresponding letter.")
        print("I choose: ")
        action = input()

    if action.lower() == "a": #move action
        action = "perform move"

    if action.lower() == "b": #interact action
        action = "perform interact"

    if action.lower() == "c": #inspect action
        action = "inspect object"

    if action.lower() == "d": #inventory action
        inventory_action(player=player)
        
        
        
def inventory_action(player:Player):
    player.check_inventory()
    fancy_print("What do you do?")
    fancy_print("""
          a: use
          b: inspect
          c: back
          """)
    print("I choose: ")
    inventory_action = input()
    
    while inventory_action.lower() not in ["a", "b", "c"]:
        fancy_print("Please choose one of the options by typing the corresponding letter.")
        print("I choose: ")
        inventory_action = input()
    if inventory_action.lower() == "a":
        player_use_item(player=player, use=True, inspect=False)
    if inventory_action.lower() == "b":
        player_use_item(player=player, use=False, inspect=True)
    if inventory_action.lower() == "c":
        return False#return to loop??
    

def player_use_item(player:Player, use:bool, inspect:bool):
    items = player.inventory

    for i, item in enumerate(items, start=1):
        fancy_print(f"{i}: {item}")

    # Ask the user to choose a number
    selected_number = int(input("Enter the number of the item you want to use: "))

        # Adjust for zero-based index
    selected_index = selected_number - 1

    # Validating if the input is within the available item range
    if 0 <= selected_index < len(items):
        selected_item = items[selected_index]
        if use == True:
            selected_item.use
        if inspect == True:
            selected_item.inspect
    else:
        fancy_print("Invalid number, please enter a number from the list.")
        player_use_item(player=player, use=use, inspect=inspect)
