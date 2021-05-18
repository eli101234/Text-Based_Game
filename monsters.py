"""
"""
from math import floor
import random

class Monsters:
    """The random monsters a player can face
    
    Attributes:
        filename(str): Path to a csv file that contains monsters and their
        hp, type, power, defense
    """
    def __init__(self, hp = 0, power = 0, defense = 0):
        """Initializes new Monster object.
        
        Side effects:
            sets attributes Mon_type, hp, power, defense
        """
        self.hp = hp
        self.power = power
        self.defense = defense
        self.monster = {}
        with open('monster_info.txt', "r", encoding="utf-8") as f:
            for line in f:
                lineSplit = line.split(",")
                self.monster[lineSplit[0]] = lineSplit[1],lineSplit[2],lineSplit[3]
    

    def attack_player(self, player):
        """
        Method for monster (self) to attack player.
        
        Args:
            player(Player object)
        Side effect:


        """
        dice = random.randint((self.power - 2), (self.power + 2))
        defense_coef = player.defense//10
        hit = dice - defense_coef
        
        if hit <= 0:
            print(f"The monster did no damage to {player.name}!")
            print(f"The monster has {player.hp} hp left!")
        else: 
            player.hp = player.hp - hit
            print(f"The monster did {hit} damage to {player.name}!")
            if player.hp <= 0:
                print(f"{player.name} has 0 hp!")
            else:
                print(f"{player.name} has {player.hp} hp left!")
        


        
