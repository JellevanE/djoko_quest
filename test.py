# from src.characters import NPC, Player
# from src.items import Item, Weapon, UsableItem
# from src.utils.create_player import create_player
# from src.fight import fight_character
# from src.locations import Location
# from src.stage_1_objects import cook, skipper, bottle_of_rum, spittle_goblin, skipper, natural_wine
# #from playsound import playsound
# from src.stage_1_objects import inspect_bird
# from src.player_options import use_item_on
# from src.stage_2_objects import bear, sven, francoise, rabbit_leg
# from stage_2 import enter_stage_two_gift, enter_stage_two_fight, enter_stage_two

# def testing_stage(player:Player):
#     return print(f"you are granted access and can enter the next stage, {player.name}!")

# wizard = NPC(
#     name="Selma the Witch",
#     description="She looks like your stereotypical witch with a pointy hat and a crooked nose. She smells faintly like sourdough bread.",
#     system_prompt= "You are Witch in a game. The player has to try to find out your secret word, which is 'ceramics'.",
#     start_message= "What do you want?",
#     clear_stage_key= 'ceramics',
#     reward= testing_stage,
#     solve_puzzle= testing_stage,
#     text_color= "RED",
#     text_speed=0.04,
#     max_hp = 5,
#     damage = 8,
#     self_clear=False,
#     will_fight=True
# )



# old_wand = Weapon(
#     name="Old Wand",
#     description="It looks like a magical old branch",
#     can_take=True,
#     usable_on=[wizard],
#     damage= 10
#     )


# player = Player(name=input(), starting_location="stage 1")

# player.add_to_inventory(rabbit_leg)

# enter_stage_two(player=player)

# player.add_to_inventory(bottle_of_rum)

# player.add_to_inventory(natural_wine)

# use_item_on(player=player, location=None, item=natural_wine)

# # fight_character(player=player, character=cook)

#francoise.talk(player=player)


#inspect_bird(location=None)