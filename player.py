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
                self.power = 70
                self.defense = 20
                choice = False
            elif classType.lower() == "tank":
                #less damage, more hp/armor
                self.hp = 50
                self.power = 20
                self.defense = 40
                choice = False
            elif classType.lower() == "warrior":
                #all around
                self.hp = 30
                self.power = 30
                self.defense = 30
                choice = False
            elif classType.lower() == "bruiser":
                #more hp, more damage, less defense
                self.hp = 40
                self.power = 40
                self.defense = 20
                choice = False
            else: print("Looks like I do not have this class, try again!")
    
    def attack_monster(player, monster):
        """Does an attack against a monster

        Args:
            monster(Monster object): the monster the player is facing currently
            weapon (string): What kind of weapon is in use for this combat
        """
        loop = True
        while loop == True:
            choice = input("""What would you like to do?
                1. Fight
                2. Use an item
                3. Block
                4. Attempt to flee
                """)
            
            if(choice == 1):
                dice = random.randint(player.Player.power - 5, player.Player.power + 5)
                monsters.Monsters.monster.hp - (dice - round(monsters.Monsters.monster.defense/100))
                loop = False
            elif(choice == 2):
                #if list is empty
                if not board.inventory:
                    print("Wait, you have no items! Use a different command!")
                else:
                    print(f"Here are your items: {board.inventory.show_items()}")
                    input("Which would you like to choose?")
                    pass
            elif (choice == 3):
                pass
            elif(choice == 4):
                pass
            else: print("Please use one of the four options!")
        
        
        
        
        


        