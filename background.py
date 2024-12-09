import arcade
from constant import *

class Background(arcade.Sprite):
    def __init__(self, images):
        super().__init__()
        self.images = images #List of sprites for each stage
        self.images_len = len(images)
        self.curr_stage = None
        self.center_x = SCREEN_WIDTH/2
        self.center_y = SCREEN_HEIGHT/2
        self.image_width = SCREEN_WIDTH
        self.image_height = SCREEN_HEIGHT
        self.texture = arcade.load_texture(self.images[0])

    def update(self, curr_stage): #Switch background based on stage passed
        if curr_stage != self.curr_stage:
            if curr_stage > self.images_len:
                curr_stage = 1
            self.texture = arcade.load_texture(self.images[curr_stage-1])
            self.curr_stage = curr_stage
        super().update()
