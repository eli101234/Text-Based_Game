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
        """Initializes a player object

        Args:
            name(String):
            hp(int/float):
            power(int/float):
            defense(int/float):
        """
        self.name = name
        self.hp = hp
        self.power = power
        self.defense = defense
        self.inventory = inventory
    
    def attack_monster(self, monster):
        """Does an attack against a monster

        Args:
            monster(Monster object): the monster the player is facing currently
        """


        