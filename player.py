import arcade
from constant import *
from movement import *
from attack import Meele
from pickup import item_collision
from character import Character
from hurt import Ouchy

class Player(Character, Ouchy):
    def __init__(self, spritesheet):
        Character.__init__(self, spritesheet, (32,48), 16)
        Ouchy.__init__(self)
        
        self.health = 100
        self.movement = playerMovement(self, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.meele_attack = Meele(self)
        self.item_collision = item_collision(self)

        #Set up sprite for block animation
        self.block_sprite = arcade.Sprite("images/guideanim_block.png")
        self.block_sprite_list = arcade.SpriteList()
        
        self.game_window = None
    
    def update(self, delta_time):
        super().update(delta_time)
        self.meele_attack.update()
        self.item_collision.update(delta_time)
        self.update_damage_state()  

    def draw(self):
        super().draw()
        # Draw attack box
        self.meele_attack.draw()
        # Overlay sprite for blocking over movement animation
        if self.invincible:
            self.block_sprite.center_y = self.movement.pos_y + 10
            if self.movement.facing_right:
                self.block_sprite.texture = arcade.load_texture("images/guideanim_block.png", flipped_horizontally=True)
                self.block_sprite.center_x = self.movement.pos_x + 2
            else:
                self.block_sprite.texture = arcade.load_texture("images/guideanim_block.png")
                self.block_sprite.center_x = self.movement.pos_x - 2
            
            self.block_sprite.draw()
    
    def on_key_press(self, key, modifiers):
        self.movement.on_key_press(key, modifiers)
        if key == arcade.key.E:
            self.item_collision.on_key_press(key)
        # Check for "dodge roll" and update timer
        if key == arcade.key.SPACE:
            if not self.dodge_timeout:
                self.trigger_invincibility(100)
                self.dodge_timeout = 250

    def on_key_release(self, key, modifiers):
        self.movement.on_key_release(key, modifiers)