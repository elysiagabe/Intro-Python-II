# Write a class to hold player information, e.g. what room they are in
# currently.
class Player: 
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def on_take(self, item):
        self.inventory.append(item)
        print("You have picked up the ",{item})

    def on_drop(self, item):
        self.inventory.remove(item)
        print("You have dropped the ",{item})

    def __str__(self):
        return f"Player Name: {self.name}, Current Room: {self.current_room}"