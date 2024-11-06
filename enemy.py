import arcade
import math
import sys
from constant import *

class Enemy:
    def __init__(self):

        self.rect_x = SCREEN_WIDTH / 2
        self.rect_y = SCREEN_HEIGHT / 2
        self.health = 100

    def on_draw(self): #Render the screen
        self.clear()
        
        # Draw the rectangle (green)
        arcade.draw_rectangle_filled(
            self.rect_x, self.rect_y,
            RECT_WIDTH, RECT_HEIGHT,
            arcade.color.GREEN
        )
    
