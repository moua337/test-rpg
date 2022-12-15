import json


class weapon():
    def __innit__(self):
        self.name = 'no weapon'
        self.price = 0
        self.weight = 0
        self.size = 0
        self.damage_low = 1
        self.damage_high = 2

def load(self,path): 
    with open(path) as f: 
        weapon = json.load(f)

        print(weapon) 
        self.name = weapon.get("name")
        self.price = weapon.get("price")
        self.weight = weapon.get("weight")
        self.size = weapon.get("size")
        self.damage_low = weapon.get("damage")[2]
        self.damage_high = weapon.get("damage")[6] 