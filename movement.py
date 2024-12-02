import arcade
from constant import *

class Movement:
    def __init__(self, character, x, y):
        self.character = character
        # Character position
        self.pos_x = x
        self.pos_y = y

        # Track directions currently moving in
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def on_update(self, delta_time):
        pos_change = MOVEMENT_SPEED
        # If moving diagonally, decrease positional change in each direction
        if (self.moving_up or self.moving_down) and (self.moving_left or self.moving_right):
            pos_change = pos_change / 1.414

        if self.moving_up:
            self.pos_y += pos_change
        if self.moving_down:
            self.pos_y -= pos_change
        if self.moving_left:
            self.pos_x -= pos_change
        if self.moving_right:
            self.pos_x += pos_change

class playerMovement(Movement):
    def on_key_press(self, key, modifiers): 
        if key == arcade.key.UP:
            self.moving_up = True
        elif key == arcade.key.DOWN:
            self.moving_down = True
        elif key == arcade.key.LEFT:
            self.moving_left = True
        elif key == arcade.key.RIGHT:
            self.moving_right = True
        elif key == arcade.key.ESCAPE:
            arcade.close_window()            
        else:
            self.character.meele_attack.attack_key(key)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.moving_up = False
        elif key == arcade.key.DOWN:
            self.moving_down = False
        elif key == arcade.key.LEFT:
            self.moving_left = False
        elif key == arcade.key.RIGHT:
            self.moving_right = False