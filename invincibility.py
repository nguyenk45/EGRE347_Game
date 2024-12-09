from constant import *

class Invincible:
    def __init__(self):
        self.invincibility = 0
        self.invincible = False
        self.dodge_timeout = 0
        
    def trigger_invincibility(self, duration):
        self.invincibility = duration
        self.invincible = True
        
    def update_invincibility(self):
        #Decrement dodge timeout
        if self.dodge_timeout > 0:
            self.dodge_timeout -= 1
            
        if self.invincibility > 0:
            self.invincibility -= 1
            self.invincible = True
        else:
            self.invincible = False
    
    def check_collision(self, other):
        return (abs(self.movement.rect_x - other.rect_x) < RECT_WIDTH/2 and 
                abs(self.movement.rect_y - other.rect_y) < RECT_HEIGHT and
                other.health > 0)