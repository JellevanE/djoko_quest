from __future__ import annotations

from src.locations import Location
from src.characters import Player, NPC
from src.items import Item
from src.utils.utils import fancy_print
from scenes_text.island_campfire import opening_wake_up, ascii_island
from test import wizard, old_wand, rusty_key
from src.player_options import player_options
from src.stage_1_objects import bottle_of_rum, skipper, cook



def enter_stage_one(player:Player):
    """Starts the first stage of the story"""
    #write opening scene
    locations = create_island_locations()
    fancy_print(ascii_island, speed=0.001, color="YELLOW")
    fancy_print(opening_wake_up, speed=0.001)
    player_options(player=player, location=locations['campfire']) #test string


if __name__ == '__main__':
    print("stages")


def create_island_locations():
    island_campfire = Location(
        name="the campfire",
        description="add description here",
        interactions=[wizard],
        objects=[old_wand]
        )

    island_docks = Location(
        name="the docks",
        description="There are a number of big ships in the harbour. Their main masts reach high into the sky. A boat on your left is called 'Bird', you wonder which bird is meant. At the end of the docks you see a lone figure preparing a skiff for sea.",
        interactions=[skipper],
        objects=[]
    )

    island_fortress_entrance = Location(
        name="the fortress entrance",
        description="add description here",
        interactions=[],
        objects=[rusty_key]
    )

    island_fortress_hallway = Location(
        name="the fortress hallway",
        description="add description here",
        interactions=[],
        objects=[]
    )

    island_fortress_dungeons = Location(
        name="the fortress dungeons",
        description="add description here",
        interactions=[],
        objects=[]
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
