import arcade
from constant import *

class Background(arcade.Sprite):
    def __init__(self, sprites):
        super().__init__(sprites[0])
        self.sprites = sprites #List of sprites for each stage
        self.image_width = RECT_WIDTH
        self.image_height = RECT_HEIGHT
        self.image_x = 0
        self.image_y = 0

    def update(self, stage): #Switch background based on stage passed
        try:
            newTexture = arcade.Texture("newTexture", self.sprites[stage-1])
            self.texture = newTexture
        except Exception as e:
            print(e)
            pass    #SHOULD BE SOME ERROR
        super().update()
