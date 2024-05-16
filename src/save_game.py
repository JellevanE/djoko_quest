import json
from src.characters import Player

import json

def save_game(player: Player, filename="savefile.json"):
    game_data = {
        "player": player.to_dict(),
        # Add other global state as necessary
    }
    with open(filename, 'w') as f:
        json.dump(game_data, f)

def load_game(filename="savefile.json"):
    with open(filename, 'r') as f:
        game_data = json.load(f)

    # Create map of existing objects
    object_map = {}
    solve_puzzle_func_map = {
        "solve_puzzle_function_name": some_puzzle_function  # Populate with actual functions
    }

    # Deserialize objects and populate map
    player_data = game_data["player"]
    player = Player.from_dict(player_data, object_map, solve_puzzle_func_map)

    return player
