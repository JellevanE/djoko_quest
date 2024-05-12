from __future__ import annotations

from src.locations import Location
from src.characters import Player, NPC
from src.items import Item
from src.utils.utils import fancy_print
from scenes_text.island_campfire import opening_wake_up, ascii_island
from test import wizard, old_wand
from src.player_options import player_options
from src.stage_1_objects import bottle_of_rum, skipper, cook, natural_wine, fortress_sign, rusty_key, bird, wooden_club, spittle_goblin



def enter_stage_one(player:Player):
    """Starts the first stage of the story"""
    #set up locations for stage 1
    locations = create_island_locations()

    #print opening scene text and add natural wine to inventory
    fancy_print(ascii_island, speed=0.001, color="YELLOW")
    fancy_print(opening_wake_up, speed=0.001)
    natural_wine.pick_up(player=player)
    print()

    #start game loop and place player at campfire
    player_options(player=player, location=locations['campfire'])


if __name__ == '__main__':
    print("stages")


def create_island_locations():
    island_campfire = Location(
        name="the campfire",
        description="""
        You hear the distant sounds of seaguls and feel a gentle island breeze on your skin.
        Around you stand a couple of palm trees and the smoldering remains of a small campfire.

        To the north you can see the outline of a blocky old fortress.
        To the west you see several masts on the horizon signifying a harbour.""",
        interactions=[wizard],
        objects=[old_wand]
        )

    island_docks = Location(
        name="the docks",
        description="""
        There are a number of big ships in the harbour. Their main masts reach high into the sky.
        A boat on your left is called 'Bird', you wonder which bird is meant.
        At the end of the docks you see a lone figure preparing a skiff for sea.
        
        Behind you the light smoke plumes of a campfire can be seen in the skies to the east.
        To the north you can see an old fortress in the distance.""",
        interactions=[skipper],
        objects=[bird]
    )

    island_fortress_entrance = Location(
        name="the fortress entrance",
        description="add description here",
        interactions=[],
        objects=[fortress_sign]
    )

    island_fortress_hallway = Location(
        name="the fortress hallway",
        description="""
        You enter the hallway. 
        The walls are slabs of grey concrete and the ceiling is high and slightly arched.
        It's dimly lit by a few candles scattered along the walls. There is some debris on the floor.

        At one end of the hallway is the entrance to the island,
        at the other end the hallway splits into two doorways. 
        Through one the light of a hearthfire shines. 
        The light is accompanied by the smell of fried onions, melted butter and some spices you can't quite place.
        You figure it must be the kitchen. 
        The other portal is dark and seems deserted.""",
        interactions=[],
        objects=[rusty_key]
    )

    island_fortress_dungeons = Location(
        name="the fortress dungeons",
        description="""
        The dungeon is dark, humid and moldy. Somebody should really do some sfeer-beheer in here...
        There are some weapon racks to your left and cells on your right. 
        The cells are empty except for an old female goblin.

        Behind you is the doorway leading back to the fortress hallway.""",
        interactions=[spittle_goblin],
        objects=[wooden_club]
    )

    island_fortress_kitchens = Location(
        name="the fortress kitchens",
        description="add description here",
        interactions=[cook],
        objects=[]
    )

    #setup connections
    island_campfire.add_accessible_locations(island_docks)
    island_campfire.add_accessible_locations(island_fortress_entrance)
    island_fortress_entrance.add_accessible_locations(island_docks)
    island_fortress_entrance.add_accessible_locations(island_fortress_hallway)
    island_fortress_hallway.add_accessible_locations(island_fortress_kitchens)
    island_fortress_hallway.add_accessible_locations(island_fortress_dungeons)

    return {
        "campfire": island_campfire,
        "docks": island_docks,
        "fortress_entrance": island_fortress_entrance,
        "fortress_hallway": island_fortress_hallway,
        "fortress_kitchens": island_fortress_kitchens,
        "fortress_dungeons": island_fortress_dungeons
    }
