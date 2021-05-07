"""
"""
from math import floor

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
        self.monster = {}
        with open('monster_info.txt', "r", encoding="utf-8") as f:
            for line in f:
                lineSplit = line.split(",")
                self.monster[lineSplit[0]] = lineSplit[1],lineSplit[2],lineSplit[3]

        self.hp = hp
        self.power = power
        self.defense = defense

    def attack_player(self, player):
        """
        Method for monster (self) to attack player.
        
        Args:

        """
        dice = random.randint(self.power - 5, self.power + 5)
        #calculating block 
        defense_coef = player.defense//10
        monster_hit = dice - defense_coef
        #damage calculation
        player.hp - monster_hit

        print(f"The monster did {monster_hit} damage to {player.name}!")
        


        
