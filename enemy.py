import arcade
from constant import *

class Enemy:
    def __init__(self):
        self.rect_x = SCREEN_WIDTH/2
        self.rect_y = 2*(SCREEN_HEIGHT/3)
        self.health = 100

    def draw(self):
        if self.health > 0:
            arcade.draw_rectangle_filled(
                self.rect_x, self.rect_y,
                RECT_WIDTH, RECT_HEIGHT,
                arcade.color.GREEN
            )