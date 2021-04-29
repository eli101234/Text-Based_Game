"""
"""
import random

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
    name = input("What is your name challenger?")
    print(f"Get ready {name}!")
    
    #create the player
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

        if option == "1":
            roll = move()
            print(f"You rolled a {roll}!")
            new_game.change_board(new_game.place, "X")
            new_game.place += roll
            new_game.change_board(new_game.place, "ඞ")
        elif option == "5":
            new_game.print_board()


if __name__ == "__main__":
    main()
    

    
