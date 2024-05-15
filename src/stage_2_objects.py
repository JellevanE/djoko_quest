from __future__ import annotations
from src.characters import Character, NPC, Player
from src.locations import Location
from src.items import Item, UsableItem, Weapon
from src.utils.utils import fancy_print
from playsound import playsound
from scenes_text.stage_two_text import moomin_troll, bear_visual, venus_milo


### set special stage functions
def clear_stage_one():
    fancy_print("You completed the first stage, which means you can open your first present..")
    return True


## Standard Item
acne_scarf = UsableItem(
    name="Acne Studios Scarf",
    description="",
    can_take=True,
    solve_puzzle=False,
    usable_on=[]
)


## Witch's shop
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


#The Pub
bear = NPC(
    name="Fuzzy Bear",
    description=f"It's a large brown bear wearing a very sporty cap. It looks at you with hungry eyes. \nYou're not sure if it's supposed to be menacing or seductive.\n\n{bear_visual}",
    system_prompt= "Your safety word is 'honeypot'. You are a bear in a video game that is a bit horny and looking for affection. You very much want the player to flirt with you. Once you feel appropriately seduced you return ONLY your safety word, make sure it is spelled the same and don't add any other text. Only say it after a couple of interactions if you are absolutely sure the player is flirting with you.",
    start_message= "Hiya ;) Don't you look like a tasty little dish.",
    clear_stage_key= 'honeypot',
    solve_puzzle= clear_stage_one, #FILLER
    reward= clear_stage_one,
    text_color= "BLUE",
    text_speed=0.06,
    max_hp = 5,
    damage = 8,
    self_clear=True,
    will_fight=False
)

sven = NPC(
    name="Sven the Bard",
    description=".",
    system_prompt= "You are a Swedish bard. Your answers are in the form of rhymes and lyrics that contain many Swedish words. You are fond of the moomins.",
    start_message= "Well met.",
    clear_stage_key= 'älskling',
    solve_puzzle= clear_stage_one, #FILLER
    reward= clear_stage_one,
    text_color= "CYAN",
    text_speed=0.03,
    max_hp = 10,
    damage = 4,
    self_clear=False,
    will_fight=True
)

francoise = NPC(
    name="Françoise the Ranger",
    description=".",
    system_prompt= ".",
    start_message= "Well met.",
    clear_stage_key= 'älskling',
    solve_puzzle= clear_stage_one, #FILLER
    reward= clear_stage_one,
    text_color= "CYAN",
    text_speed=0.03,
    max_hp = 10,
    damage = 4,
    self_clear=False,
    will_fight=True
)

#The Market
statue = Item(
    name="Statue",
    description=f"It's a gorgeous classical statue, but it looks a bit out of place on this market... {venus_milo}",
    usable_on=[],
    can_take=False,
    solve_puzzle=None
)




def take_stroopwafels(player, location:Location):
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
                    fancy_print(f"The is added to the inspectable items at {location.name}", dim=True)
                    return location.add_item()
                
                if player_input.lower() == "no":
                    return False
                else:
                    fancy_print("Invalid answer, please enter 'yes' or 'no'")
                        
            return False
        fancy_print("Invalid answer, please enter 'yes' or 'no'")


stroopwafels = UsableItem(
    name="Stroopwafel",
    description=take_stroopwafels,
    solve_puzzle=None,
    usable_on=[francoise],
    can_take=True
)