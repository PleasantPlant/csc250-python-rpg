class Character:
    def __init__(self):
        self.name = "player"
        self.strength = 0
        self.intel = 0
        self.wisdom = 0
        self.dexterity = 0
        self.constitution = 0
        self.charisma = 0
        self.race = ""
        self.job = ""
        self.level = 1
        self.maxHP = 0
        self.currentHP = 0
        self.movement = 0
        self.armors = []
        self.weapons = []
        self.xp = 0
        self.type = ""
        self.current_weapon = ""
        self.current_armor = ""

    def set_current_weapon(self):
        pass

    def roll_to_hit(self):
        pass

    def roll_for_damage(self):
        pass

    def get_ac(self):
        pass

    def get_movement(self):
        pass

    def get_ability_bonuses(self):
        pass

    def modCharsheet(self):
        ##match case statement to modify the charactersheet based on passed inputs. add more inputs once other things are fleshed out.
        ##specifically this mods stats, so HP, AC, STR, etc.
        pass
