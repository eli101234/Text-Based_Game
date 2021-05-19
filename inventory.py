class Item:
    """ Used to instantiate items pulled from inventory"""
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
        if found_item[0][1] != 0: # potion or easter egg
            if found_item[0][1] == 0: # a potion or a elixor
                if found_item[0][2] != 0: # power elixor
                    print(f'You check the monster and find a {found_item[0][0]}! It heals you by {found_item[0][1]} hp.It also grants you {found_item[0][2]} power points')
                elif found_item[0][3]!= 0: # defense elixor
                    print(f'It also grants you {found_item[0][3]} defense points')
                elif found_item[0][2] == 0: # potion
                    print(f'You check the monster and find a {found_item[0][0]}! It heals you by {found_item[0][1]} hp.It also grants you {found_item[0][2]} power points')
                else:
                    print(f'You check the monster and find a {found_item[0][0]}! It heals you by {found_item[0][1]} hp.') # just potion
            elif found_item[0][2] != 0: # ring
                #print(found_item[0][2])
                if found_item[0][2] != 20: # a minor or major ring
                    print(f'You check the monster and find a {found_item[0][0]}! It boosts your power by {found_item[0][2]} points.')
                else : # special defense ring (special)
                    print(f'You check the monster and find the {found_item[0][0]}! It boosts your power by {found_item[0][2]} points.')
            elif found_item[0][3] != 0: # necklace
                if found_item[0][3] != 20:  # a minor or major ring
                    print(f'You check the monster and find a {found_item[0][0]}! It boosts your defense by {found_item[0][3]} points.')
                else : # special defense ring (special)
                    print(f'You check the monster and find the {found_item[0][0]}! It boosts your defense by {found_item[0][3]} points.')
        else:
            print("should be easter egg")
        return found_item
