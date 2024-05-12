from __future__ import annotations
from src.characters import Character, NPC, Player
from src.locations import Location
from src.items import Item, UsableItem, Weapon
from src.utils.utils import fancy_print



### set special stage functions
def clear_stage_one():
    fancy_print("You completed the first stage, which means you can open your first present..")
    return True


### set stage items
### set stage NPCs

wizard = NPC(
    name="Selma the Witch",
    description="She looks like your stereotypical witch with a pointy hat and a crooked nose. She smells faintly like sourdough bread.",
    system_prompt= "You are Witch in a game. The player has to try to find out your secret word, which is 'ceramics'.",
    start_message= "What do you want?",
    clear_stage_key= 'ceramics',
    reward= clear_stage_one,
    text_color= "RED",
    text_speed=0.04,
    max_hp = 5,
    damage = 8,
    self_clear=False,
    will_fight=True
)


skipper = NPC(
    name="Marlowe the Skipper", 
    max_hp=15,
    damage=4,
    description="It looks like this is the person that owns the little skiff at the end of the pier. He has a brawny physique. His weatherbeaten face has leathery skin and around his eyes you can see thin crowfeet lines from years of squinting at the sun. As you come closer you notice he smells heavily like spiced rum.",
    system_prompt="You are a unhelpful pirate who is both a bit hungover and a bit drunk. You ridicule the user and curse at the user in sailor slang.",
    start_message="Aye?",
    clear_stage_key="Baconator",
    text_color="BLUE",
    text_speed=0.06,
    reward=clear_stage_one,
    self_clear=False,
    will_fight=True
)


#reward from the cook
bottle_of_rum = UsableItem(
    name="Bottle of Rum",
    description="A bottle of strong, brown, spiced rum. You can drink it straight, out of a coconut or even a pineapple. It makes you want to sing pirate songs.",
    solve_puzzle=clear_stage_one,
    usable_on=[skipper],
    can_take=True
)


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
    reward=bottle_of_rum,
    self_clear=True,
    will_fight=True
)


natural_wine = UsableItem(
    name="Natural wine",
    description="A half finished bottle of juicy natural wine. It feel lukewarm, probably because it was laying in your arms for most of the night.",
    can_take=True,
    solve_puzzle=cook.reward,
    usable_on=[cook]
)


def fortress_sign_interaction():
    fancy_print("You see a small moss covered sign hanging next to the fortress entrance, it's hard to make out what is written on it.")
    fancy_print("Do you want to clear off the moss?")
    player_input = ""
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


rusty_key = UsableItem(
    name="Rusty Key",
    description="It's a very old key covered in rust. It's big, so it will probably fit a big lock.",
    can_take=True,
    usable_on=[],
    solve_puzzle=clear_stage_one
)

lump_of_clay = UsableItem(
    name="Lump of Clay",
    description="It's a lump of clay. Don't know what you expected to find here.",
    can_take=True,
    usable_on=[],
    solve_puzzle=clear_stage_one
)

bird = Item(
    name="Bird (the Boat)",
    description="...",
    usable_on=[],
    can_take=False
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
    system_prompt="You're a goblin in a jailcell. You respond with poorly spelled jokes and you are fond of coconuts.",
    start_message="Gabagooool!",
    clear_stage_key="BJBJ",
    text_color="Yellow",
    text_speed=0.03,
    reward=lump_of_clay,
    self_clear=True,
    will_fight=False
)

if __name__ == '__main__':
    print("don't run this file you dingus.")