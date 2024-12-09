from constant import *
from invincibility import Invincible
from hitbox import draw_hitbox

class Ouchy(Invincible):
    def __init__(self):
        super().__init__()
        self.health = Player_Health
    
    def take_damage(self, amount):
        if not self.invincible:
            self.health -= amount

            print("Player:", self.health)

            self.trigger_invincibility(Time)
            return True
        return False

    def update_damage_state(self):
        self.update_invincibility()

    def draw(self):
        draw_hitbox(100, self.health, 20, 10, 10)