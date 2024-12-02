import arcade
from constant import *
from movement import Movement
from attack import Meele
from pickup import item_collision
from anim import Animator

class Player(arcade.Sprite):
    def __init__(self, spritesheet):
        super().__init__()
        self.health = 100
        self.movement = Movement(self)
        self.meele_attack = Meele(self)
        self.item_collision = item_collision(self)

        self.anim = Animator(spritesheet, (32, 48), 16, 2)
        self.anim.registerAnim("stand", 0)
        self.anim.registerAnim("walk", *list(range(1, 15)))
        self.anim.change("stand")
        
        self.game_window = None
    
    def on_key_press(self, key, modifiers):
        self.movement.on_key_press(key, modifiers)
        if key == arcade.key.E:
            self.item_collision.on_key_press(key)
            
    def on_key_release(self, key, modifiers):
        self.movement.on_key_release(key, modifiers)
            
    def update(self, delta_time):
        self.movement.on_update(delta_time)

        self.center_x = self.movement.rect_x
        self.center_y = self.movement.rect_y

        if any([self.movement.up_pressed, self.movement.down_pressed,
                self.movement.left_pressed, self.movement.right_pressed]):
            if self.anim.anim_curr != "walk":
                self.anim.change("walk")
        elif self.anim.anim_curr != "stand":
            self.anim.change("stand")

        if self.movement.left_pressed:
            self.anim.flipHoriz(False)
        elif self.movement.right_pressed:
            self.anim.flipHoriz(True)
        self.anim.next()
        self.texture = self.anim.texture

        self.meele_attack.update()
        self.item_collision.update(delta_time)

        super().update()
            
    def draw(self):
        # Draw attack box
        self.meele_attack.draw()
        super().draw()