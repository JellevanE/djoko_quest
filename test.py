from colored import fg
import colorama
from colorama import init, Fore, Back, Style
colorama.init(autoreset=True)
from characters import Character
from stages import testing_stage


Wizard = Character(
    name="Selma the Witch",
    system_prompt= "You are Witch in a game. The player has to try to find out your secret word, which is 'ceramics'.",
    start_message= "What do you want?",
    clear_stage_key= 'ceramics',
    next_stage= testing_stage,
    text_color= "RED",
    text_speed=0.04
)

# Daan = Character(
#     name="DAAN",
#     system_prompt="You are a video game character. The player/user/human completes the stage when you call your name. Make them convince you to do so. Don't make it too easy",
#     start_message="Hi",
#     clear_stage_key=
# )

Wizard.talk('Juul')