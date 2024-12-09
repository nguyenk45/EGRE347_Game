import arcade
from constant import *
from movement import Movement
from hurt import Invincible
from attack import Meele
from pickup import item_collision
from anim import Animator

class Character(arcade.Sprite, Invincible):
    def __init__(self, spritesheet, dim, cols):
        super().__init__()
        self.movement = Movement(self, 0, 0)

        self.anim = Animator(spritesheet, dim, cols, 1)
        self.anim.registerAnim("stand", 0)
        self.anim.registerAnim("walk", *list(range(1, cols-1)))
        self.anim.change("stand")
        
        self.game_window = None
            
    def update(self, delta_time):
        self.movement.on_update(delta_time)

        self.center_x = self.movement.pos_x
        self.center_y = self.movement.pos_y

        if ((self.movement.moving_up ^ self.movement.moving_down) or
                (self.movement.moving_left ^ self.movement.moving_right)):
            if self.anim.anim_curr != "walk":
                self.anim.change("walk")
        elif self.anim.anim_curr != "stand":
            self.anim.change("stand")

        if self.movement.moving_left:
            self.anim.flipHoriz(False)
            self.movement.facing_right = False
        elif self.movement.moving_right:
            self.anim.flipHoriz(True)
            self.movement.facing_right = True
        self.anim.next()
        self.texture = self.anim.texture

        super().update()
            
    def draw(self):
        # Draw player
        super().draw()