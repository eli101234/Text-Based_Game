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
        while True:
            if name in self.inventory:
                hp,power,defense = self.inventory[name]
                item= Item(name,hp,power,defense) #presumes there's an item class to for item objects
                self.inventory.pop(name)
                return item
            else: ## raise error
                print("Not found, type a valid item")
    def show_items(self):
        """ Prints a list of the items in inventory
        
        Side-effects: Prints out a list
        """
        items_list = [self.inventory[key] for key in self.inventory] # list comprehension
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
            found_potion = self.health_inv.pop(random.randint(-4,4))
        else:
            found_potion = self.health_inv.pop()
        if found_potion[2] == '0' and found_potion[3] == '0': #potio
            print(f'You check the monster and find a {found_potion[0]}! It heals you by {found_potion[1]} hp.')
        elif found_potion[2] != 0: # 
            print(f"""
            You check the monster and find a legendary potion!The {found_potion[0]}!
            It heals you by {found_potion[1]} hp and boosts your power by {found_potion[2]} points.""")
        else:# found_potion[3] != 0:
            print(f"""
                  You check the monster and find a legendary potion!
                  The {found_potion[0]}! It heals you by {found_potion[1]} hp and boosts your defense by {found_potion[3]} points.""")
        return found_potion
    def present_item(self):
        if len(self.item_inv) > 10:
            found_item = self.item_inv.pop(random.randint(-5,4))
        else:
            found_item = self.item_inv.pop()
        if found_item[2] != '0': # power item
            print(f'You check the monster and find the {found_item[0]}! It boosts your power by {found_item[2]} points.')
        elif found_item[3] != '0': # defense item
            print(f'You check the monster and find the {found_item[0]}! It boosts your defense by {found_item[3]} points.')
        else: # found_item[2] !=0 and found_item[3]  != 0: # legendary
            print(f'You check the monster and find a legendary item! The {found_item[0]}! It  you boosts your power by {found_item[2]} and boosts your defense by {found_item[3]} points.')
        return found_item
