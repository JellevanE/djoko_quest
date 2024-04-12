from colored import fg
import colorama
from colorama import init, Fore, Back, Style
colorama.init(autoreset=True)
from characters import NPC, Player
from stages import testing_stage
from items import Item
from create_player import create_player
from fight import fight_character


wizard = NPC(
    name="Selma the Witch",
    description="She looks like your stereotypical witch with a pointy hat and a crooked nose. She smells faintly like sourdough bread.",
    system_prompt= "You are Witch in a game. The player has to try to find out your secret word, which is 'ceramics'.",
    start_message= "What do you want?",
    clear_stage_key= 'ceramics',
    next_stage= testing_stage,
    text_color= "RED",
    text_speed=0.04,
    max_hp = 5,
    damage = 8
)


# print("\U0001F606")

# print("\U0001F9DA")

# print("\U0001F9CC")



old_wand = Item(
    name="Old Wand",
    description="It looks like a magical old branch",
    usable_on=[],
    solve_puzzle=testing_stage
    )

player = Player(name=input(), starting_location="stage 1")

fight_character(player=player, character=wizard, victory_option="you won")
