from __future__ import annotations

from src.locations import Location
from src.characters import Player, NPC
from src.items import Item
from src.utils.utils import fancy_print
from src.player_options import player_options
from src.stage_2_objects import acne_scarf
from scenes_text.stage_two_text import entering_stage_two, ascii_boat_trip, reset_stats_and_stuff


def enter_stage_two(player:Player, location=None, npc=None):
    """Starts the second of the story"""
    #set up locations for stage 2
    locations = create_harbour_locations()

    #print scene two opening and pick up scarf
    fancy_print(ascii_boat_trip, speed=0.01, color="BLUE")
    fancy_print(entering_stage_two, speed=0.01)

    acne_scarf.pick_up(player=player)
    print()

    #reset and improve the players stats
    fancy_print(reset_stats_and_stuff, speed=0.01, dim=True)
    player.max_hp = 14
    player.hp = player.max_hp
    player.damage =+2
    fancy_print(f"Your max heath is now {player.max_hp} and your damage is {player.damage}!")
    player.health_bar.update()
    player.health_bar.draw()
    print()

    #start game loop and place player at campfire
    player_options(player=player, location=locations['Port of Amsterdam'])


def create_harbour_locations():
    harbour_entrance = Location(
        name="",
        description="""
        You hear the distant sounds of seaguls and feel a gentle island breeze on your skin.
        Around you stand a couple of palm trees and the smoldering remains of a small campfire.

        To the north you can see the outline of a blocky old fortress.
        To the west you see several masts on the horizon signifying a harbour.""",
        NPCS=[],
        items=[]
        )

    market = Location(
        name="",
        description="""
        """,
        NPCS=[],
        items=[]
    )

    #setup connections
    harbour_entrance.add_accessible_locations(market)


    return {
        "Port of Amsterdam": harbour_entrance,
        "Market": market,
        }