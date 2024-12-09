import arcade
from constant import *
from movement import Movement
from hurt import Ouchy
from attack import Meele
from pickup import item_collision
from anim import Animator

class Character(arcade.Sprite, Ouchy):
    def __init__(self, spritesheet, x, y):
        super().__init__()
        self.health = 100
        self.movement = Movement(self, x, y)
        self.meele_attack = Meele(self)
        self.item_collision = item_collision(self)

        self.anim = Animator(spritesheet, (32, 48), 16, 2)
        self.anim.registerAnim("stand", 0)
        self.anim.registerAnim("walk", *list(range(1, 15)))
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
        elif self.movement.moving_right:
            self.anim.flipHoriz(True)
        self.anim.next()
        self.texture = self.anim.texture

        self.meele_attack.update()
        self.item_collision.update(delta_time)

        super().update()
            
    def draw(self):
        #Draw hitbox
        Ouchy.draw(self)
        # Draw attack box
        self.meele_attack.draw()
        # Draw player
        super().draw()