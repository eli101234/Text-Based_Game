"""
Create the features of a player
"""
import random
from math import floor

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
            
    def player_menu(self, monster):
        """Menu for the player
        """
        decision = input("""What would you like to do?
        1. Attack!
        2. Use an item
        4. Attempt to flea (Will drop an item, chance to not work)
        5. Block
        6. Check the board state
              """)
        if decision == 1:
            self.attack_monster(monster)
        elif decision == 2:
            print(f"Here is your inventory:\n{self.inventory}")
            input("Which item would you like to use?")
    
    
        
    def attack_monster(self, monster):
        """Does an attack against a monster

        Args:
            monster(Monster object): the monster the player is facing currently
            weapon (string): What kind of weapon is in use for this combat
        """
        
        dice = random.randint((self.power - 5), (self.power + 5))
        defense_coef = floor(monster.defense//10)
        hit = dice - defense_coef
        
        if hit <= 0:
            print(f"{self.name} did no damage to the monster!")
            print(f"The monster has {monster.hp} hp left!")
        else: 
            monster.hp = monster.hp - hit
            print(f"{self.name} did {hit} damage to the monster!")
            if monster.hp <= 0:
                print(f"The monster has 0 hp!")
            else:
                print(f"The monster has {monster.hp} hp left!")