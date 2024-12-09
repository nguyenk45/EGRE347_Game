from constant import *
from invincibility import Invincible

class Ouchy(Invincible):
    def __init__(self):
        super().__init__()
        self.health = Player_Health
        self.total_damage_taken = 0
        self.damage_observers = []

    def register_damage_observer(self, observer):
        self.damage_observers.append(observer)

    def notify_damage(self):
        for o in self.damage_observers:
            o.notified_damage()
    
    def take_damage(self, amount):
        if not self.invincible:
            self.health -= amount
            self.total_damage_taken += amount # track damage

            self.trigger_invincibility(Time)
            #Notify damage observers when damage taken
            self.notify_damage()
            return True
        return False

    def update_damage_state(self):
        self.update_invincibility()