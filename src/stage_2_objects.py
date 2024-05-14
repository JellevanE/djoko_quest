from __future__ import annotations
from src.characters import Character, NPC, Player
from src.locations import Location
from src.items import Item, UsableItem, Weapon
from src.utils.utils import fancy_print
from playsound import playsound


### set special stage functions
def clear_stage_one():
    fancy_print("You completed the first stage, which means you can open your first present..")
    return True

acne_scarf = UsableItem(
    name="Acne Studios Scarf",
    description="",
    can_take=True,
    solve_puzzle=False,
    usable_on=[]
)

witch = NPC(
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
