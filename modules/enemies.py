from random import randint


class Monster:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.ac = 11
        self.maxHP = 0
        self.currentHP = 0
        self.minDmg = 0
        self.maxDmg = 0
        self.morale = ""
        self.movement = 0
        self.xp = 0
        self.tag = "NPC"

    def roll_to_hit(self):
        return randint(1, 20)

    def roll_for_damage(self):
        return randint(self.minDmg, self.maxDmg)

    def get_ac(self):
        return self.ac

    def get_movement(self):
        pass
