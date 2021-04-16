"""
Create the features of a player
"""

class Player:
    """
    Creates a player for the text-based video game

    Attributes:
        name(String):
        hp(int/float):
        power(int/float):
        defense(int/float):
    """

    def __init__(self, name, hp, power, defense, inventory):
        """
        Initializes a player object

        Args:
            name(String):
            hp(int/float):
            power(int/float):
            defense(int/float):
        """
    
    def attack(self, monster):
        """
        Does an attack against a monster

        Args:
            monster(Monster object): the monster the player is facing currently
        """