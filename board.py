"""
Class that creates the game board and runs the game
"""
import random
import player
import monsters

import sys
from time import sleep

class Item:
    """ Used to instantiate items pulled from inventory"""
    def __init__(self,name,hp,power,defense):
        self.name = name
        self.hp = float(hp)
        self.power = float(power)
        self.defense = float(defense)


class Inventory:
    """An inventory of healing objects available to player"""
    
    """Attributes:
        inventory (dict): A dictionary containing health objects and their associated hp
    """
    
    def __init__(self):
        self.inventory = {}

    
    def get_item(self,name):
        """ Uses instatiates an item object using info from inventory
        Args:
            name (str): item name
        """
        if name in self.inventory:
            hp,power,defense = self.inventory[name]
            item= Item(name,hp,power,defense) #presumes there's an item class to for item objects
            self.inventory.pop(name)
            return item
        else: ## raise error
            raise KeyError("Not found")
    def show_items(self):
        """ Prints a list of the items in inventory
        
        Side-effects: Prints out a list
        """
        items_list = [self.inventory[key] for key in self.inventory] # list comprehension
        print(items_list)
class GameInventory:
    def __init__(self):
        inv = []
        with open('game_items.txt', 'r', encoding = 'utf-8') as f:
            for line in f:
                line = line.strip()
                line = line.split(',')
                name = line[0]
                hp = line[1]
                power = line[2]
                defense = line[3]
                #defense = line[3]
                list1 = [name,hp,power,defense]
                inv.append(list1)
        self.game_inv = inv
    

    def present_item(self):
       # set_0 = ([0])
        found_item = self.game_inv.pop(random.randint(0,23))
        if found_item[1] != 0: # potion or easter egg
            if found_item[1] == 0: # a potion or a elixor
                if found_item[2] != 0: # power elixor
                    print(f'You check the monster and find a {found_item[0]}! It can heal you by {found_item[1]} hp.It also grants you {found_item[2]} power points')
                elif found_item[3]!= 0: # defense elixor
                    print(f'It also grants you {found_item[3]} defense points')
                elif found_item[2] == 0: # potion
                    print(f'You check the monster and find a {found_item[0]}! It can heal you by {found_item[1]} hp.It also grants you {found_item[2]} power points')
                else:
                    print(f'You check the monster and find a {found_item[0]}! It can heal you by {found_item[1]} hp.') # just potion
            elif found_item[2] != 0: # ring
                #print(found_item[0][2])
                if found_item[2] != 20: # a minor or major ring
                    print(f'You check the monster and find a {found_item[0]}! It can boost your power by {found_item[2]} points.')
                else : # special defense ring (special)
                    print(f'You check the monster and find the {found_item[0]}! It can boost your power by {found_item[2]} points.')
            elif found_item[3] != 0: # necklace
                if found_item[3] != 20:  # a minor or major ring
                    print(f'You check the monster and find a {found_item[0]}! It can boost your defense by {found_item[3]} points.')
                else : # special defense ring (special)
                    print(f'You check the monster and find the {found_item[0]}! It can boost your defense by {found_item[3]} points.')
        else:
            print("should be easter egg")
        return found_item


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
        """
        self.place = 0
        self.board_state = []
        for i in range(1, 31):
            self.board_state.append("_")
    
    def print_board(self):
        """
        prints the current game state board
        
        Side Effects:
            prints board to console
        """
        for space in self.board_state:
           print(space, end = " ") 

    def change_board(self, index,  symbol = "x"):
        """
        marks the board where the player was and is currently

        Args:
            index(int): the current index to update
            symbol(character): the character to insert at the current index
        """
        self.board_state[index] = symbol

    def clear_board(self):
        """
        clears the board for a new game

        Side Effects:
            changes the current game board_state and place
        """
        self.place = 0
        for i in range(0, 30):
            self.board_state[i] = "_"

def move():
    """
    Will use a Random Number Generator to simulate a dice roll.
    How the player progresses the game
    
    Returns:
        Int: random integer between 1 and 6
    """
    return random.randint(1, 6)



def battle(player, monster, monster_name):
    """
    Board function that engages user in battle with monster

    Args:
        player(Player Object): the current player object
        monster(Monster Object): the object that holds all the monsters
        monster_name(String): name of the current monster
    
    Side Effects:
        
    """
    monster_stats = monster.monster[monster_name]

    current_monster = monsters.Monsters(int(monster_stats[0]), int(monster_stats[1]), int(monster_stats[2]))

    print("Battle commence!")
    try: 
        while(player.hp > 0 and current_monster.hp > 0):
            player.player_menu(current_monster, monster_name)
            sleep(2.0)
            
            if current_monster.hp <= 0:
                break

            current_monster.attack_player(player)

            sleep(2.0)
       
        if player.hp > 0 and current_monster.hp <= 0:
            print(f"{player.name} has won the battle vs a {monster_name}!")
            return True
        elif player.hp <= 0 and current_monster.hp > 0:
            print(f"The {monster_name} has won the battle vs {player.name}!")
            return False
    except:
        print("Ran away successfully")
        return True
        
        
def final_encounter(player, monster):
    """
    simulates the battle between the player and the final boss

    Args:
        player(Player Object) : the current player object
        monster(Monsters Object): the object that holds all the monsters

    Side Effects:
        Asking user for input by printing to the console

    Returns:
        boolean: returns true if the player will like to play or try again
    """
    print("""Welcome to the final encounter challenger!""")
    sleep(2.00)
    print("Now you must fight Aric, the final boss! Commence!")

    final_battle_result = battle(player, monster, "Aric Bills")

    #win
    if final_battle_result:
        option = input("""
        Congratulations you have won the game! POGGERS!
        Would you like to play again?
        1 to play again or 2 to exit the game!""")
    #Lose
    else:
        option = input("""
        You have died to the final boss! 
        Would you like to try again?
        1 to try again or 2 to exit the game!""")

    if option == "1":
        return True
    else:
        sys.exit()





def healing(item_name, player):
    """
    Function for player healing
    
    Args:
        Heal_item(int/float):
    """

def monster_encounter():
    """
    picks the monster for the encounter with certain chances for each

    Side Effects:
        prints the name of the monster to the console

    Returns:
        monster_name(String): the name of the monster the player will encounter
    """
    monster_list = ["Aardvark", "Vampire", "Werewolf", "Dark Boxer", "Loh",
    "Titan"]

    choice = random.choices(monster_list, weights = [30, 20, 20, 15, 10, 5])

    monster_name = choice.pop()

    print(f"You have encountered a wild {monster_name}")

    return monster_name

def main():
    """
    runs the entire text-based game

    Side Effects:
        simulates the entire game to the console
    """

    #create the board
    new_game = Board()
    monster_game = monsters.Monsters()
    
    print("Hello and Welcome to the King of UMCP!")
    #create the player
    name = input("What is your name challenger?")
    classType = input("""What class would you like?\n(Assassin, Tank, Warrior, Bruiser):""")
    p1 = player.Player(name,classType)
    print(f"Get ready {name}!")
    game_inventory = GameInventory()
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
            new_game.change_board(new_game.place)
            new_game.place += roll
            new_item = game_inventory.present_item()
            name = new_item[0]
            hp = new_item[1]
            power = new_item[2]
            defense = new_item[3]
            inventory.inventory[name] = (hp,power,defense)

            if new_game.place >= 30:
                encounter = final_encounter(p1, monster_game)
                if encounter:
                    new_game.clear_board()
            else:
                new_game.change_board(new_game.place, "ඞ")
            
                #monster encounter
                if(random.randint(0, 50) < 0):
                #encounter a monster (50% chance)!
                    monster_name = monster_encounter()
                    game_status = battle(p1, monster_game, monster_name)
                    

            
            
        elif option == "2": # using health items
            held_items = [name for name in inventory.inventory]
            test = inventory.inventory
            print(test)
            #print(held_items)
            item = input("Enter an item: ").lower()
            item = inventory.get_item(item)
            p1.hp = float(p1.hp) + float(item.hp)
            p1.power = float(p1.power) + float(item.power)
            p1.defense = float(p1.defense) + float(item.defense)
            print(p1.defense)
            p1.defense = float(p1.defense)
            #print(f'You gained {item.hp} hp, your health is now {p1.hp}')
            print(f'your health is now {p1.hp}, your power is {p1.power}, your defense is {p1.defense}')
            
            
            
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
    

    