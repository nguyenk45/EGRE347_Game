import arcade
from constant import *

class Attacks:
    def __init__(self, player):
        self.player = player
        self.attack_cooldown = 0
        self.is_attacking = False
        self.attack_duration = 20
        self.attack_range = 30
        self.damage = Dagger

    def attack_key(self, key):
        if key == arcade.key.W:
            return self.stab('up')
        elif key == arcade.key.S:
            return self.stab('down')
        elif key == arcade.key.A:
            return self.stab('left')
        elif key == arcade.key.D:
            return self.stab('right')
        return False

class Meele(Attacks):
    def __init__(self, player):
        super().__init__(player)
        self.attack_box = None

    def stab(self, direction):
        if not self.player.item_collision.current_item:
            return False

        if not self.is_attacking and self.attack_cooldown <= 0:
            self.is_attacking = True
            self.attack_cooldown = 30
            self.attack_direction = direction
            self.player_attack_direction(direction)
            return True
        return False
    
    def player_attack_direction(self, direction):
        if direction == 'right':
            self.attack_box = {
                'x': self.player.movement.pos_x + RECT_WIDTH/1.5,
                'y': self.player.movement.pos_y,
                'width': self.attack_range,
                'height': self.attack_range/2
            }
        elif direction == 'left':
            self.attack_box = {
                'x': self.player.movement.pos_x - RECT_WIDTH/1.5,
                'y': self.player.movement.pos_y,
                'width': self.attack_range,
                'height': self.attack_range/2
            }
        elif direction == 'up':
            self.attack_box = {
                'x': self.player.movement.pos_x,
                'y': self.player.movement.pos_y + RECT_HEIGHT/1.5,
                'width': self.attack_range/2,
                'height': self.attack_range
            }
        elif direction == 'down':
            self.attack_box = {
                'x': self.player.movement.pos_x,
                'y': self.player.movement.pos_y - RECT_HEIGHT/1.5,
                'width': self.attack_range/2,
                'height': self.attack_range
            }  
    
    def update(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        if self.is_attacking:
            self.player_attack_direction(self.attack_direction)
            self.attack_duration -= 1
#            print(self.attack_duration)
            if self.attack_duration <= 0:
                self.is_attacking = False
                self.attack_duration = 20
                self.attack_box = None

    def draw(self):
        if self.is_attacking and self.attack_box:
            arcade.draw_rectangle_filled(
                self.attack_box['x'],
                self.attack_box['y'],
                self.attack_box['width'],
                self.attack_box['height'],
                arcade.color.RED
            )
            
class Attack_Collision_Damage:
    def apply_damage(self):
        if self.player.item_collision.current_item:
            base_damage = self.player.meele_attack.damage
            scaled_damage = int(base_damage * self.player.game_window.enemy_manager.scaling_system.player_damage())
            self.enemy.health -= scaled_damage
            print("Enemy:", self.enemy.health)
            if self.enemy.health <= 0:
                self.player.game_window.enemy_manager.enemy_died()
            self.enemy.invincibility = Time