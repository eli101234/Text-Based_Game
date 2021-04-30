"""
"""
import random
import player

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


def battle(player, monster):
    """
    Board function that engages user in battle
    
     Side Effects:
        Calls Monster objects
        Calls Item objects
    """
    while(player.hp > 0 or monster.hp > 0):
        pass
        
    


def healing(item_name, player):
    """
    Function for player healing
    
    Args:
        Heal_item(int/float):
    """

def main():

    #create the board
    new_game = Board()
    
    print("Hello and Welcome to the King of UMCP!")
    #create the player
    name = input("What is your name challenger?")
    hp = input("How much hp will you like?")
    power = input("How strong are you?")
    defense = input("How tanky are you?")
    p1 = player.Player(name, hp, power, defense)
    print(f"Get ready {name}!")
    
    
    #create the inventory

    game_status = True

    while (game_status):
        option = input ("""
        1. Roll the dice
        2. Check inventory
        3. Heal yourself
        4. Flee
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
        elif option == "4":
            #A way to quit this game
            print(f"You decide this is all too much for you and flee, ending this journey...")
            exit()
        elif option == "5":
            #Checks the board
            new_game.print_board()
            
        #monster encounter!    
        if(random.randint(1, 100) < 30):
            #encounter a monster (30% chance)!
            print(f"You have encountered a monster! But this feature is still in developement!")
            pass


if __name__ == "__main__":
    main()
    

    
