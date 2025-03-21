from src.locations import Location
from src.characters import Player, NPC
from src.items import Item, Weapon, UsableItem
from src.utils.utils import fancy_print, get_valid_input
from src.fight import fight_character
from playsound import playsound


def player_options(player:Player, location = Location):
    """Access default action options for a player in a certain location"""
    fancy_print("""What do you do?
                
          a: move
          b: interact
          c: inspect
          d: inventory
          """, speed=0.01)
    print("I choose: ")
    action = input()
    print()

    while action.lower() not in ["a", "b", "c", "d"]:
        fancy_print("Please choose one of the options by typing the corresponding letter.")
        print("I choose: ")
        action = input()
        print()

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

    fancy_print(f"You decide to leave {location.name}.", speed=0.02, dim=True)
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
    selected_number = get_valid_input("I'm will travel to: ", len(accessible_locations) + 1)
    print()

    # Adjust for zero-based index
    selected_index = selected_number - 1

    # Check if the selected option is to go back to the main menu
    if selected_number == len(accessible_locations) + 1:
        fancy_print("Returning to previous options...")
        fancy_print(f"You are still at {location.name}")
        print()
        return player_options(player=player, location=location)

    # Validating if the input is within the available item range
    if 0 <= selected_index < len(accessible_locations):
        selected_location = accessible_locations[selected_index]
        location = selected_location #update location

        fancy_print(f"{player.name} travels to {location.name}.", dim=True)
        if location.sound:
            location.play_location_sound()
        fancy_print(f"{location.description}", speed=0.01)
        print()
        return player_options(player=player, location=location)

    else:
        playsound("src/sounds/error_sound.wav", False)
        fancy_print("Invalid number, please enter a number from the list.")
        return player_move_to_location(player=player, location=location)


def player_choose_npc(player:Player, location:Location):
    npcs_list = location.NPCS
    
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
          """, speed=0.01)
    print("I choose: ")
    npc_action = input()
    
    while npc_action.lower() not in ["a", "b", "c", "d"]:
        fancy_print("Please choose one of the options by typing the corresponding letter.")
        print("I choose: ")
        npc_action = input()

    if npc_action.lower() == "a": #talk to character
        print()
        result = npc.talk(player=player)
        if isinstance(result, Item):
            print()
            result.pick_up(player=player)

        #result false means the user stops the chat
        if result == False:
            print()
            return interact_with_npc(player=player, location=location, npc=npc)
        
        #check if result is a function
        if hasattr(result, '__call__'):
            result(player, location, npc)
        else:
            return npc.reward

    if npc_action.lower() == "b": #fight character

        if npc.will_fight == True:
            return fight_character(player=player, character=npc, location=location)

        if npc.will_fight == False:
            print()
            fancy_print(f"It doesn't look like {npc.name} is interested in fighting you.", dim=True)
            return interact_with_npc(player=player, location=location, npc=npc)

    if npc_action.lower() == "c": #inspect character

        print()
        npc.inspect()
        print()

        return interact_with_npc(player=player, location=location, npc=npc)
    
    if npc_action.lower() == "d": #inventory action
        print()
        return player_options(player=player, location=location)

    return player_options(player=player, location=location)


def inspect_action(player:Player, location:Location):
    """default action to inspect object in a location"""
    fancy_print("You look around and inspect your surroundings more closely... \n", speed=0.02, dim=True)
    fancy_print("You spot the following things:")

    player_inspect_object(player=player, location=location)

    print()

    player_options(player=player, location=location)


def player_inspect_object(player:Player, location:Location):
    """enumerates objects to inspect and prompts player"""
    items = location.items
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
        selected_item.inspect(player=player, location=location)

        print()
        fancy_print(f"Do you want to take {selected_item.name}?", speed=0.05, dim=True)
        take_item = ""

        while take_item not in ["yes", "no"]:
            take_item = input("yes/no: ")
            print()
            if take_item.lower() == "yes":
                selected_item.pick_up(player=player)

                if selected_item.can_take == True:
                    location.items.remove(selected_item)

                return player_options(player=player, location=location)
            
            if take_item.lower() == "no":
                return player_options(player=player, location=location)

            else:
                playsound("src/sounds/error_sound.wav", False)
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
          """, speed=0.01)
    print("I choose: ")
    inventory_action = input()
    print()
    
    while inventory_action.lower() not in ["a", "b", "c"]:
        fancy_print("Please choose one of the options by typing the corresponding letter.")
        print("I choose: ")
        inventory_action = input()
        print()

    if inventory_action.lower() == "a":
        player_use_item(player=player, location=location, use=True, inspect=False)

    if inventory_action.lower() == "b":
        player_use_item(player=player, location=location, use=False, inspect=True)

    if inventory_action.lower() == "c":
        return player_options(player=player, location=location)
    

