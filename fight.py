from characters import Player, NPC
from src.utils import fancy_print
from llm import generate_text

def fight_character(player:Player, character:NPC, victory_option):
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
        return print(victory_option)
    

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
            return print("restart game") #enter restart function here
