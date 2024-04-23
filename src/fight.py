from src.characters import Player, NPC
from src.utils.utils import fancy_print
from src.utils.llm import generate_text
import os



def fight_character(player:Player, character:NPC):
    while player.hp and character.hp != 0:
        print("\n")

        player.health_bar.draw()
        character.health_bar.draw()

        player.attack(character)
        character.attack(player)

        print("\n")
    
    if player.hp == 0:
        return game_over(player=player)
    if character.hp == 0:
        fancy_print(f"You beat {character.name}!")
        return character.reward
    

def game_over(player:Player):
    fancy_print(f"You died {player.name}...", speed=0.2)
    print("\n")

    fancy_print(generate_text(
        system_prompt="You are a shakespeare expert",
        user_prompt="provide a short direct quote from shakespeare about death")
        )
    print("\n")

    fancy_print("Do you want to try again?")
    print("Type y if you'd like to give it another go, type quit if you want to exit.")

    answer = ""
    
    while answer.lower() not in ["quit", "y"]:
        answer = input(f"{player.name}: ")
        if answer == "quit":
            return quit()
        if answer == "y": 
            fancy_print("Restarting game", bright=True)
            os.system('cls')
            os.system('python main.py')
