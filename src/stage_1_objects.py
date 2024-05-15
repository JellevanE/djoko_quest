from __future__ import annotations
from playsound import playsound
from src.characters import NPC, Player
from src.locations import Location
from src.items import Item, UsableItem, Weapon
from src.utils.utils import fancy_print
from stage_2 import enter_stage_two_fight, enter_stage_two_gift
from src.stage_2_objects import witch
from src.utils.llm import generate_text

### set stage items
### set stage NPCs

#DUNGEON OBJECTS
lump_of_clay = UsableItem(
    name="Lump of Clay",
    description="It's a lump of clay. Don't know what you expected to find here.",
    can_take=True,
    usable_on=[witch],
    solve_puzzle=None
)


wooden_club = Weapon(
    name="Wooden Club",
    description="It's a large wooden club. It's quite heavy, but if you give it a good swing it looks like it can do some damage in a fight.",
    can_take=True,
    usable_on=[],
    damage= 3
    )

def spittle_says_thanks(player:Player, npc:NPC, location=None):
    fancy_print("You hand Spittle the coconut through the bars of her cell. \nHer eyes light up with delight and almost become as large as saucers.\n")
    fancy_print(f"""Spittle the Goblin: {generate_text(
        system_prompt="You are an illiterate goblin who is absolutetely mad for coconuts.",
        user_prompt="Here's a coconut! Enjoy!")}""", color="Yellow"
        )
    print()
    fancy_print("She ruffles through her raggy clothing and present you with a little soft lump wrapped in cloth. She barely looks at you while she does this. \nYou presume it is her way of saying thanks.\n")
    return player.add_to_inventory(npc.reward)


spittle_goblin = NPC(
    name="Spittle the Goblin", 
    max_hp=10,
    damage=99,
    description="An old goblin with mud brown skin. She's rattling the bars of her cell with a pewter cup and softly humming to herself.",
    system_prompt="You're a goblin in a jailcell (in a video game). You have poor control over the English language. Somtimes you will respond with poor jokes. Also, you are fond of coconuts.",
    start_message="Gabagooool!",
    clear_stage_key="BJBJ",
    text_color="Yellow",
    text_speed=0.03,
    solve_puzzle=spittle_says_thanks,
    reward=lump_of_clay,
    self_clear=True,
    will_fight=False
)

#CAMPFIRE OBJECTS
def search_the_sand(player, location:Location):
    fancy_print("There is a bunch of sand all around you. You figure it might be a nice place to bury treasure.")
    fancy_print("Do you want to search the sand for buried treasure?")
    player_input = ""
    while player_input not in ["yes", "no"]:
        player_input = input("yes/no: ")
        print()

        if player_input.lower() == "yes":
            fancy_print("You crawl around on the sand for several minutes...\nJust when you think there is nothing to find..\nA portion of ground gives way when you place your weight on it!")
            fancy_print("Do you want to dig and see if it leads anywhere?")
            player_input = ""

            while player_input not in ["yes", "no"]:
                player_input = input("yes/no: ")
                print()
                if player_input.lower() == "yes": 
                    fancy_print("You start digging a hole... \nAfter what seems like half an hour, you hit something hard. You dig out the edges and find an old treasure chest!")
                    print()
                    fancy_print(f"The {old_chest.name} is added to the inspectable items at {location.name}", dim=True)
                    return location.add_item(old_chest)
                
                if player_input.lower() == "no":
                    return False
                else:
                    fancy_print("Invalid answer, please enter 'yes' or 'no'")
                        
            return False
        fancy_print("Invalid answer, please enter 'yes' or 'no'")


sandy_ground = Item(
    name="Sand",
    description=search_the_sand,
    usable_on=[],
    can_take=False,
    solve_puzzle=None
)


pirate_cutlass = Weapon(
    name="Pirate Cutlass",
    description="It's an old cutlass found in a pirate treasure chest! The blade is not very sharp, but it's set with beautiful ruby gemstones.",
    can_take=True,
    usable_on=[],
    damage= 6
    )


old_chest = Item(
    name="Old Chest",
    description="It's a very large wooden chest with a rusty lock. It looks really old. You try to open it, but it's locked shut.",
    usable_on=[],
    can_take=False,
    solve_puzzle=pirate_cutlass
)


coconut = UsableItem(
    name="Coconut",
    description="It's a nice round coconut.",
    solve_puzzle=None,
    usable_on=[spittle_goblin],
    can_take=True
)


