from src.characters import Player, NPC
from src.items import Item
from src.utils.utils import fancy_print
from scenes_text.island_campfire import opening_wake_up, ascii_island
from test import wizard
from create_player import create_player
from src.player_options import player_options


def enter_stage_one(player:Player):
    """Starts the first stage of the story"""
    #write opening scene
    fancy_print(ascii_island, speed=0.01, color="YELLOW")
    fancy_print(opening_wake_up)
    player_options(player=player, locations=["fortress", "docks"], interactions=wizard, objects=[]) #test string





if __name__ == '__main__':
    print("stages")