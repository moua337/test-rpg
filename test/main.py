from rpg.character import Character 
from rpg.weapon import weapon
from rpg.armor import Armor
from rpg.combat import Combat
from utiles.generator import Generator
from rpg.monster import monster

#player1 = Character()

#print(player1.name)

#shortsword = weapon()
#shortsword.load('weapons/sword.json')

#steel = Armor()
#steel.load('armor/steel.json')
def ply_function():
    print()
def end_game_function():
    print("winner")
    print("Game Over")


Captain = Character()
Captain.load = ('character/Captain.json') 

monster = monster()
monster.name = "Skeleton"
monster.hit_p_max = 4
monster


game = Combat([Captain], [monster])



#generator = Generator() 
#new_charactor = generator.character() 






