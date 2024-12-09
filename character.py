import arcade
from constant import *
from movement import Movement
from attack import Meele
from pickup import item_collision
from hurt import Ouchy

class Player(Ouchy):
    def __init__(self):
        super().__init__()
        self.movement = Movement(self)
        self.meele_attack = Meele(self)
        self.item_collision = item_collision(self)
        
        self.game_window = None
        self.Alive = True
    
    def on_key_press(self, key, modifiers):
        self.movement.on_key_press(key, modifiers)
        if key == arcade.key.E:
            self.item_collision.on_key_press(key)
            
    def on_key_release(self, key, modifiers):
        self.movement.on_key_release(key, modifiers)
            
    def update(self, delta_time):
        if self.Alive:
            self.movement.on_update(delta_time)
        self.meele_attack.update()
        self.item_collision.update(delta_time)
        self.update_damage_state()
            
    def draw(self):
        #Draw hitbox
        Ouchy.draw(self)
        # Draw player
        arcade.draw_rectangle_filled(
            self.movement.rect_x, 
            self.movement.rect_y,
            RECT_WIDTH, RECT_HEIGHT,
            arcade.color.BLUE if self.health > 0 else arcade.color.RED
        )
        
        # Draw attack box
        self.meele_attack.draw()