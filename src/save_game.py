import json
from src.characters import Player
from src.locations import Location

def save_game(player, locations):
    save_data = {
        'player': player.to_dict(),
        'locations': {name: loc.to_dict() for name, loc in locations.items()}
    }
    with open('savegame.json', 'w') as save_file:
        json.dump(save_data, save_file, indent=4)
    print("Game saved successfully.")

def load_game():
    with open('savegame.json', 'r') as save_file:
        save_data = json.load(save_file)

    # Re-create the locations first
    locations = {name: Location.from_dict(data) for name, data in save_data['locations'].items()}

    # Need to re-establish the accessible locations relationship
    for name, location in locations.items():
        location.accessible_locations = [locations[loc_name] for loc_name in save_data['locations'][name]['accessible_locations']]

    # Re-create the player
    player = Player.from_dict(save_data['player'], locations)

    return player, locations
