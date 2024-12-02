import arcade
from constant import *

class Background(arcade.Sprite):
    def __init__(self, images):
        super().__init__()
        self.images = images #List of sprites for each stage
        self.curr_stage = None
        self.image_width = RECT_WIDTH
        self.image_height = RECT_HEIGHT
        self.image_x = 0
        self.image_y = 0

    def update(self, curr_stage): #Switch background based on stage passed
        # try:
        if curr_stage != self.curr_stage:
            self.texture = arcade.load_texture(self.images[curr_stage-1])
            self.curr_stage = curr_stage
        # except Exception as e:
        #     print(e)
        #     pass    #SHOULD BE SOME ERROR
        super().update()
