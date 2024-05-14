from __future__ import annotations
from playsound import playsound
from src.characters import Character, NPC, Player
from src.locations import Location
from src.items import Item, UsableItem, Weapon
from src.utils.utils import fancy_print
from stage_2 import enter_stage_two

### set special stage functions
def clear_stage_one():
    fancy_print("You completed the first stage, which means you can open your first present..")
    return True


### set stage items
### set stage NPCs

#CAMPFIRE OBJECTS
def search_the_sand(location:Location):
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


wizard = NPC(
    name="Selma the Witch",
    description="She looks like your stereotypical witch with a pointy hat and a crooked nose. She smells faintly like sourdough bread.",
    system_prompt= "You are Witch in a game. The player has to try to find out your secret word, which is 'ceramics'.",
    start_message= "What do you want?",
    clear_stage_key= 'ceramics',
    solve_puzzle= clear_stage_one,
    reward= clear_stage_one,
    text_color= "RED",
    text_speed=0.04,
    max_hp = 5,
    damage = 8,
    self_clear=False,
    will_fight=True
)


#DOCKS OBJECTS
skipper = NPC(
    name="Marlowe the Skipper", 
    max_hp=15,
    damage=4,
    description="It looks like this is the person that owns the little skiff at the end of the pier. He has a brawny physique. His weatherbeaten face has leathery skin and around his eyes you can see thin crowfeet lines from years of squinting at the sun. As you come closer you notice he smells heavily like spiced rum.",
    system_prompt="You are a unhelpful pirate who is both a bit hungover and a bit drunk. You ridicule the user and curse at the user in sailor slang.",
    start_message="Aye?",
    clear_stage_key="baconator",
    text_color="BLUE",
    text_speed=0.06,
    solve_puzzle=enter_stage_two,
    reward=enter_stage_two,
    self_clear=False,
    will_fight=True
)


def inspect_bird(location:Location):
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


natural_wine = UsableItem(
    name="Natural wine",
    description="A half finished bottle of juicy natural wine. It feel lukewarm, probably because it was laying in your arms for most of the night.",
    can_take=True,
    solve_puzzle=None,
    usable_on=[cook]
)

#FORTRESS ENTRANCE OBJECTS
def fortress_sign_interaction(location:Location):
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

#DUNGEON OBJECTS
lump_of_clay = UsableItem(
    name="Lump of Clay",
    description="It's a lump of clay. Don't know what you expected to find here.",
    can_take=True,
    usable_on=[wizard],
    solve_puzzle=clear_stage_one
)


wooden_club = Weapon(
    name="Wooden Club",
    description="It's a large wooden club. It's quite heavy, but if you give it a good swing it looks like it can do some damage in a fight.",
    can_take=True,
    usable_on=[],
    damage= 3
    )

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
    solve_puzzle=lump_of_clay,
    reward=lump_of_clay,
    self_clear=True,
    will_fight=False
)

if __name__ == '__main__':
    print("don't run this file you dingus.")