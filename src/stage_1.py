from __future__ import annotations

from src.locations import Location
from src.characters import Player
from src.utils.utils import fancy_print
from src.scenes_text.island_campfire import opening_wake_up, ascii_island
from src.player_options import player_options
from src.stage_1_objects import skipper, cook, natural_wine, fortress_sign, rusty_key, bird, wooden_club, spittle_goblin, sandy_ground, hallway_portrait, palm_trees, guards_helmet, cooking_pot, bag_of_spices, old_guard
from playsound import playsound



def enter_stage_one(player:Player):
    """Starts the first stage of the story"""
    #set up locations for stage 1
    locations = create_island_locations()

    #print opening scene text and add natural wine to inventory
    playsound("src\sounds\seagulls.wav", block=False)
    fancy_print(ascii_island, speed=0.01, color="YELLOW")
    fancy_print(opening_wake_up, speed=0.02)
    natural_wine.pick_up(player=player)

    #start game loop and place player at campfire
    player_options(player=player, location=locations['campfire'])


if __name__ == '__main__':
    print("stages")


def create_island_locations():
    island_campfire = Location(
        name="the campfire",
        description="""
        You hear the distant sounds of seaguls and feel a gentle island breeze on your skin.
        Around you stand a couple of palm trees, and the smoldering remains of a small campfire emit a comforting warmth.

        To the north the silhouette of a blocky old fortress looms against the sky.
        To the west, several masts rise on the horizon, indicating a harbour.""",
        NPCS=[],
        items=[sandy_ground, palm_trees]
        )

    island_docks = Location(
        name="the docks",
        description="""
        The harbor is more deserted than you expected. A number of big ships are anchored, rocking gently on the waves.
        Their main masts reach high into the sky and their crews seem largely absent.

        A boat on your left is called 'Bird', you wonder which bird is meant.
        At the end of the docks a lone figure is busy preparing a skiff for sea.
        
        Behind you the light smoke plumes of a campfire can be seen drifting in the skies to the east.
        To the north you can see an old fortress in the distance.""",
        NPCS=[skipper],
        items=[bird]
    )

    island_fortress_entrance = Location(
        name="the fortress entrance",
        description="""
        You stand before the imposing entrance of an ancient fortress. The stone walls rise high, 
        covered in creeping ivy and moss. The heavy wooden doors are slightly ajar, creaking as they 
        sway with the breeze. A weathered sign hangs nearby, its text barely legible. 
        
        The path behind you leads back to the campfire and docks, while the entrance beckons you inside.""",
        NPCS=[old_guard],
        items=[fortress_sign, guards_helmet]
    )

    island_fortress_hallway = Location(
        name="the fortress hallway",
        description="""
        You enter the hallway, its walls made of grey concrete slabs, and the ceiling high and slightly arched.
        It's dimly lit by a few candles scattered along the walls. There is some debris on the floor.

        The dim lighting from a few scattered candles casts eerie shadows along the walls. Debris litters the floor, hinting at the fortress's age.

        At one end of the hallway is the entrance to the island, while at the other end, the hallway splits into two doorways.
        Through one, the warm light of a hearthfire shines, accompanied by the tantalizing smell of fried onions, melted butter, and unfamiliar spices, suggesting 
        a kitchen.
        The other doorway lies in darkness, seemingly abandoned.
""",
        NPCS=[],
        items=[rusty_key, hallway_portrait]
    )

    island_fortress_dungeons = Location(
        name="the fortress dungeons",
        description="""
        The dungeon is dark, humid and moldy. Somebody should really do some sfeer-beheer in here...
        There are some weapon racks to your left and cells on your right. 
        The cells are empty except for an old female goblin.

        Behind you is the doorway leading back to the fortress hallway.""",
        NPCS=[spittle_goblin],
        items=[wooden_club]
    )

    island_fortress_kitchens = Location(
        name="the fortress kitchens",
        description="""
        The kitchen is warm and bustling with activity. The smell of fried onions, melted butter, 
        and a variety of spices fills the air. Pots and pans clatter as the cook prepares a meal. 
        Shelves lined with jars of preserved goods and fresh produce are scattered around. 
        The hearthfire crackles invitingly, casting a cozy glow across the room. 

        The fortress hallway lies just outside.""",
        NPCS=[cook],
        items=[cooking_pot, bag_of_spices]
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
