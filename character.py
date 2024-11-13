import arcade
from constant import *
from movement import Movement
from attack import Meele
from pickup import item_collision

class Player:
    def __init__(self):
        self.health = 100
        
        self.movement = Movement(self)
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
        self.meele_attack.update()
        self.item_collision.update(delta_time)
            
    def draw(self):
        # Draw player
        arcade.draw_rectangle_filled(
            self.movement.rect_x, 
            self.movement.rect_y,
            RECT_WIDTH, RECT_HEIGHT,
            arcade.color.BLUE
        )
        
        # Draw attack box
        self.meele_attack.draw()