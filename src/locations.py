from __future__ import annotations
from typing import TypedDict
from src.characters import NPC, Character
from src.items import Item


class Location:
    """class to access all objects in a location"""
    def __init__(self, name:str, description:str, NPCS:list[NPC], items:list[Item]) -> None:
        self.name = name
        self.description = description
        self.accessible_locations = []
        self.NPCS = NPCS
        self.items = items      
        pass

    def __str__(self) -> str:
        return f"{self.name}"
    
    def add_accessible_locations(self, location:Location): #ensure biderectional movement
        if location not in self.accessible_locations:
            self.accessible_locations.append(location)
            location.accessible_locations.append(self)

    def detail(self):
        details = self.__str__()
        details += "\nAccessible Locations:"
        for loc in self.accessible_locations:
            details += f"\n- {loc.name}"
        return details
    
    def add_item(self, item: Item):
        if item not in self.items:
            self.items.append(item)

    def remove_item(self, item:Item):
        if item in self.items:
            self.items.remove(item)
    
    def add_npc(self, npc: NPC):
        if npc not in self.NPCS:
            self.NPCS.append(npc)

    def remove_npc(self, npc:NPC):
        if npc in self.NPCS:
            self.NPCS.remove(npc)
    