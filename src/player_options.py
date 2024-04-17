from src.locations import Location
from src.characters import Player, NPC
from src.items import Item
from src.utils.utils import fancy_print


def player_options(player:Player, location = Location):
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
    print()

    while action.lower() not in ["a", "b", "c", "d"]:
        fancy_print("Please choose one of the options by typing the corresponding letter.")
        print("I choose: ")
        action = input()

    if action.lower() == "a":
        player_move_to_location(player=player, location=location)

    if action.lower() == "b": #interact action FIX THIS
        action = "perform interact"

    if action.lower() == "c":
        inspect_action(player=player, location=location)

    if action.lower() == "d":
        inventory_action(player=player, location=location)

def player_move_to_location(player:Player, location:Location):
    """default action to move to a new location"""
    accessible_locations = location.accessible_locations

    fancy_print(f"You decide to leave {location.name} \n", speed=0.05, dim=True)
    print()

    if len(accessible_locations) == 0:
        fancy_print("Hmm.. It doesn't look like you can leave..")
        print()
        return player_options(player=player, location=location)

    fancy_print("Where do you want to go?")
    for i, item in enumerate(accessible_locations, start=1):
        fancy_print(f"{i}: {item}")

    print()
    selected_number = int(input("I'm going to: "))
    print()

    # Adjust for zero-based index
    selected_index = selected_number - 1

    # Validating if the input is within the available item range
    if 0 <= selected_index < len(accessible_locations):
        selected_location = accessible_locations[selected_index]
        location = selected_location #update location

        fancy_print(f"{player.name} moves to {location.name}")
        fancy_print(f"{location.description}")
        print()
        return player_options(player=player, location=location) ### SHOULD BE ACCESS NEW LOCATION: MOVETO

    else:
        fancy_print("Invalid number, please enter a number from the list.")
        return player_move_to_location(player=player, location=location)


def inspect_action(player:Player, location:Location):
    """default action to inspect object in a location"""
    fancy_print("You look around and inspect your surroundings more closely... \n", speed=0.08, dim=True)
    fancy_print("You spot the following things:")

    player_inspect_object(player=player, location=location)

    print()

    player_options(player=player, location=location)


def player_inspect_object(player:Player, location:Location):
    """enumerates objects to inspect and prompts player"""
    items = location.objects
    if len(items) == 0:
        fancy_print("There seem to be no items of importance here.")
        print()
        return player_options(player=player, location=location)

    for i, item in enumerate(items, start=1):
        fancy_print(f"{i}: {item}")

    print()
    selected_number = int(input("Enter the number of the object you want to inspect: "))
    print()

    # Adjust for zero-based index
    selected_index = selected_number - 1

    # Validating if the input is within the available item range
    if 0 <= selected_index < len(items):
        selected_item = items[selected_index]
        selected_item.inspect()

        print()
        fancy_print(f"Do you want to take {selected_item.name}?", speed=0.1, dim=True)
        take_item = input("yes/no: ")

        if take_item.lower() == "yes":
            selected_item.pick_up(player=player)
            print()

            if selected_item.can_take == True:
                location.objects.remove(selected_item)

            return player_options(player=player, location=location)
            
        if take_item.lower() == "no":
            return player_options(player=player, location=location)

    else:
        fancy_print("Invalid number, please enter a number from the list.")
        return player_inspect_object(player=player, location=location)

    
def inventory_action(player:Player, location:Location):
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
        return player_options(player=player, location=location)
    

def player_use_item(player:Player, use:bool, inspect:bool): ### NEEDS FIXING
    """uses or inspects a selected item in the player inventory"""
    items = player.inventory

    for i, item in enumerate(items, start=1):
        fancy_print(f"{i}: {item}")

    print()

    # Ask the user to choose a number
    if use == True:
        selected_number = int(input("Enter the number of the item you want to use: "))
    if inspect == True:
        selected_number = int(input("Enter the number of the item you want to inspect: "))

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