import arcade
from constant import *

class item:
    def __init__(self, object):
        self.object = object
        self.x = SCREEN_WIDTH/2
        self.y = SCREEN_HEIGHT/3
        self.is_picked = False
        self.Tutorial_Text = True

    def draw(self):
        if not self.is_picked:
            arcade.draw_rectangle_filled(
                self.x,
                self.y,
                ITEM_WIDTH, ITEM_HEIGHT,
                arcade.color.RED
            )

        if self.Tutorial_Text == True: 
            arcade.draw_text(
                "Press E to Pickup/Swap Weapons",
                SCREEN_WIDTH/4.3, SCREEN_HEIGHT/20,
                arcade.color.WHITE,
                20
            )