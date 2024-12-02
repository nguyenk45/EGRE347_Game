from constant import *
from invincibility import Invincible

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