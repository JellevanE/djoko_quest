from __future__ import annotations
from src.characters import Character, NPC, Player
from src.locations import Location
from src.items import Item, UsableItem, Weapon
from src.utils.utils import fancy_print
from playsound import playsound

acne_scarf = UsableItem(
    name="Acne Studios Scarf",
    description="",
    can_take=True,
    solve_puzzle=False,
    usable_on=[]
)