def player_use_item(player:Player, location:Location, use:bool, inspect:bool):
    """uses or inspects a selected item in the player inventory"""
    fancy_print("Options: ")
    items = player.inventory

    for i, item in enumerate(items, start=1):
        fancy_print(f"{i}: {item}")


    fancy_print(f"{len(items) + 1}: Go back to previous options")
    
    print()

    # Ask the user to choose a number
    if use == True:
        selected_number = get_valid_input("Enter the number of the item you want to use: ", len(items) + 1)
    if inspect == True:
        selected_number = get_valid_input("Enter the number of the item you want to inspect: ", len(items) + 1)

    print()

    # Adjust for zero-based index
    selected_index = selected_number - 1

    if selected_number == len(items) + 1:
        return inventory_action(player=player, location=location)

    # Validating if the input is within the available item range
    if 0 <= selected_index < len(items):
        selected_item = items[selected_index]
        if use == True:
            return use_item_on(player=player, location=location, item=selected_item)
        if inspect == True:
            selected_item.inspect()
            print()
            return inventory_action(player=player,location=location)
    else:
        playsound("src/sounds/error_sound.wav", False)
        fancy_print("Invalid number, please enter a number from the list.")
        player_use_item(player=player, use=use, inspect=inspect)

def use_item_on(player: Player, location: Location, item: Item):
    #if item is weapon, equip weapon
    if isinstance(item, Weapon):
        return item.use(player=player)

    #for usable items check what to use on
    if isinstance(item, UsableItem):
        fancy_print(f"What do you want to use {item.name} on?")

        object_list = location.NPCS + location.items

        for i, obj in enumerate(object_list, start=1):
            fancy_print(f"{i}: {obj}")

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
            return player_options(player=player, location=location)

        # Validating if the input is within the available item range
        if 0 <= selected_index < len(object_list):
            selected_object = object_list[selected_index]

            if selected_object in item.usable_on:

                if isinstance(selected_object, NPC):
                    fancy_print(f"You give {item.name} to {selected_object}. \n", dim=True)
                    result = selected_object.solve_puzzle
                    player.remove_from_inventory(item=item)

                    if isinstance(result, Item):
                        print()
                        playsound("src/sounds/use_item_sound.wav", False)
                        result.pick_up(player=player)
                        return player_options(player=player, location=location)
                    else:
                        playsound("src/sounds/use_item_sound.wav", False)
                        result(player=player, location=location, npc=selected_object)
                        return player_options(player=player, location=location)

                if isinstance(selected_object, Item):
                    fancy_print(f"You use {item.name} on {selected_object}. \n", dim=True)
                    result =  selected_object.solve_puzzle

                    if isinstance(result, Item):
                        print()
                        playsound("src/sounds/use_item_sound.wav", False)
                        result.pick_up(player=player)
                        return player_options(player=player, location=location)  
                    else:
                        playsound("src/sounds/use_item_sound.wav", False)
                        result(player=player, location=location)
                        return player_options(player=player, location=location)
                    
            else:
                fancy_print("This item can't be used in this way.\n", dim=True)
                return use_item_on(player=player, location=location, item=item)

        else:
            playsound("src/sounds/error_sound.wav", False)
            fancy_print("Invalid number, please enter a number from the list.\n")
            return use_item_on(player=player, location=location, item=item)

    fancy_print("This item can't be used in this way.", dim=True)

    return player_options(player=player, location=location)