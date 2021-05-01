"""
"""

class Monsters:
    """The random monsters a player can face
    
    Attributes:
        filename(str): Path to a csv file that contains monsters and their
        hp, type, power, defense
    """
    def __init__(self, filepath):
        """Initializes new Monster object.
        
        Side effects:
            sets attributes Mon_type, hp, power, defense
        """
        with open(Monsters.csv, "r", encoding="utf-8") as f:
            for line in f:
                lineSplit = line.split("	")
                self.Mon_type, self.hp, self.power, self.defense = lineSplit[0],lineSplit[1],lineSplit[2],lineSplit[3]

<<<<<<< HEAD
    def attack_player(self, player, defense, armor):
        """ Initializes an attack on player

        """
        
    
