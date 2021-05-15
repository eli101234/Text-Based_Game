"""
Create the features of a player
"""
import random
import board
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
        
        
        while(True):
            if classType.lower() == "assassin":
                #less hp/armor, more damage
                self.hp = 20
                self.power = 20
                self.defense = 20
                break
            elif classType.lower() == "tank":
                #less damage, more hp/armor
                self.hp = 50
                self.power = 5
                self.defense = 40
                break
            elif classType.lower() == "warrior":
                #all around
                self.hp = 30
                self.power = 10
                self.defense = 30
                break
            elif classType.lower() == "bruiser":
                #more hp, more damage, less defense
                self.hp = 40
                self.power = 15
                self.defense = 20
                break
            else: 
                print("Looks like I do not have this class, try again!")
                classType = input("What class would you like: ")
                continue
            
            
    def player_menu(self, monster):
        """Menu for the player during combat
        """
        while True:
            decision = input("""What would you like to do?
            1. Attack!
            2. Use an item
            3. Attempt to flea (Will drop an item, chance to not work)
            4. Inspect enemy
            5. Check the board state""")
        
            if decision == "1":
                self.attack_monster(monster)
                break
            elif decision == "2":
                print(f"Here is your inventory:\n{self.inventory}")
                item_choice = input("Which item would you like to use?")
                print("Still working on this! You just skipped a turn!")
                break
            elif decision == "3":
                pass #Still working on it
            elif decision == "4":
                pass # still workin
            elif decision == "5":
                pass # did board.new_game.print_board(). Breaks the terminal
            else:
                print("Wait, that was not an option! Try again!")
    
    
        
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