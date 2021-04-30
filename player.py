"""
Create the features of a player
"""

class Player:
    """
    Creates a player for the text-based video game

    Attributes:
        name(String): Name of the player
        hp(int/float): How much hit points a character can take
        power(int/float): How damage a player can inflict
        defense(int/float): How much damage a player can nullify
    """

    def __init__(self, name, hp, power, defense, inventory = None):
        """Initializes a player object

        Args:
            name(String):
            hp(int/float):
            power(int/float):
            defense(int/float):
        """
        #Should we randomize the hp/power/Def?
        self.name = name
        self.hp = hp
        self.power = power
        self.defense = defense
        self.inventory = inventory
    
    def attack_monster(self, monster, weapon = "hands"):
        """Does an attack against a monster

        Args:
            monster(Monster object): the monster the player is facing currently
            weapon (string): What kind of weapon is in use for this combat
        """
        #are we making it so defense nulifies power?
        #Weapons: Hands, knife, sword, Hatchet, Testudo relic?
        #armor: Helmet, vest, testudo blessing
        if weapon == "sword":
            monster.hp = monster.hp - (self.power*2 - self.power*(monster.defense/100))
            return print(f'You unseathed the sword and strike the creature, dealing {(self.power - self.power*(monster.defense/100))} damage to them!')
        elif weapon == "hatchet":
            monster.hp = monster.hp - (self.power*1.5 - self.power*(monster.defense/100))
            return print(f'You take out a hatchet and "axe" them a question, dealing {(self.power - self.power*(monster.defense/100))} damage to them!')
        elif weapon == "knife":
            monster.hp = monster.hp - (self.power*1.2 - self.power*(monster.defense/100))
            return print(f"You take out the knife and slash the creature, dealing {(self.power - self.power*(monster.defense/100))} damage to them!")
        #Bare hands
        else:
            monster.hp = monster.hp - (self.power - self.power*(monster.defense/100))
            return print(f"You curl your hand into a fist and lung at the creature, dealing {(self.power - self.power*(monster.defense/100))} damage to them!")
        
        
        
        


        