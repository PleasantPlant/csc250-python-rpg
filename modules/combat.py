class Combat:
    class Combat:
        def __init__(self):
            self.player_characters = "character.py"
            self.npcs = "monster.py"
            self.interactive_mode = True
            self.party_xp = 0
            self.party_success = False
            self.ordered_combatants = 0
            self.player_ply_function = ""
            self.endgame_function = ""

        def characters_dead(self):
            self.players_dead = False
            self.npc_dead = False

        def combat_over(self):
            self.players_dead = True
            self.npc_dead = True

        def end_combat(self):
            self.endgame_function

        def ply(self):
            self.player_ply = True
            self.npc_ply = True

        def print_stats(self):
            self.stats = ""

        def turn(self):
            self.player_turn = ""
            self.npc_turn = ""

        def start(self):
            self.ordered_combatants = self.player_characters + self.npcs
            while not self.combat_over():
                if self.players_dead == True or self.npc_dead == True:
                    pass
