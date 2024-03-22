from colored import fg

from characters import Character
from stages import testing_stage


Wizard = Character(
    name="Selma the Witch",
    system_prompt= "You are Witch in a game. The player has to try to find out your secret word, which is 'ceramics'.",
    start_message= "What do you want?",
    clear_stage_key= 'ceramics',
    next_stage= testing_stage,
    text_color= fg('88')
)

Wizard.talk('MadDucky')