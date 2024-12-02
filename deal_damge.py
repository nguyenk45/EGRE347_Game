from constant import *
from attack import *
from enemy import *

class hurt:
    def __init__(self, weapon):
        self.weapon = weapon
        self.damaged = False

    def weapon_contact(self):
        weapon_x = self.weapon.item.x
        weapon_y = self.weapon.item.y

        if (abs(weapon_x) < (RECT_WIDTH + ITEM_WIDTH)/2 and 
            abs(weapon_y) < (RECT_HEIGHT + ITEM_HEIGHT)/2):           
            self.damged = True
            return True 
        
        self.damged = False
        return False

    def damage(self):
        if self.damaged:
            self.enemy.health -= Dagger
            return self.enemy.health
        
    def update(self):
        self.weapon_contact()