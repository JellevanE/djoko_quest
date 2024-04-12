from src.utils import fancy_print
from characters import Character, Player


class Item:
    def __init__(self, name:str, description:str, usable_on:list, solve_puzzle):
        self.name = name
        self.description = description
        self.usable_on = usable_on
        self.solve_puzzle = solve_puzzle
        pass


    def __str__(self) -> str:
        return f"{self.name}"


    def pick_up(self, player:Player):
        if self.name in player.inventory:
            return print(f"{self.name} is already in your inventory.")
        else: 
            return player.add_to_inventory(self.name)


    def can_use(self, player:Player, object):
        if self.name not in player.inventory:
            return fancy_print(f"{self.name} is not currently in your inventory.")
        
        else: 
            if object not in self.usable_on:
                if object == Character:
                    return fancy_print(f"{Character.name} does not seem interested.")
                else:
                    return fancy_print("This does not seem like the time or place to use this item.")
            else:
                return True
            
    def use(self, player:Player, object):
        if self.can_use(player, object) == True:
            return self.solve_puzzle()
        else:
            return None


    def inspect(self):
        print(f"You look at {self.name} more closely...")
        return fancy_print(self.description)