from __future__ import annotations
import time
import os
from sys import platform
from playsound import playsound

from src.locations import Location
from src.characters import Player
from src.utils.utils import fancy_print
from src.player_options import player_options
from src.stage_2_objects import acne_scarf, bear, sven, francoise, statue, stroopwafels, mural_drawing
from src.scenes_text.stage_two_text import entering_stage_two, ascii_boat_trip, reset_stats_and_stuff, stage_two_barrier, enter_the_harbor
from src.utils.llm import generate_text

def enter_stage_two_fight(player:Player, location=None, npc=None):
    fancy_print("\nYou strike the old pirate down! That'll teach him to call you names!\n")

    response = generate_text(
        system_prompt="You are a drunken pirate who has just received a death blow.",
        user_prompt="Ha-ha! That will teach you to call me names. Die pirate scum!"
        )
    formatted_response = response.replace('\n', '\n\t\t')
    
    fancy_print(f"""Marlow the Skipper: {formatted_response}\n""", speed=0.06, color="BLUE")

    fancy_print("Marlowe's lifeless body lies at your feet. Will you give him a pirate's grave before you steal his skiff?")

    player_input = ""

    while player_input not in ["yes", "no"]:
        player_input = input("yes/no: ")
        print()

        if player_input.lower() == "yes":
            fancy_print("You search the body for any valuable items but find that his life amouted to very little riches.")
            fancy_print("You kick the corpse of the pier. As the body floats away on the waves, you take of your hat and give a small nod to thank Marlowe for his ship.")
            print()
            fancy_print("By pirate law, you now own a boat!\n", dim=True)
            return enter_stage_two(player=player)
            
        if player_input.lower() == "no":
            fancy_print("You leave Marlowe's corpse on the pier. Some customs agent will deal with it later, you figure.\n")
            fancy_print("By pirate law, you now own a boat!\n", dim=True)
            return enter_stage_two(player=player)

        else:
            fancy_print("Invalid answer, please enter 'yes' or 'no'")


def enter_stage_two_gift(player:Player, location=None, npc=None):
    fancy_print("As you hand Marlowe the bottle of rum, you immediately know this was the right course of action.\n")
    response = generate_text(
        system_prompt="You are a drunken pirate who has just received a bottle of rum.",
        user_prompt="Here's a bottle of rum. Does that change your mind about giving me passage on your skiff?"
        )
    formatted_response = response.replace('\n', '\n\t\t')
    fancy_print(f"""Marlow the Skipper: {formatted_response}\n""", speed=0.06, color="BLUE")
    fancy_print("He steps aside swaying and let's you board his skiff.")
    return enter_stage_two(player=player)

def enter_stage_two(player:Player, location=None, npc=None):
    """Starts the second of the story"""
    
    #create nice transition to second stage
    time.sleep(2)

    if platform == "darwin":
        # OS X
        os.system('clear')
    if platform == "win32":
        # Windows...
        os.system('cls')

    fancy_print(stage_two_barrier, color="CYAN")
    print()
    fancy_print(f"\nWell {player.name}, you made it to the second chapter. \n\nYour game is saved. If you die, you can restart from this checkpoint.\n", bright=True)

    fancy_print("Note for the real Djoko:", speed=0.05, color="MAGENTA", bright=True)
    fancy_print("You've made it off the island, good stuff. You've earned present #2\n", speed=0.06, color="MAGENTA")
    
    #set up locations for stage 2
    locations = create_harbour_locations()

    #print scene two opening and pick up scarf
    playsound("src/sounds/ocean_waves_sound.wav", block=False)
    fancy_print(ascii_boat_trip, speed=0.01, color="BLUE")
    fancy_print(entering_stage_two, speed=0.03)

    acne_scarf.pick_up(player=player)

    #reset and improve the players stats
    fancy_print(reset_stats_and_stuff, speed=0.02)
    print()
    player.max_hp = 14
    player.hp = player.max_hp
    player.damage += 2
    fancy_print(f"Your max heath is now {player.max_hp} and your damage is {player.damage}!", dim=True)
    player.health_bar.update()
    player.health_bar.draw()
    print()
    playsound("src/sounds/sailing_into_the_city.wav", False)
    fancy_print(enter_the_harbor)
    #start game loop and place player at campfire
    player_options(player=player, location=locations['Port of Amsterdam'])


