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
    description="",
    system_prompt="You are Leornardo, a character in a videogame that is a busy, italian cook. You ask the player for advice on how to finish your recipes. Once the player has helped you for 3 times. You exclaim 'Bellissima!' and reward the player with a bottle of rum.",
    start_message="Ciao bella, welcome to the galley.",
    clear_stage_key="bellissima!",
    text_color="GREEN",
    text_speed=0.03,
    reward=bottle_of_rum,
    self_clear=True,
    will_fight=True
)

if __name__ == '__main__':
    print("don't run this file you dingus.")