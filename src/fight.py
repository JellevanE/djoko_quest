import os
import json
from src.characters import Player, NPC
from src.items import Item
from src.locations import Location
from src.utils.utils import fancy_print
from src.utils.llm import generate_text
from src.utils.clear_screen import clear_screen

SAVE_FILE_PATH = "savefile.json"

def fight_character(player:Player, character:NPC, location:Location):
    print()
    while player.hp and character.hp != 0:

        player.health_bar.draw()
        character.health_bar.draw()

        player.attack(character)
        character.attack(player)
        
        print("\n")
    
    if player.hp == 0:
        return game_over(player=player)
    if character.hp == 0:
        fancy_print(f"You beat {character.name}!", dim=True)
        location.remove_npc(npc=character)
        if isinstance(character.reward, Item):
            return character.reward.pick_up(player=player)
        else:
            return character.reward(player)
    

def game_over(player:Player):
    fancy_print(f"You died {player.name}...", speed=0.2, dim=True)
    print("\n")

    fancy_print(generate_text(
        system_prompt="You are a shakespeare expert",
        user_prompt="provide a short direct quote from shakespeare about death"), color="BLUE", bright=True
        )
    print("\n")

    fancy_print("Do you want to try again?")
    print("Type 'yes' if you'd like to give it another go, type quit if you want to exit.\n")

    answer = ""
    
    while answer.lower() not in ["quit", "yes"]:
        answer = input(f"{player.name}: ")
        if answer == "quit":
            return quit()
        if answer == "yes":
            print("\n \n") 
            fancy_print("Restarting game...\n", speed=0.2, bright=True)
            
            clear_screen()

            #save player data
            with open(SAVE_FILE_PATH, 'w') as f:
                json.dump(player.to_dict(), f) 
            
            os.system(f'python main.py {player}')