def create_harbour_locations():
    harbour_entrance = Location(
        name="Port of Amsterdam",
        description="""
        The Port of Amsterdam is a bustling hub of activity. Ships of various sizes dock here, their sails billowing in the wind.
        The salty sea air mixes with the scents of exotic spices and fresh fish. Sailors shout orders and greetings, while merchants
        haggle over prices. The cobblestone streets are worn smooth by countless footsteps, and the sounds of seagulls still fill the air.
        
        From here, you can already hear sounds of a bustling market. Bordering the market a popular inn, next to which lies a shadowy alleyway.
        """,
        NPCS=[],
        items=[]
        )

    market = Location(
        name="market",
        description="""
        The market near the port of Amsterdam is a cacophony of sounds and a riot of colors. Street children weave through the
        market stalls, their laughter mingling with the vendors' shouts. The air is thick with the mouth-watering aromas of freshly baked
        bread, sizzling meats, and fragrant spices from all the corners of the earth.
        Each stall seems to hold a new mystery, beckoning you to explore further. 
        
        Several stall catch your eye. You also see a large old inn on the edge of the markt. The port lies behind you.
        """,
        NPCS=[],
        items=[statue]
    )

    market_cookie_stall = Location(
        name="cookie stall",
        description="""
        This stall is filled with delicious stroopwafel cookies! The vendor does not seem to be around at the moment.
        A pile of still piping hot stroopwafels lays on the counter, with a little sign saying "Free stroopwafels, 1 per person please!"
        The sweet, warm scent of caramel and waffle wafts through the air, making it hard for anyone passing by to resist. 
        
        The stall itself is quaint, with a simple wooden structure and a few decorative touches that give it a cozy, inviting feel. 
        It almost makes you forget the rest of the market around you.
        """,
        NPCS=[],
        items=[stroopwafels]
    )

    # market_fruit_stall = Location(
    #     name="fruit stall",
    #     description="""
    #     The fruit stall is a feast for the eyes, with vibrant piles of fresh, juicy fruits arranged in enticing displays. 
    #     The vendor is an attractive, bright young woman with a sun-kissed face. She greets you with a broad smile. 
    #     The air is filled with the sweet scent of ripe passion fruit, oranges, and strawberries. 
        
    #     This colorful stall is just one of many on the lively market.
    #     """,
    #     NPCS=[fruit_vendor],
    #     items=[assorted_fruits]
    # )

    old_pub = Location(
        name="the Leaky Fawcett Pub",
        description="""
        The "Leaky Fawcett" pub looks like a Jan Steen painting brought to life. 
        The low-ceilinged room is filled with the hum of animated conversation and the rich aroma of spiced wine and freshly baked bread. 
        A roaring fire crackles in the hearth, casting a golden glow over the scene. 
        Patrons crowd around mismatched tables, their faces flushed with drink and merriment. 
        A group of dwarves engages in a boisterous arm-wrestling match, while nearby,
        an elf and a human share a secretive conversation, their heads bent close together. 
        Children sit below the tables playing. 

        In one corner, a Nordic-looking bard with a braided beard and a fur-lined cloak strums a lyre. 
        At a table near the fire, a female ranger, her skin sun-kissed and her eyes sharp as a hawk’s, leans back in her chair.
        Her boots are propped up on the table.
        At the bar the strangest sight of all can be seen. A large bear in cap sits on a stool. 
        The bear speaks in a deep, rumbling voice to the bartender. 
    
        The atmosphere is a perfect blend of camaraderie and chaos, where magic and reality intertwine seamlessly.
        """,
        NPCS=[sven, francoise, bear],
        items=[],
        sound=["src/sounds/tavern_1.wav", "src/sounds/tavern_2.wav"]
    )

    alleyway = Location(
        name="alleyway",
        description="""
        The cobblestone alleyway is completely deserted. There is a oddly shaped drawing on the one of the walls. 
        The other wall is blocked by stacked crates.
        
        On your left is the back entrance to a pub, while the end of the street leads back to the port.  
        """,
        NPCS=[],
        items=[mural_drawing]
    )


    #setup connections
    harbour_entrance.add_accessible_locations(market)
    harbour_entrance.add_accessible_locations(alleyway)
    harbour_entrance.add_accessible_locations(old_pub)
    market.add_accessible_locations(old_pub)
    alleyway.add_accessible_locations(old_pub)
    market.add_accessible_locations(market_cookie_stall)
    # market.add_accessible_locations(market_fruit_stall)
    # market_fruit_stall.add_accessible_locations(market_cookie_stall)


    return {
        "Port of Amsterdam": harbour_entrance,
        "market": market,
        "cookie stall": market_cookie_stall,
        # "fruit stall": market_fruit_stall,
        "the Leaky Fawcett Pub":old_pub,
        "alleyway": alleyway
        }


