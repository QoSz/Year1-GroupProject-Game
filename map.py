# ######################################################################################################## #
# Importing from modules
from items import *
from evidence import *

# ######################################################################################################## #
room_lobby = {
    "name": "The Lobby",

    "description":
    """You are in the grand lobby of Buckingham Palace, a crystal chandelier looms high above you, attached to the ceiling.
There is an exquisite wooden staircase to the east. You're told that it leads to the master bedroom.
There is a massive doorway to the south that leads to the main living room.
There is also another doorway to the north that leads to the dining room. """,

    "exits": {"south": "Living", "east": "Bedroom", "north": "Dining"},

    "items": [item_torch],

    "light": "light",

    "dna": ["Prince Charles", "Grant Harrold", "Mark Lane", "Adam Sandler", "Rob Lowe", "Lyndsy Lohan", "George Wood", "Jake Duffner", "Amelia Riley", "Vicky Ray", "Samuel Dane", "Xav Nicko"],

    "evidence": []
}

# ######################################################################################################## #

room_kitchen = {
    "name": "The Kitchen",  

    "description":
    """You are standing on the marble floor tiles of the kitchen. There are many shiny appliances around you.
The walls and ceiling are lined with cooking instruments, such as knives, pots, pans and various utensils.
There is a small doorway to the east that leads to the garden.
There is a long corridor to the north of the kitchen which leads to the servant's quarters.
Behind you, to the south, is the original doorway you entered, that leads back to the dining room.""",

    "exits":  {"east": "Garden", "north": "Servants", "south": "Dining"},

    "items": [],

    "light": "light",

    "dna": ["Grant Harrold", "Amelia Riley"],

    "evidence": [evidence_knife]
}

# ######################################################################################################## #

room_servants = {
    "name": "The Servant's Quarters",

    "description":
    """You are in a small room which contains a neatly made double bed, a small table with a single wooden chair beside it.
Next to the bed is a chest of drawers and a wardrobe full of various clothes.
There is a an attached room that has a shower, sink and toilet in. One of the servants tells you, that all the servant's rooms look the same.
There is a plain wooden door to the south, which takes you back to the kitchen. """,

    "exits": {"south": "Kitchen"},

    "items": [],

    "light": "light",

    "dna": ["Grant Harrold", "Amelia Riley", "Rob Lowe", "Mark Lane", "George Wood"],

    "evidence": [evidence_wine]
}

# ######################################################################################################## #

room_diningroom = {
    "name": "The Dining Room",

    "description":
    """You are standing at the end of a magnificent mahogany dining table. Plates, knives, forks, spoons and glasses
are all lined up atop the dining table, with not a single item out of place. There are 20 mahogany chairs placed
all around the table, each evenly spaced apart from one another. Many paintings and oranments line the walls, all extremely valuable. A freshly
polished suit of armour holding a large joust, stands tall in the corner of the room.
To the north are two large wooden doors that lead to the kitchen.
To the south, is another large door that leads back to the lobby.""",

    "exits": {"north": "Kitchen", "south": "Lobby"},

    "items": [],

    "light": "light",

    "dna": ["Prince Charles", "Grant Harrold", "Adam Sandler", "Rob Lowe", "Lyndsy Lohan", "George Wood", "Jake Duffner", "Amelia Riley", "Vicky Ray", "Samuel Dane", "Xav Nicko"],

    "evidence": [evidence_napkin]
}

# ######################################################################################################## #

room_basement = {
    "name": "The Basement",

    "description":
    """You enter the basement. As you look around you see barrels and crates placed on the floor in neat and orderly rows.
There is a small wooden hatch the the east of the room that leads to the wine cellar.
There is a door to the west that leads back the to Living Room.""",

    "exits": {"west": "Living", "east": "Wine"},

    "items": [],

    "light": "dark",

    "dna": ["Grant Harrold", "Adam Sandler"],

    "evidence":[evidence_letteropener]
}

# ######################################################################################################## #

room_winecellar = {
    "name": "The Wine Cellar",

    "description":
    """You enter the wine cellar, located deep within the basement of Buckingham Palace. It is the biggest wine cellar you've
ever encountered, with hundreds of bottles lining the walls, all of varying ages and flavours.
There is the small wooden hatch to the west of you, leading back to the basement.""",

    "exits": {"west": "Basement"},

    "items": [],

    "light": "dark",

    "dna": ["Grant Harrold", "Adam Sandler"],

    "evidence":[evidence_corkscrew]
}

# ######################################################################################################## #

room_bedroom = {
    "name": "The Master Bedroom",

    "description":
    """You enter the master bedroom. Infront of you is an elegant, silk canopy bed. Beside the bed is a small bedside table with a
small table lamp and a book. There is a massive wardrobe containing all elegant dresses.
There is a door to the east of the bedroom which leads to the en-suite bathroom.
There is also a door to the west that leads back to the lobby.""",

    "exits": {"west": "Lobby", "east": "Bathroom"},

    "items": [],

    "light": "light",

    "dna": ["Grant Harrold", "Amelia Riley"],

    "evidence":[evidence_gun, evidence_necklace]
}

# ######################################################################################################## #

room_garden = {
    "name": "The Garden",

    "description":
    """You enter the luscious garden, full of flowers and trees. There are two hedge designs, in the shape of the king and queen
chess pieces. In the distance there is also a greenhouse containing some vegetables.
There is a staircase to the west that leads back to the kitchen. """,

    "exits": {"west": "Kitchen"},

    "items": [],

    "light": "light",

    "dna": [],

    "evidence":[evidence_shears]
}

# ######################################################################################################## #

room_bathroom = {
    "name": "The Bathroom",

    "description":
    """You enter the en-suite bathroom of the mater bedroom. There is a massive mirror on the wall, with a marble sink below it.
There is a toilet in one corner, with a shower and bath on the other side of the room.
There is a doorway to the west that leads back to the bedroom.""",

    "exits": {"west": "Bedroom"},

    "items": [],

    "light": "light",

    "dna": [],

    "evidence":[evidence_toothbrush]
}

# ######################################################################################################## #

room_livingroom = {
    "name": "The Living Room",

    "description":
    """You enter the living room. The centerpiece of the living room is an ornate fireplace, with many ornaments atop
the mantelpiece. There are many couches and arm chairs spread among the room. There is also a oak wood coffee table in between the couches and arm chairs.
Behind you, to the north, is the doorway leading back to the lobby.
To the east is a small wooden doorway that leads to the basement""",

    "exits": {"north": "Lobby", "east": "Basement"},

    "items": [],

    "light": "light",

    "dna": ["Prince Charles", "Grant Harrold", "Adam Sandler", "Rob Lowe", "Lyndsy Lohan", "George Wood", "Jake Duffner", "Amelia Riley", "Vicky Ray", "Samuel Dane", "Xav Nicko"],

    "evidence":[evidence_newspaper]
}

# ######################################################################################################## #

rooms = {
    "Lobby": room_lobby,
    "Kitchen": room_kitchen,
    "Servants": room_servants,
    "Dining": room_diningroom,
    "Basement": room_basement,
    "Wine": room_winecellar,
    "Bedroom": room_bedroom,
    "Garden": room_garden,
    "Bathroom": room_bathroom,
    "Living": room_livingroom,
}

# ######################################################################################################## #