def search_palm_tree(player:Player, location:Location):
    fancy_print("You see three beautiful palm trees standing closely together. One contains a number of coconuts at the very top.")
    fancy_print("Do you want to try to climb the tree and retrieve one?")
    player_input = ""

    while player_input not in ["yes", "no"]:
        player_input = input("yes/no: ")
        print()

        if player_input.lower() == "yes":
            fancy_print("You wrap your arms and legs around the tree and try to wiggle your way up. \nHalfway there your arm catches a wood splinter and you let go. \nYou fall flat on your ass in the sand. It kinda hurts.\n")
            fancy_print("You take 2 damage.", dim=True)
            player.hp -= 2
            player.health_bar.update()
            player.health_bar.draw()
            print()

            fancy_print("Do you want to give it another try?")
            player_input = ""

            while player_input not in ["yes", "no"]:
                player_input = input("yes/no: ")
                print()

                if player_input.lower() == "yes":
                    fancy_print("You try a different approach by using two palmtrees to climb. You slowly shimmy you way up the trees until you can almost reach the coconuts. \nWhen you can almost reach them, you give the tree a good shake and one of the coconuts falls on the ground!")
                    print()
                    fancy_print(f"The {coconut.name} is added to the inspectable items at {location.name}", dim=True)
                    return location.add_item(coconut)
            
                if player_input.lower() == "no":
                    return False
                else:
                    fancy_print("Invalid answer, please enter 'yes' or 'no'")

        if player_input.lower() == "no":
            return False
        
        else:
            fancy_print("Invalid answer, please enter 'yes' or 'no'")


palm_trees = Item(
    name="Palm Trees",
    description=search_palm_tree,
    usable_on=[],
    can_take=False,
    solve_puzzle=None
)


#DOCKS OBJECTS
skipper = NPC(
    name="Marlowe the Skipper", 
    max_hp=15,
    damage=5,
    description="It looks like this is the person that owns the little skiff at the end of the pier. He has a brawny physique. His weatherbeaten face has leathery skin and around his eyes you can see thin crowfeet lines from years of squinting at the sun. As you come closer you notice he smells heavily like spiced rum.",
    system_prompt="You are a unhelpful pirate who is both a bit hungover and a bit drunk. You ridicule the user and curse at the user in sailor slang.",
    start_message="Aye?",
    clear_stage_key="baconator",
    text_color="BLUE",
    text_speed=0.06,
    solve_puzzle=enter_stage_two_gift,
    reward=enter_stage_two_fight,
    self_clear=False,
    will_fight=True
)


def inspect_bird(player, location:Location):
    playsound("src/sounds/sax-jazz-jazz-sax-riff.mp3", block=False)
    fancy_print("You walk along the yacht slowly. It has an almost mint green color and wooden paneling.")
    fancy_print("It's a magnificent ship. Somehow it kind of makes you think of a smokey jazz bar in 1950s New York. \nYou can barely make out who's playing, but the bebop music sounds electrifying... \nIt could also just be a reference to a seagull of course.")


bird = Item(
    name="Bird (the Boat)",
    description=inspect_bird,
    usable_on=[],
    can_take=False
)

#KITCHEN OBJECTS
cooking_pot = Item(
    name="Cooking Pot",
    description="A large, well-used cooking pot. It’s filled with a bubbling stew that smells delicious.",
    usable_on=[],
    can_take=False,
    solve_puzzle=None
    )

bag_of_spices = Item(
    name="Bag of Spices",
    description="A small burlap bag filled with various aromatic spices. It looks like it could add some serious flavor to any dish.",
    usable_on=[],
    can_take=True,
    solve_puzzle=None
    )

#reward from the cook
bottle_of_rum = UsableItem(
    name="Bottle of Rum",
    description="A bottle of strong, brown, spiced rum. You can drink it straight, out of a coconut or even a pineapple. It makes you want to sing pirate songs.",
    solve_puzzle=skipper.reward,
    usable_on=[skipper],
    can_take=True
)

