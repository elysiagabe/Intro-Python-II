import sys
from room import Room
from player import Player
from item import Item

########################################
""" ~~~ GAME SET UP ~~~ """
########################################

# cat = "a cat"
# dog = "dog"

# print(len(cat.split()))
# print(len(dog.split()))

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Declare all the items -- like how they did rooms above
item = {
    "axe": Item("axe", "A double axe with iron blades and a wooden handle"),
    "flashlight": Item("flashlight", "Light the way along the path to find adventure"),
    "key": Item("key", "Skeleton key to an unknown door"),
    "crystal": Item("crystal", "A magical crystal, or so they say"),
    "diary": Item("diary", "A leather-bound diary"),
    "sword": Item("sword", "Brass sword with gems inlaid and a leather hilt"),
    "backpack": Item("backpack", "Waxed canvas backpack"),
    "puppy": Item("puppy", "A tiny, oh-so-cute Maltese puppy"),
    "iphone": Item("iphone", "An outdated iPhone SE with a cracked screen & no service"),
    "sunglasses": Item("sunglasses", "A dark pair of tortoise-shell sunglasses"),
    "suitcase": Item("suitcase", "An ugly old suitcase")
}

# Place items in rooms -- like how they linked rooms...call add_item method
room['outside'].add_item(item['sunglasses'])
room['outside'].add_item(item['flashlight'])
room['foyer'].add_item(item['iphone'])
room['foyer'].add_item(item['key'])
room['foyer'].add_item(item['axe'])
room['overlook'].add_item(item['puppy'])
room['narrow'].add_item(item['diary'])
room['narrow'].add_item(item['backpack'])
room['treasure'].add_item(item['crystal'])
room['treasure'].add_item(item['sword'])
room['treasure'].add_item(item['suitcase'])


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

########################################
""" ~~~ WELCOME SEQUENCE & LOOP ~~~ """
########################################
is_welcoming = True
is_playing = False

print("Welcome to Adventure Quest!\n")

while is_welcoming:
    # Ask if player wants to play game:
    player_start = input("Do you want to go an adventure to find some hidden treasure (Y = yes, N = no)?: ")
    # Player says no
    if player_start.upper() == 'N':
        print("\nThat's too bad. Well, if you change your mind, we'll be around. Tata for now!")
        sys.exit()
    # Player says yes
    elif player_start.upper() == 'Y':
        is_welcoming = False
        is_playing = True
        print("\nYay! That's great news. We're going to be rich. Before we get started, if at anytime you need to go home, enter 'Q' to quit the game. Now let's get started.")
    # Player enters invalid resopnse
    else: 
        print("\nOops! I don't understand. Try again.")

# Prompt player for their name 
player_name = input("\nFirst things first. Tell me, what is your name? ")
# If player wants to quit:
if player_name.upper() == 'Q':
    is_playing = False
    print("\nGoodbye! Hope to see you again some time soon.")
# Collect player's name & instantiate player...by default, player starts in 'outside' room
else: 
    current_player = Player(player_name, room['outside'])
    print("\nIt's nice to meet you,", current_player.name.capitalize(),"! Let's get started.\n", current_player.current_room)

########################################
""" ~~~ MAIN GAME LOOP ~~~ """
########################################

while is_playing: 
    action = input("\nWhat would you like to do next?\nTo travel, enter one of the following: N = north, E = east, S = south, W = west.\nTo view your inventory, enter I.\nTo add or remove items from your inventory, enter either 'take' or 'drop' with the item's name.\n").upper()

    print("action uppercase:", action)

    if len(action.split()) == 1 and action in ['Q', 'I', 'N', 'S', 'E', 'W']:
        # If player wants to quit game...
        if action == 'Q': 
            is_playing = False
            print("\nGoodbye! Hope to see you again some time soon.")
        
        # If player wants to check inventory...
        elif action == 'I':
            if len(current_player.inventory) == 0: 
                print("\nThere's nothing in your inventory right now!")
            else: 
                print("\nHere's what you have in your inventory right now: ", current_player.inventory)
        # Travel N...
        elif action == 'N':
            if (hasattr(current_player.current_room, 'n_to')):
                current_player.current_room = current_player.current_room.n_to
                print(current_player.current_room)
            else: 
                print("\nNothing's there. Let's go somewhere else.")
        # Travel E...
        elif action == 'E':
            if (hasattr(current_player.current_room, 'e_to')):
                current_player.current_room = current_player.current_room.e_to
                print(current_player.current_room)
            else: 
                print("\nYou must not go that way! Try again.")

        elif action == 'S':
            if (hasattr(current_player.current_room, 's_to')):
                current_player.current_room = current_player.current_room.s_to
                print(current_player.current_room)
            else: 
                print("\nDoesn't look like anything's that way.")        

        elif action == 'W':
            if (hasattr(current_player.current_room, 'w_to')):
                print(current_player.current_room.w_to)
            else: 
                print("\nThat's definitely the wrong way. Head in a different direction.")

    elif len(action.split()) == 2 and action.split()[0] in ['TAKE', 'GET', 'DROP']:
        # Define the item player wants to add to their inventory
        item_to_add = action.split()[1].lower()

        # Player wants to take item...
        if action.split()[0] in ['TAKE', 'GET']:
            # Check to make sure item is in the current room's items
            if item_to_add in current_player.current_room.items: 
                if item_to_add == 'iphone':
                    print("\n\n*!~*!~*!~*!~*!~*!~*!~*!~*!~*!~*!~*!~\nOMG you found the treasure! \nThere's a $1 million reward on this ancient lost iPhone for some reason (must be something super top secret on there...). \nCongrats. Let's go splitsies?\n*!~*!~*!~*!~*!~*!~*!~*!~*!~*!~*!~*!~\n\n")
                    sys.exit()
                else: 
                    # If it is, add to player's inventory
                    current_player.on_take(item_to_add)
                    # Also need to remove from current_room
                    current_player.current_room.items.remove(item_to_add)
            else: 
                # If not, tell them to try again
                print("items: ", current_player.current_room.items)
                print("Where do you think you are? That item isn't here! Try again.")

        # Player wants to drop item...
        elif action.split()[0] == 'DROP':
            # Check to make that item is in the player's inventory
            if item_to_add in current_player.inventory:
                # If it is, remove from player's inventory
                current_player.on_drop(item_to_add)
                # Also need to add to current_room items list
                current_player.current_room.items.append(item_to_add)
            # If it's not, let them know they don't have that item
            else:
                print("You don't have that item with you. Try again.")

    else: 
        print("\nThat's not an option. Enter a valid command.")