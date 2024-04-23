from create_player import create_player
from stages import enter_stage_one

#start here

#title
#start, quit, load?
def game_loop():
    #start
    player = create_player()

    #start stage 1
    enter_stage_one(player=player)

game_loop()