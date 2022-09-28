# ######################################################################################################## #

# Importing from Modules / Library
import random
from items import *
from map import rooms

# ######################################################################################################## #

inventory = [item_fingerprint, item_dna, item_magnifyingglass, item_camera]
evidence = []

# Start game at the reception
current_room = rooms["Lobby"]

# ######################################################################################################## #

# Suspicous People
SuspicousPeople = {

    "Prince Charles": [], # Son
    "Grant Harrold": [], # Butler
    "Mark Lane": [], # Gardener
    "Adam Sandler": [],
    "Rob Lowe": [], # Chef
    "Lyndsy Lohan": [],
}

# ######################################################################################################## #

# Innocent People
# People used for different items
InnocentPeople = [

    "George Wood", # Chauffeur
    "Jake Duffner",
    "Amelia Riley", # Maid
    "Vicky Ray",
    "Samuel Dane"
    "Xav Nicko",
]

# ######################################################################################################## #
