
class Character():
    def __init__(self):
        self.name = 'player'
        self.strength = '0'
        self.intelligence = '0'
        self.wisdom = '0'
        self.dexterity = '0'
        self.consitution = '0'
        self.charisma = '0'
        self.race = ''
        self.p_class = ''
        self.level = ''
        self.hit_point_max = ''
        self.movement = ''
        self.armors = []
        self.weapons = []
        self.xp = ''
        self.type = ''
        self.current_weapon = ''
        self.current_armor = ''

        def load_from_json(self, path):
            with open(path) as f:
                character = json.load(f)
                





    def set_current_weapon(self):
        pass





