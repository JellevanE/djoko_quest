from src.utils.utils import fancy_print
from src.characters import Character, Player


class Item:
    def __init__(self, name:str, description:str, usable_on:list, can_take:bool, solve_puzzle=False):
        self.name = name
        self.description = description
        self.usable_on = usable_on
        self.solve_puzzle = solve_puzzle
        self.can_take = can_take
        pass


    def __str__(self) -> str:
        return f"{self.name}"


    def pick_up(self, player:Player):
        if self.name in player.inventory:
            return print(f"{self.name} is already in your inventory.")
        else:
            if self.can_take == True:
                return player.add_to_inventory(self)
            else:
                return fancy_print("It doesn't look like you can take this", dim=True)


    def can_use(self, player:Player, object=None):
        if self not in player.inventory:
            return fancy_print(f"{self.name} is not currently in your inventory.")
        
        if isinstance(self, Weapon):
            return True
        
        else: 
            if object not in self.usable_on:
                if object == Character:
                    return fancy_print(f"{Character.name} does not seem interested.")
                else:
                    return fancy_print("This does not seem like the time or place to use this item.")
            else:
                return True
            

    def inspect(self):
        print(f"You look at {self.name} more closely... \n")
        if isinstance(self.description, str):
            return fancy_print(self.description)
        else:
            return self.description()
    

class Weapon(Item):
    def __init__(self, name, description, usable_on, solve_puzzle, can_take, damage):
        super().__init__(name, description, usable_on, can_take, solve_puzzle)
        self.damage = damage  # Additional attribute for damage

    def __str__(self) -> str:
        return f"{self.name}"

    def use(self, player:Player, object=None):
        # Equip the weapon to the player
        if self.can_use(player, object):
            player.damage += self.damage 
            fancy_print(f"You equip the {self.name}, your damage is improved by {self.damage}!")
            player.remove_from_inventory(self)
            return True
        else:
            return False


class UsableItem(Item):
    def __init__(self, name, description, usable_on, solve_puzzle, can_take):
        super().__init__(name, description, usable_on, can_take, solve_puzzle)

    def use(self, player:Player, object):
        # Use the item to interact with a puzzle or environment
        if self.can_use(player, object):
            player.remove_from_inventory(self)
            return self.solve_puzzle(player, object)  # solve_puzzle could be a method or function
        return False