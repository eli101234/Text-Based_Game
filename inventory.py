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
        """
        """
        if name in self.inventory:
            hp = self.inventory[name]
            item= Item(name,hp) #presumes there's an item class to for item objects
            return item
        else: ## raise error
            raise KeyError("Not found")
    def show_items(self):
        items_list = [self.inventory[key] for key in self.inventory] # list comprehension
        print(items_list)