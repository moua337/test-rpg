import random
class monster():
    def __init__(self):
        self.name = ''
        self.type = ''
        self.ac = ''
        self.hit_point_max = ''
        self.movement = ''
        self.damage_low = ''
        self.damage_high = ''
        self.morale = ''
        self.treasure_type = ''
        self.xp = ''
        self.type = ''
    def roll_to_hit(self):
        return random.randint(3,18)

    def roll_for_damage(self):
        return random.randint(1,4)

    def get_ac(self):
        return 12

    def get_movement(self):
        pass

