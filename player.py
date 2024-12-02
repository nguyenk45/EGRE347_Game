import arcade
from constant import *
from movement import *
from attack import Meele
from pickup import item_collision
from character import Character

class Player(Character):
    def __init__(self, spritesheet):
        super().__init__(spritesheet, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.health = 100
        self.movement = playerMovement(self, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.meele_attack = Meele(self)
        self.item_collision = item_collision(self)
        
        self.game_window = None
    
    def on_key_press(self, key, modifiers):
        self.movement.on_key_press(key, modifiers)
        if key == arcade.key.E:
            self.item_collision.on_key_press(key)
            
    def on_key_release(self, key, modifiers):
        self.movement.on_key_release(key, modifiers)