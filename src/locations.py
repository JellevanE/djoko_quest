from __future__ import annotations
from typing import TypedDict
from src.characters import NPC, Character
from src.items import Item


class Location:
    """class to access all objects in a location"""
    def __init__(self, name:str, description:str, interactions:list[NPC], objects:list[Item]) -> None:
        self.name = name
        self.description = description
        self.accessible_locations = []
        self.interactions = interactions
        self.objects = objects      
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
    