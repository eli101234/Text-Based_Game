"""
"""
import random
import player
import monsters


class Item:
    """ Attributes--> name"""
    def __init__(self,name,hp):
        self.name = name
        self.hp = float(hp)


class Inventory:
    """An inventory of healing objects available to player"""
    
    """Attributes:
        inventory (dict): A dictionary containing health objects and their associated hp
    """
    
    def __init__(self):
        self.inventory = {}
        with open('items.csv', 'r', encoding = 'utf-8') as f:
            for line in f:
                line = line.strip()
                line = line.split(',')
                name = line[0]
                hp = float(line[1])
                self.inventory[name] = (hp)

    
    def get_item(self,name):
        """ Uses instatiates an item object using info from inventory
        Args:
            name (str): item name
        """
        
        if name in self.inventory:
            hp = self.inventory[name]
            item= Item(name,hp) #presumes there's an item class to for item objects
            return item
        else: ## raise error
            raise KeyError("Item Not found")
    def show_items(self):
        """ Prints a list of the items in inventory
        
        Side-effects: Prints out a list
        """
        items_list = [key for key in self.inventory] # list comprehension
        print(items_list)


class Board:
    """
    The environment in which the user plays the game.
    The board will have 30 tiles to land on.
    Monsters and Items will spawn randomly on each tile
    
    Attributes: 
        filename(str): Path to a csv file that contains text descriptions 
        for each tile.
    """

    def __init__(self):
        """
        Initializes Board object
        
        Side Effects:
            Creates game environment
            30 Tile objects placed here
        """
        self.place = 0
        self.board_state = []
        for i in range(1, 31):
            self.board_state.append("_")
    
    def print_board(self):
        """
        Tile objects are created
        
        Side Effects:
            Attributes: RNG spawns Monsters and Items
        """
        for space in self.board_state:
           print(space, end = " ") 

    def change_board(self, index,  symbol = "x"):
        self.board_state[index] = symbol

def move():
    """
    Will use a Random Number Generator to simulate a dice roll.
    How the player progresses the game
    
    Args:
        Dice(range/int):
    """
    return random.randint(1, 6)


def battle(player, monster, monster_name):
    """
    Board function that engages user in battle
    
     Side Effects:
        
    """
    monster_stats = monster.monster[monster_name]

    current_monster = monsters.Monster(monster_stats[0], monster_stats[1], monster_stats[2])

    print("Battle commence!")

    while(player.hp > 0 or monster.hp > 0):

        player.attack_monster(current_monster)
        
        if monster.hp <= 0:
            break

        monster.attack_player(player)

    if player.hp > 0 and monster.hp <= 0:
        print(f"{player.name} has won the battle vs a {monster_name}!")
        return True
    elif player.hp <= 0 and monster.hp > 0:
        print(f"The {monster_name} has won the battle vs {player.name}!")
        return False
        
        
    


def healing(item_name, player):
    """
    Function for player healing
    
    Args:
        Heal_item(int/float):
    """

def monster_encounter():
    """
    """
    monster_list = ["Aardvark", "Vampire", "Werewolf", "Dark Boxer", "Loh",
    "Titan"]

    choice = random.choices(monster_list, weights = [30, 20, 20, 15, 10, 5])

    monster_name = choice.pop()

    print(f"You have encountered a wild {monster_name}")

    return monster_name

def main():

    #create the board
    new_game = Board()
    monster_game = monsters.Monsters()
    
    print("Hello and Welcome to the King of UMCP!")
    #create the player
    name = input("What is your name challenger?")
    classType = input("""What class would you like?
                      (Assassin, Tank, Warrior, Bruiser)""")
    p1 = player.Player(name,classType)
    print(f"Get ready {name}!")
    inventory = Inventory() # Can be Inventory(file) instead and i wont hardcode item.csv in Inventory
    print(f'Here are your health items:')
    inventory.show_items()

    game_status = True
    while (game_status):
        option = input ("""
        1. Roll the dice
        2. Use inventory
        3. Heal yourself
        4. Flee (Exits the game)
        5. Check the board state
        (ඞ is where you are, X is where you have been, and _ is undiscovered)
        """)
        #maybe have a monster checker after each roll?
        if option == "1":
            roll = move()
            print(f"You rolled a {roll}!")
            new_game.change_board(new_game.place, "X")
            new_game.place += roll
            new_game.change_board(new_game.place, "ඞ")
            
            #monster encounter
            if(random.randint(0, 100) < 50):
            #encounter a monster (50% chance)!
               monster_name = monster_encounter()
               game_status = battle(player, monster_game, monster_name)

            
            
        elif option == "2": # using health items
            item = input("Enter an item: ").lower()
            item = inventory.get_item(item)
            p1.hp = float(p1.hp) + item.hp
            print(f'You gained {item.hp} hp, your health is now {p1.hp}')
            
            
            
            
        elif option == "4":
            #A way to quit this game
            print(f"You decide this is all too much for you and flee, ending this journey...")
            exit()
            
            
            
        elif option == "5":
            #Checks the board
            new_game.print_board()
            
        #monster encounter!    
        


if __name__ == "__main__":
    main()
    

    