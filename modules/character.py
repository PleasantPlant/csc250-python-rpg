import json
from random import randint


class Character:
    def __init__(self):
        self.name = "player"
        self.str = 0
        self.int = 0
        self.wis = 0
        self.dex = 0
        self.con = 0
        self.cha = 0
        self.race = ""
        self.job = ""
        self.level = 1
        self.maxHP = 0
        self.currentHP = 0
        self.movement = 0
        self.armors = []
        self.weapons = []
        self.minDMG = 1
        self.maxDMG = 6
        self.xp = 0
        self.type = ""
        self.current_weapon = ""
        self.current_armor = ""
        self.tag = "PC"

    def load(self, path):
        with open(path) as f:
            character = json.load(f)
        self.name = character.get("name")
        self.str = character.get("str")
        self.int = character.get("int")
        self.wis = character.get("wis")
        self.dex = character.get("dex")
        self.con = character.get("con")
        self.cha = character.get("cha")
        self.race = character.get("race")
        self.job = character.get("job")
        self.level = character.get("level")
        self.maxHP = character.get("maxHP")
        self.currentHP = character.get("currentHP")
        self.movement = character.get("movement")
        self.xp = character.get("xp")
        self.current_weapon = character.get("current_weapon")
        self.current_armor = character.get("current_armor")

    def set_current_weapon(self):
        pass

    def roll_to_hit(self):
        return randint(1, 20)

    def roll_for_damage(self):
        return randint(self.minDMG, self.maxDMG)

    def get_ac(self):
        return 15

    def get_movement(self):
        pass

    def get_ability_bonuses(self):
        pass

    def modCharsheet(self, param):
        ##match case statement to modify the charactersheet based on passed inputs. add more inputs once other things are fleshed out.
        ##specifically this mods stats, so HP, AC, STR, etc.
        match param:
            case "weapon":
                pass
            case "armor":
                pass

    def update_weapon(self):
        pass

    def update_armor(self):
        pass

    def charSave(self):
        pass
