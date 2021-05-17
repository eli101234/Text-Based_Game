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
            name (String): Name of the player/Character
            classType (String): Name of the class
            Inventory (Disctionary): Items the player has 
        
        Side effects:
            Set attributes for name, inventory, hp, power, and defense of the player
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
            
            
    def player_menu(self, monster, m_name):
        """Menu for the player during combat
        
        Args:
            monster (Monster Object): Takes the current monster
            m_name (string):  The name of the monster
        
        Side effects:
            Prints feedback dependning on choice made
        """
        while True:
            decision = input("""What would you like to do?
            1. Attack!
            2. Use an item
            3. Attempt to flea (chance to not work)
            4. Inspect enemy""")
        
            if decision == "1":
                self.attack_monster(monster)
                break
            
            
            elif decision == "2":
                print(f"Here is your inventory:\n{self.inventory}")
                item_choice = input("Which item would you like to use?")
                print("Still working on this! You just skipped a turn!")
                break
            
            
            elif decision == "3":
                run_dice = random.randint(0,100)
                if run_dice <= 30 and m_name != "Aric Bills":
                    monster.hp = "Nigerundayo, Smokeyyyyy" #Means run away in japanese. Jojo meme
                    break
                else: 
                    print("Failed to run away.")
                    break
            
            
            elif decision == "4":
                print(f"""Enemy: {m_name}\nMax hp: {monster.hp}\nPower: {monster.power}\nDefense: {monster.defense}""")
                if m_name == "Aardvark":
                    print("Description: A giant Aardvark! It is clenching its fist, ready to strike.")
                elif m_name == "Vampire":
                    print("Description: A tall man with sharp teeth looking thirstly at you. His skin glistens in the sun.")
                elif m_name == "Werewolf":
                    print("Description: A very hairy, giant beast. Maybe it likes pets?")
                elif m_name == "Dark Boxer":
                    print("Description: He was once a boxer in a past life. Now he roams this realm, finding victims to K.O, permanently.")
                elif m_name == "Loh":
                    print("Description: Former ruler of this realm. His husk holds strong in this dungeon and is ready to strike you.")
                elif m_name == "Titan":
                    print("Description: A gigantic, horrific looking creature. I heard the neck is the weakspot!")
                elif m_name == "Aric Bills":
                    print("Description: The mastermind of this dungeon. You spent the last 5 months gearing for this battle. Lets do this!")
            
            
            else:
                print("Wait, that was not an option. Try again!")
    
    
        
    def attack_monster(self, monster):
        """Does an attack against a monster

        Args:
            monster(Monster object): the monster the player is facing currently
        Side effects:
            Changes monster current hp
            Prints if player damaged monster as well as by how much and left over hp
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