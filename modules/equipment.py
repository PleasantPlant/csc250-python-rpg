import json


class Armor:
    def __init__(self):
        self.name = "No Armor"
        self.price = 0
        self.weight = 0
        self.ac = 11

    def load(self, path):
        with open(path) as f:
            armor = json.load(f)
        self.name = armor.get("name")
        self.price = armor.get("price")
        self.weight = armor.get("weight")
        self.ac = armor.get("ac")
        self.mod = armor.get("MaxMod")


class Weapon:
    def __init__(self):
        # Size-> 0 is 1-handed, 1 is 2 handed.
        self.name = "No Weapon"
        self.price = 0
        self.weight = 0
        self.size = 0
        self.damage = 0
        self.die = 0
        self.mod = "str"

    def load(self, path):
        with open(path) as f:
            weapon = json.load(f)
        self.name = weapon.get("name")
        self.price = weapon.get("price")
        self.weight = weapon.get("weight")
        self.size = weapon.get("size")
        self.damage = weapon.get("damage")
        self.die = weapon.get["die"]
        self.mod = weapon.get["mod"]