def use_natural_wine(player:Player, npc:NPC, location=None):

    fancy_print(f"""Leonardo the Cook: Aahhh bellisima! That's exactly what I was craving!
                    How did you know {player.name}? Will you have a drink with me?
                    Some hair of the dog never hurt anybody.""", color="GREEN", speed=0.02)
    player_input = ""
    print()

    while player_input not in ["yes", "no"]:
        player_input = input("yes/no: ")
        print()
        if player_input.lower() == "yes":
            fancy_print("You take a swig of the luke warm natural wine from yesterday... \nIt's not as bad as you thought it would be. You might actually feel a bit better. \n")
            fancy_print("Your health is improved by 1.\n", dim=True)
            player.max_hp += 1
            player.hp += 1
            player.health_bar.update()
            player.health_bar.draw()
            print()
            fancy_print("Leonardo the Cook: Ha-ha! The look on your face. Here I'll give you a bottle of mine in return.\n")
            return player.add_to_inventory(npc.reward)
        
        if player_input.lower() == "no":
            fancy_print("Leonardo the Cook: Allright, suit yourself. It might be a bit too early for alcohol. \nHere, take a bottle of mine in case you change your mind later today.\n")
            return player.add_to_inventory(npc.reward)
        
        else:
            fancy_print("Invalid answer, please enter 'yes' or 'no'")


cook = NPC(
    name="Leonardo the Cook", 
    max_hp=7,
    damage=2,
    description="This must be the chef of this kitchen. He is a short, stout, southern looking man with a large mustache and an evan larger belly. \nHe seems good natured but also really busy cooking up all kinds of dishes at the same time.",
    system_prompt="You are Leornardo, a character in a videogame that is a busy cook. You ask the player for advice on what ingredients to use in y your recipes. Once the player has helped you for 3 times. You exclaim 'Bellissima!' and reward the player with a bottle of rum.",
    start_message="Ciao bella, welcome to the galley.",
    clear_stage_key="bellissima!",
    text_color="GREEN",
    text_speed=0.02,
    solve_puzzle=use_natural_wine,
    reward=bottle_of_rum,
    self_clear=True,
    will_fight=True
)

#Starting item
natural_wine = UsableItem(
    name="Natural wine",
    description="A half finished bottle of juicy natural wine. It feel lukewarm, probably because it was laying in your arms for most of the night.",
    can_take=True,
    solve_puzzle=None,
    usable_on=[cook]
)

#FORTRESS ENTRANCE OBJECTS
def fortress_sign_interaction(player, location:Location):
    fancy_print("You see a small moss covered sign hanging next to the fortress entrance, it's hard to make out what is written on it.")
    fancy_print("Do you want to clear off the moss?")
    player_input = ""
    print()
    while player_input not in ["yes", "no"]:
        player_input = input("yes/no: ")
        if player_input.lower() == "yes":
            return fancy_print("You scrape of several layers of moss and read the sign closely... \nYou make out the letters 'Fort aan het Pampus, sedert 1887'. You wonder what it means.")
        if player_input.lower() == "no":
            return False
        fancy_print("Invalid answer, please enter 'yes' or 'no'")


fortress_sign = Item(
    name="Fortress sign",
    description=fortress_sign_interaction,
    usable_on=[],
    can_take=False
)

guards_helmet = Item(
    name="Guard's Helmet",
    description="A rusty old helmet that once belonged to a fortress guard. It’s too damaged to wear, but it might have some historical value.",
    usable_on=[],
    can_take=True,
    solve_puzzle=None
    )


old_guard = NPC(
    name="Old Guard",
    max_hp=12,
    damage=4,
    description="An elderly guard with a long, white beard and a weathered face. His eyes hold a wealth of knowledge, and he seems to be slightly amused by your presence.",
    system_prompt="You are an old guard of the fortress island Pampus (close to Amsterdam) in a video game. You have extensive historical of knowledge and will share some of this knowledge in short answers. You are semi-aware of being a game character.",
    start_message="Ah, a new adventurer!",
    clear_stage_key="you know who you are",
    text_color="GREEN",
    text_speed=0.04,
    solve_puzzle=None,
    reward=None,
    self_clear=False,
    will_fight=False
)


#HALLWAY OBJECTS
rusty_key = UsableItem(
    name="Rusty Key",
    description="It's a very old key covered in rust. It's big, so it will probably fit a big lock.",
    can_take=True,
    usable_on=[old_chest],
    solve_puzzle=None
)

hallway_portrait = Item(
    name="Portraits",
    description="It's a portrait of two sailors and a captain that all look rather feminine. \nThe description reads: 'Dido, Neel Cuyper and Cpt. A. Bonny'.",
    usable_on=[],
    can_take=False
)


if __name__ == '__main__':
    print("don't run this file you dingus.")