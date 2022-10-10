from modules.character import Character
from random import randint, choice as randchoice


class charGen:
    def __init__(self) -> None:
        pass

    def character(self):
        pass

    def generate(self):
        races = ("Human", "Elf", "Dwarf", "Lizard", "Alien")
        classes = ("Knight", "Ranger", "Mage")
        char = Character()
        stats = []
        race = randchoice(races)
        job = randchoice(classes)
        for i in range(6):
            stats.append(randint(3, 19))

        stats.sort(reverse=True)

        match job:
            case "Knight":
                char.job = job
                char.str = stats[0]
                char.int = stats[4]
                char.wis = stats[3]
                char.dex = stats[2]
                char.con = stats[1]
                char.cha = stats[5]
                char.maxHP = 12
            case "Ranger":
                char.job = job
                char.dex = stats[0]
                char.int = stats[3]
                char.wis = stats[1]
                char.str = stats[4]
                char.con = stats[2]
                char.cha = stats[5]
                char.maxHP = 8
            case "Mage":
                char.job = job
                char.str = stats[5]
                char.int = stats[0]
                char.wis = stats[1]
                char.dex = stats[3]
                char.con = stats[4]
                char.cha = stats[2]
                char.maxHP = 6
        char.race = race
        char.level = 1
        char.movement = 30
