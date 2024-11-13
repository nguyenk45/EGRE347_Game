import arcade
from constant import *

class Movement:
    def __init__(self, player):
        self.player = player
        # Square position
        self.rect_x = SCREEN_WIDTH / 2
        self.rect_y = SCREEN_HEIGHT / 2 

        # Track which keys are currently pressed
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False

    def on_key_press(self, key, modifiers): 
        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
        elif key == arcade.key.ESCAPE:
            arcade.close_window()            
        else:
            self.player.meele_attack.attack_key(key)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        if self.up_pressed:
            self.rect_y += MOVEMENT_SPEED
        if self.down_pressed:
            self.rect_y -= MOVEMENT_SPEED
        if self.left_pressed:
            self.rect_x -= MOVEMENT_SPEED
        if self.right_pressed:
            self.rect_x += MOVEMENT_SPEED