from src.locations import Location
from src.characters import Player, NPC
from src.items import Item, Weapon, UsableItem
from src.utils.utils import fancy_print, get_valid_input
from src.fight import fight_character


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
        player_choose_npc(player=player, location=location)

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

    # Adding an option to go back to the previous menu
    fancy_print(f"{len(accessible_locations) + 1}: Go back to previous options")

    print()
    selected_number = get_valid_input("I'm going to: ", len(accessible_locations) + 1) #int(input("I'm going to: "))
    print()

    # Adjust for zero-based index
    selected_index = selected_number - 1

    # Check if the selected option is to go back to the main menu
    if selected_number == len(accessible_locations) + 1:
        fancy_print("Returning to previous options...")
        fancy_print(f"You are still at {location.name}")
        print()
        fancy_print(f"{location.description}")
        print()
        return player_options(player=player, location=location)

    # Validating if the input is within the available item range
    if 0 <= selected_index < len(accessible_locations):
        selected_location = accessible_locations[selected_index]
        location = selected_location #update location

        fancy_print(f"{player.name} travels to {location.name}")
        fancy_print(f"{location.description}")
        print()
        return player_options(player=player, location=location) ### SHOULD BE ACCESS NEW LOCATION: MOVETO

    else:
        fancy_print("Invalid number, please enter a number from the list.")
        return player_move_to_location(player=player, location=location)


def player_choose_npc(player:Player, location:Location):
    npcs_list = location.interactions
    
    #check if there are NPCs
    if len(npcs_list) == 0:
        fancy_print("There doesn't seem to by anybody around, it makes you feel a bit lonely..")
        print()
        return player_options(player=player, location=location)

    #list available NPCs
    fancy_print("Who do you want to interact with?")
    for i, item in enumerate(npcs_list, start=1):
        fancy_print(f"{i}: {item}")

    # Adding an option to go back to the previous menu
    fancy_print(f"{len(npcs_list) + 1}: Go back to previous options")

    print()
    selected_number = get_valid_input(f"{player.name}: ", len(npcs_list) + 1)
    print()

    # Adjust for zero-based index
    selected_index = selected_number - 1

    if selected_number == len(npcs_list) + 1:
        fancy_print("Returning to previous options...")
        fancy_print(f"You are still at {location.name}")
        print()
        fancy_print(f"{location.description}")
        print()
        return player_options(player=player, location=location)
    
    # Validating if the input is within the available item range
    if 0 <= selected_index < len(npcs_list):
        selected_npc = npcs_list[selected_index]
        interact_with_npc(player=player, location=location, npc=selected_npc)
        
        print()
        return player_options(player=player, location=location)


def interact_with_npc(player:Player, location:Location, npc:NPC):
    """Default function to interact with an NPC, gives player 4 options"""

    fancy_print(f"What do you want to do with {npc.name}?")

    fancy_print("""
          a: talk
          b: fight
          c: inspect
          d: return to options
          """)
    print("I choose: ")
    npc_action = input()
    
    while npc_action.lower() not in ["a", "b", "c", "d"]:
        fancy_print("Please choose one of the options by typing the corresponding letter.")
        print("I choose: ")
        npc_action = input()

    if npc_action.lower() == "a": #talk to character
        print()
        result = npc.talk(user_name=player.name)

        if result == False:
            return interact_with_npc(player=player, location=location, npc=npc)
        
        else:
            return npc.reward

    if npc_action.lower() == "b": #fight character

        if npc.will_fight == True:
            return fight_character(player=player, character=npc)

        if npc.will_fight == False:
            fancy_print(f"It doesn't look like {npc.name} is interested in fighting you.")
            return interact_with_npc(player=player, location=location, npc=npc)

    if npc_action.lower() == "c": #inspect character

        print()
        npc.inspect()
        print()

        return interact_with_npc(player=player, location=location, npc=npc)
    
    if npc_action.lower() == "d": #inventory action
        return player_options(player=player, location=location)

    return player_options(player=player, location=location)


def inspect_action(player:Player, location:Location):
    """default action to inspect object in a location"""
    print()
    fancy_print("You look around and inspect your surroundings more closely... \n", speed=0.06, dim=True)
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

    # Adding an option to go back to the previous menu
    fancy_print(f"{len(items) + 1}: Go back to previous options")

    print()
    selected_number = get_valid_input("Enter the number of the object you want to inspect: ", len(items) + 1)
    print()

    # Adjust for zero-based index
    selected_index = selected_number - 1

    #return to previous options
    if selected_number == len(items) + 1:
        fancy_print("Returning to previous options...")
        fancy_print(f"You are still at {location.name}")
        print()
        fancy_print(f"{location.description}")
        print()
        return player_options(player=player, location=location)
    
    # Validating if the input is within the available item range
    if 0 <= selected_index < len(items):
        selected_item = items[selected_index]
        selected_item.inspect()

        print()
        fancy_print(f"Do you want to take {selected_item.name}?", speed=0.1, dim=True)
        take_item = ""

        while take_item not in ["yes", "no"]:
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
                fancy_print("Invalid answer, please enter 'yes' or 'no'")

    
def inventory_action(player:Player, location:Location):
    """default action to access the player inventory"""
    fancy_print("Your inventory contains: ")
    items = player.inventory

    for i, item in enumerate(items, start=1):
        fancy_print(f"{i}: {item.name}")

    print()

    fancy_print("What do you do?")
    fancy_print("""
          a: use
          b: inspect
          c: return to options
          """)
    print("I choose: ")
    inventory_action = input()
    
    while inventory_action.lower() not in ["a", "b", "c"]:
        fancy_print("Please choose one of the options by typing the corresponding letter.")
        print("I choose: ")
        inventory_action = input()
    if inventory_action.lower() == "a":
        player_use_item(player=player, location=location, use=True, inspect=False)

    if inventory_action.lower() == "b":
        player_use_item(player=player, location=location, use=False, inspect=True)

    if inventory_action.lower() == "c":
        return player_options(player=player, location=location)
    

def player_use_item(player:Player, location:Location, use:bool, inspect:bool): ### NEEDS FIXING
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
            return use_item_on(player=player, location=location, item=selected_item)
        if inspect == True:
            selected_item.inspect()
            return inventory_action(player=player,location=location)
    else:
        fancy_print("Invalid number, please enter a number from the list.")
        player_use_item(player=player, use=use, inspect=inspect)

def use_item_on(player:Player, location:Location, item:Item):
    if isinstance(item, Weapon):
        return item.use(player=player)
    
    if isinstance(item, UsableItem):
        fancy_print(f"What do you want to use {item.name} on?")

        object_list = location.interactions + location.objects
        
        for i, item in enumerate(object_list, start=1):
            fancy_print(f"{i}: {item}")

        # Adding an option to go back to the previous menu
        fancy_print(f"{len(object_list) + 1}: Go back to previous options")
    
        print()
        selected_number = get_valid_input(f"{player.name}: ", len(object_list) + 1)
        print()

        # Adjust for zero-based index
        selected_index = selected_number - 1

        if selected_number == len(object_list) + 1:
            fancy_print("Returning to previous options...")
            fancy_print(f"You are still at {location.name}")
            print()
            fancy_print(f"{location.description}")
            print()
            return player_options(player=player, location=location)
    
        # Validating if the input is within the available item range
        if 0 <= selected_index < len(object_list):

            selected_object = object_list[selected_index]
            item.use(player=player, object=selected_object)
        
            print()
            return player_options(player=player, location=location)
