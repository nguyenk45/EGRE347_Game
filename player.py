import arcade
from constant import *
from movement import *
from attack import Meele
from pickup import item_collision
from character import Character
from hurt import Ouchy

class Player(Character, Ouchy):
    def __init__(self, spritesheet):
        Character.__init__(self, spritesheet, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        Ouchy.__init__(self)
        
        self.health = 100
        self.movement = playerMovement(self, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.meele_attack = Meele(self)
        self.item_collision = item_collision(self)
        
        self.game_window = None
    
    def update(self, delta_time):
        super().update(delta_time)
        self.update_damage_state()  
    
    def on_key_press(self, key, modifiers):
        self.movement.on_key_press(key, modifiers)
        if key == arcade.key.E:
            self.item_collision.on_key_press(key)
            
    def on_key_release(self, key, modifiers):
        self.movement.on_key_release(key, modifiers)