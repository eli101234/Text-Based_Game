"""
Class that creates the game board and runs the game
"""
import random
import player
import monsters
import functools
import sys
from time import sleep


class Item:
    """Instantiates an item object for use

        Attributes:
            name (str): item name
            hp (float): item hp
            power (float): item power
            defense (float): item defense
    """
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
    
    def __init__(self,):
        self.inventory = {}

    
    def get_item(self,name):
        """ Uses instatiates an item object using info from inventory
        Args:
            name (str): item name
        """
        
        if name in self.inventory:
            self.hp,self.power,self.defense = self.inventory[name]
            item= Item(name,self.hp,self.power,self.defense) #presumes there's an item class to for item objects
            self.inventory.pop(name)
            return item
        else: ## raise error
           print("we don't have that, try again.")
           item = input('What item?')
           return self.get_item(item)
    def show_items(self):
        """ Prints a list of the items in inventory
        
        Side-effects: Prints out a list
        """
        items_list = [key for key in self.inventory] # list comprehension
        print(items_list)


class GameInventory:
    def __init__(self):
        health_inv = []
        item_inv = []
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
                item_inv.append(list1)
        with open('health_items.txt', 'r', encoding = 'utf-8') as f:
            for line in f:
                line = line.strip()
                line = line.split(',')
                name = line[0]
                hp = line[1]
                power = line[2]
                defense = line[3]
                #defense = line[3]
                list1 = [name,hp,power,defense]
                health_inv.append(list1)
        self.health_inv = health_inv
        self.item_inv = item_inv
    

    def present_potion(self):
        if len(self.health_inv) >8:
            found_potion = self.health_inv.pop(random.randint(-2,2))
        else:
            found_potion = self.health_inv.pop()
        if found_potion[2] == '0' and found_potion[3] == '0': #potio
            print(f'You check the room and find a {found_potion[0]}! It can heal you by {found_potion[1]} hp.')
        elif found_potion[2] != 0: # 
            print(f"""
            You check the room and find a legendary potion!The {found_potion[0]}!
            It can heal you by {found_potion[1]} hp and boosts your power by {found_potion[2]} points.""")
        else:# found_potion[3] != 0:
            print(f"""
                  You check the room and find a legendary potion!
                  The {found_potion[0]}! It can heal you by {found_potion[1]} hp and boosts your defense by {found_potion[3]} points.""")
        return found_potion
    def present_item(self):
        if len(self.item_inv) > 10:
            found_item = self.item_inv.pop(random.randint(-2,2))
        else:
            found_item = self.item_inv.pop()
        if found_item[2] != '0': # power item
            print(f'You check the room and find the {found_item[0]}! It boosts your power by {found_item[2]} points.')
        elif found_item[3] != '0': # defense item
            print(f'You check the room and find the {found_item[0]}! It boosts your defense by {found_item[3]} points.')
        else: # found_item[2] !=0 and found_item[3]  != 0: # legendary
            print(f'You check the room and find a legendary item! The {found_item[0]}! It  you boosts your power by {found_item[2]} and boosts your defense by {found_item[3]} points.')
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
        self.board_state = []
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
        prints messages in a menu-like structure in the console and asks
        for user input
    """

    #getting the monster's stats
    monster_stats = monster.monster[monster_name]

    #creating the monster object
    current_monster = monsters.Monsters(int(monster_stats[0]), int(monster_stats[1]), int(monster_stats[2]))

    #battle
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

    #uses the battle function to also do the final battle
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




def monster_encounter():
    """
    picks the monster for the encounter with certain chances for each

    Side Effects:
        prints the name of the monster to the console

    Returns:
        monster_name(String): the name of the monster the player will encounter
    """

    #list of all the monsters 
    monster_list = ["Aardvark", "Vampire", "Werewolf", "Dark Boxer", "Loh",
    "Titan"]

    #pick a random monster with certain chances
    choice = random.choices(monster_list, weights = [30, 20, 20, 15, 10, 5])

    #obtaining the monster name
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

    #creating the monster's information
    monster_game = monsters.Monsters()

    #creating the inventory
    inventory = Inventory()

    print("Hello and Welcome to the King of UMCP!")

    #create the player
    name = input("What is your name challenger?")
    classType = input("""What class would you like?\n(Assassin, Tank, Warrior, Bruiser):""")
    p1 = player.Player(name,classType,inventory)

    print(f"Get ready {name}!")

    game_inventory = GameInventory()
     # Can be Inventory(file) instead and i wont hardcode item.csv in Inventory
    print(f'Here are your health items:')
    #inventory.show_items()

    game_status = True
    while (game_status):
        option = input ("""
        1. Roll the dice
        2. Use inventory
        3. Flee (Exits the game)
        4. Check the board state
        (ඞ is where you are, X is where you have been, and _ is undiscovered)
        """)
        
        #rolling and monster encounters
        if option == "1":
            roll = move()
            print(f"You rolled a {roll}!")
            new_game.change_board(new_game.place)
            new_game.place += roll
            if random.randint(1,2) == 1:
                new_item = game_inventory.present_item()
                name = new_item[0]
                hp = new_item[1]
                power = new_item[2]
                defense = new_item[3]
                inventory.inventory[name] = (hp,power,defense)
            else: 
                new_item = game_inventory.present_potion()
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
                if(random.randint(0, 100) <50):
                #encounter a monster (50% chance)!
                    monster_name = monster_encounter()
                    game_status = battle(p1, monster_game, monster_name)
                    #item

        #using health items
        elif option == "2":
            if len(inventory.inventory) == 0:
                print('no items!')
            else:
                held_items = [name for name in inventory.inventory]
                print(held_items)
                #print(held_items)
                item = input("Enter an item: ").lower()
                item = inventory.get_item(item)
                p1.hp = float(p1.hp) + float(item.hp)
                p1.power = float(p1.power) + float(item.power)
                p1.defense = float(p1.defense) + float(item.defense)
                print(p1.defense)
                p1.defense = float(p1.defense)
                #print(f'You gained {item.hp} hp, your health is now {p1.hp}')
                print(f'your health is {p1.hp}, your power is {p1.power}, your defense is {p1.defense}')
            
        #end the game   
        elif option == "3":
            print(f"You decide this is all too much for you and flee, ending this journey...")
            exit()

        #print the board     
        elif option == "4":
            new_game.print_board()
        


if __name__ == "__main__":
    main()
    

    