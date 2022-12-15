import random

class Combat():

    def __init__(self, player_characters, npcs, player_ply_function, endgame_function):
        #no idea if im doing this right but im trying!!!
        self.player_characters = player_characters
        self.npcs = npcs
        self.interactive_mode = True
        self.party_xp = 0
        self.party_success = False
        self.ordered_combatants = []
        self.player_ply_function = player_ply_function
        self.endgame_function = endgame_function

    def are_characters_dead(self, characters):
        dead_characters = []
        for character in characters:
            if character.hit_p_max <= 0:
                dead_characters.append(character)
        if len(characters) == len(dead_characters):
            return True
        else:
            return False


        pass

    def is_combat_over(self):
        return self.are_characters_dead(self.player_characters) or self.are_characters_dead(self.npcs)
        # if self.are_characters_dead(self.player_characters) or self.are_characters_dead(self.npcs):
        #     return True
        # else:
        #     return False
        
        
    
    def end_combat(self):
        if not self.are_characters_dead(self.player_characters):
            self.party_success = True
        return self.party_success

    def ply(self, attacker, defender):
        hit_roll = attacker.roll_to_hit()
        hit = False

        if hit_roll > defender.get_ac():
            damage_roll = attacker.roll_for_damage()
            defender.hit_p_max = defender.hit_p_max - damage_roll
            hit = True

        return {
            "hit" : hit,
            "hit_roll" : hit_roll,
            "defender_hp" : defender.hit_p_max,
            "attacker_name" : attacker.name,
            "defender_name" : defender.name
        }

        
        
    def print_stats(self):
        pass
    
    def turn(self):
        #1 Loop through everyone so they all get a "ply"
        for attacker in self.ordered_combatants:
            # 2 choose an attacker and a defender
            if attacker  in  self.player_characters:
                attacker_is_player = True
                defender = random.choice(self.npcs) 
            else:
                attacker_is_player = False
                defender = random.choice(self.player_characters)

            # 3 Ply
            result = self.ply(attacker, defender)
            # 4 Return results to client
            self.player_ply_function(result)

            # 5 Determine is the defender needs to be removed from the all combatants list
            if  result["defender_hp"] <= 0:
                self.ordered_combatants.remove(defender)
                if attacker_is_player:
                    self.npcs.remove(defender)
                else:
                    self.player_characters.remove(defender)

            # 6 Determine if the game is over
            if self.is_combat_over():
                self.end_combat()


    def start(self):
        self.ordered_combatants = self.player_characters  +   self.npcs
        while not self.is_combat_over():
            winner = self.turn()

        self.endgame_function(winner)
        