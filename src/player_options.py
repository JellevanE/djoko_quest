from characters import Player, NPC
from items import Item
from utils.utils import fancy_print

def player_options(player:Player, locations:list, interactions:list[NPC], objects:list[Item]):
    """Access default action options for a player in a certain location"""
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

    if action.lower() == "a": #move action FIX THIS
        action = "perform move"

    if action.lower() == "b": #interact action FIX THIS
        action = "perform interact"

    if action.lower() == "c": #inspect action FIX THIS
        action = "inspect object"

    if action.lower() == "d": #inventory action
        inventory_action(player=player)
        
        
        
def inventory_action(player:Player):
    """default action to access the player inventory"""
    player.check_inventory() #print items in inventory
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
    """uses or inspects a selected item in th eplayer inventory"""
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
            return selected_item.use
        if inspect == True:
            return selected_item.inspect
    else:
        fancy_print("Invalid number, please enter a number from the list.")
        player_use_item(player=player, use=use, inspect=inspect)

