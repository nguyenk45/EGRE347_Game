from constant import *

class Invincible:
    def __init__(self):
        self.invincibility = 0
        self.invincible = False
        
    def trigger_invincibility(self, duration):
        self.invincibility = duration
        self.invincible = True
        
    def update_invincibility(self):
        if self.invincibility > 0:
            self.invincibility -= 1
            self.invincible = True
        else:
            self.invincible = False
    
    def check_collision(self, other):
        return (abs(self.movement.rect_x - other.rect_x) < RECT_WIDTH and 
                abs(self.movement.rect_y - other.rect_y) < RECT_HEIGHT and
                other.health > 0)