from item import Item
# Implement a class to hold room information. This should have name and
# description attributes.
class Room: 
    def __init__(self, name, description):
        self.name = name
        self.desc = description
        self.items = []

    def add_item(self, item):
        print(item)
        self.items.append(item.name) #TODO: decide if I want the whole item object here or if just the name is sufficient

    def __str__(self):
        return f"\nYou are currently located in the {self.name}. {self.desc}\nItems here: {self.items}"
        #TODO: look into parsing out items so it doesn't display brackets and single quote marks