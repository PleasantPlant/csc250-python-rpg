from modules.character import Character
from modules.combat import *
from modules.enemies import *
from modules.equipment import *

##how many parameters do we save using the save spell? obviously we save full characters, but what if we had premade characters only?
##story triggers? exp?


# def main():
#     print("Welcome to the csc250 rpg!")
#     print("Would you like to start a new game or load a game?")
#     print("type START to start a game, or LOAD to load the saved file")
#     startMenu()

#     ##this is essentially only going to call imports and execute that code. I don't plan on writing any complex logic here.


# def startMenu():
#     startLoad = input(": ", str)
#     match startLoad.lower():
#         case "start":
#             print("Starting new game...")
#         case "load":
#             print("now loading saved file...")
#         case _:
#             print("invalid command, please re-input the command.")
#             return startMenu()

guy = Character()
guy.load("csc250-python-rpg/actors/Guy.json")
print(guy.name)
