import arcade
from constant import *
from movement import Movement
from attack import Meele
from pickup import item_collision

class Player(arcade.Sprite):
    def __init__(self, sprite):
        super().__init__(sprite)
        self.image_width = RECT_WIDTH
        self.image_height = RECT_HEIGHT
        self.health = 100
        self.movement = Movement(self)
        self.image_x = self.movement.rect_x
        self.image_y = self.movement.rect_y
        self.meele_attack = Meele(self)
        self.item_collision = item_collision(self)
        
        
        self.game_window = None
    
    def on_key_press(self, key, modifiers):
        self.movement.on_key_press(key, modifiers)
        if key == arcade.key.E:
            self.item_collision.on_key_press(key)
            
    def on_key_release(self, key, modifiers):
        self.movement.on_key_release(key, modifiers)
            
    def update(self, delta_time):
        self.movement.on_update(delta_time)
        self.image_x = self.movement.rect_x
        self.image_y = self.movement.rect_y
        self.meele_attack.update()
        self.item_collision.update(delta_time)
            
    def draw(self):
        # Draw attack box
        self.meele_attack.draw()