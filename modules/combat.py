from random import choice as randchoice


class Combat:
    def __init__(self, player_characters, npcs, player_ply_function, endgame_function):
        self.player_characters = player_characters
        self.npcs = npcs
        self.interactive_mode = True
        self.party_xp = 0
        self.partyWin = False
        self.ordered_combatants = 0
        self.player_ply_function = player_ply_function
        self.endgame_function = endgame_function
        self.combatOver = False

    def are_characters_dead(self, characters):
        dead_characters = []
        for character in characters:
            if character.currentHP <= 0:
                dead_characters.append(character)
        if len(characters) == len(dead_characters):
            return True
        else:
            return False

    def is_combat_over(self):
        if self.are_characters_dead(self.player_characters):
            return True
        elif self.are_characters_dead(self.npcs):
            return True
        else:
            return False

    def end_combat(self):
        if not self.are_characters_dead(self.player_characters):
            self.partyWin = True
        return self.partyWin

    def ply(self, attacker, defender):
        hitRoll = attacker.roll_to_hit()
        hit = False
        if hitRoll > defender.get_ac():
            damageRoll = attacker.roll_for_damage()
            defender.currentHP -= damageRoll
            hit = True

        return {
            "hit": hit,
            "hit_roll": hitRoll,
            "defender_hp": defender.currentHP,
            "attacker_name": attacker.name,
            "attacker_tag": attacker.tag,
            "defender_name": defender.name,
            "defender_tag": defender.tag,
        }

    def print_stats(self):
        self.stats = ""

    def turn(self):
        for attacker in self.ordered_combatants:
            if attacker.tag == "PC":
                defender = randchoice(self.npcs)
            else:
                defender = randchoice(self.player_characters)

            result = self.ply(attacker, defender)
            self.player_ply_function(result)
            if result["defender_hp"] <= 0:
                self.ordered_combatants.remove(defender)
                if defender.tag == "PC":
                    self.player_characters.remove(defender)
                else:
                    self.npcs.remove(defender)

    def start(self):
        self.ordered_combatants = self.player_characters + self.npcs
        while not self.combatOver:
            winner = self.turn()
            self.combatOver = self.is_combat_over()
        if self.end_combat():
            self.endgame_function("The Party Won!")
        else:
            self.endgame_function("The party lost.")
