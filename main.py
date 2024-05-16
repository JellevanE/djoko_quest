import os
import sys
import json
from src.characters import Player
from src.utils.create_player import create_player
from src.stage_1 import enter_stage_one
from src.stage_2 import enter_stage_two
from src.utils.utils import fancy_print
from src.utils.clear_screen import clear_screen

SAVE_FILE_PATH = "savefile.json"

def load_player() -> Player:
    if os.path.exists(SAVE_FILE_PATH):
        with open(SAVE_FILE_PATH, 'r') as f:
            player_data = json.load(f)
            return Player.from_dict(player_data)  # You'll need to implement `from_dict` method in Player class
    return None

def save_player(player):
    with open(SAVE_FILE_PATH, 'w') as f:
        json.dump(player.to_dict(), f)  # You'll need to implement `to_dict` method in Player class


def game_loop():
    #start / clear screen / opening title
    clear_screen()

    player = load_player()

    if player:
        if player.current_stage == 1:
            fancy_print("Loading checkpoint...", speed=0.2, bright=True)
            clear_screen()
            return enter_stage_one(player=player)
        if player.current_stage == 2:
            fancy_print("Loading checkpoint...", speed=0.2, bright=True)
            clear_screen()
            return enter_stage_two(player=player)
    
    #opening title
    print()
    print()
    fancy_print("_________\U0001F9CC____\U0001F9DA____\U0001F9CC____\U0001F9DA____\U0001F9CC____\U0001F9DA____ WELCOME TO DJOKO_QUEST ____\U0001F9DA____\U0001F9CC____\U0001F9DA____\U0001F9CC____\U0001F9DA____\U0001F9CC_________", speed=0.02, color="MAGENTA", bright=True)
    print()
    print()

    #create player instance
    player = create_player()

    #start stage 1
    enter_stage_one(player=player)


if __name__ == "__main__":
    game_loop()