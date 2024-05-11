import os
from create_player import create_player
from stage_1 import enter_stage_one
from src.utils.utils import fancy_print


def game_loop():
    #start / clear screen / opening title
    os.system('cls')
    fancy_print("_________\U0001F9CC____\U0001F9DA____\U0001F9CC____\U0001F9DA____\U0001F9CC____\U0001F9DA____ WELCOME TO DJOKO_QUEST ____\U0001F9DA____\U0001F9CC____\U0001F9DA____\U0001F9CC____\U0001F9DA____\U0001F9CC_________", speed=0.3, color="MAGENTA", bright=True)
    print()
    print()

    #create player instance
    player = create_player()

    #start stage 1
    enter_stage_one(player=player)

    # your have reached a checkpoint. Your game is saved.
    # save_state = ...

    # enter_stage_two(save_state)

game_loop()