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
                Mon_type, hp, power, defense = lineSplit[0],lineSplit[1],lineSplit[2],lineSplit[3]

    def attack_player(self, player):
        """
        Method for monster (self) to attack player.
        
        
        """
        
    