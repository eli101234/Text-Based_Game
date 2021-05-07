"""
Create the features of a player
"""
import random

class Player:
    """
    Creates a player for the text-based video game

    Attributes:
        name(String): Name of the player
        hp(int/float): How much hit points a character can take
        power(int/float): How damage a player can inflict
        defense(int/float): How much damage a player can nullify
    """

    def __init__(self, name, classType, inventory = None):
        """Initializes a player object

        Args:
            name(String):
            hp(int/float):
            power(int/float):
            defense(int/float):
        """
        self.name = name
        self.inventory = inventory
        choice = True
        #Should we randomize the hp/power/Def?
        while(choice == True):
            if classType.lower() == "assassin":
                #less hp/armor, more damage
                self.hp = 20
                self.power = 20
                self.defense = 20
                choice = False
            elif classType.lower() == "tank":
                #less damage, more hp/armor
                self.hp = 50
                self.power = 5
                self.defense = 40
                choice = False
            elif classType.lower() == "warrior":
                #all around
                self.hp = 30
                self.power = 10
                self.defense = 30
                choice = False
            elif classType.lower() == "bruiser":
                #more hp, more damage, less defense
                self.hp = 40
                self.power = 15
                self.defense = 20
                choice = False
            else: print("Looks like I do not have this class, try again!")
    
    def attack_monster(self, monster):
        """Does an attack against a monster

        Args:
            monster(Monster object): the monster the player is facing currently
            weapon (string): What kind of weapon is in use for this combat
        """
        dice = random.randint(self.power - 5, self.power + 5)
        hit = monster.hp - abs((dice - monster.defense))
        monster.hp = hit
        print(f"{self.name} did {dice - monster.defense} damage to the monster!")
        print(f"The monster has {monster.hp} hp left!")
        
        
        
        


        