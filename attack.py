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
                'x': self.player.movement.rect_x + RECT_WIDTH/1.5,
                'y': self.player.movement.rect_y,
                'width': self.attack_range,
                'height': self.attack_range/2
            }
        elif direction == 'left':
            self.attack_box = {
                'x': self.player.movement.rect_x - RECT_WIDTH/1.5,
                'y': self.player.movement.rect_y,
                'width': self.attack_range,
                'height': self.attack_range/2
            }
        elif direction == 'up':
            self.attack_box = {
                'x': self.player.movement.rect_x,
                'y': self.player.movement.rect_y + RECT_HEIGHT/1.5,
                'width': self.attack_range/2,
                'height': self.attack_range
            }
        elif direction == 'down':
            self.attack_box = {
                'x': self.player.movement.rect_x,
                'y': self.player.movement.rect_y - RECT_HEIGHT/1.5,
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
'''
class Attack_Collision_Damage:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        
    def check_attack_collision(self):
        if (########################################arcade.check_for_collision()
            self.player.meele_attack.is_attacking and 
            self.player.meele_attack.attack_box and 
            self.enemy.health > 0):
            
            attack_box = self.player.meele_attack.attack_box
            if self.is_hit(attack_box):
                self.apply_damage()
    
    def is_hit(self, attack_box):
#        return (arcade.check_for_collision(attack_box,self.rect_x and self.enemy.rect_y))

        return (abs(attack_box['x'] - self.enemy.rect_x) < (attack_box['width'] + RECT_WIDTH)/2 and 
                abs(attack_box['y'] - self.enemy.rect_y) < (attack_box['height'] + RECT_HEIGHT)/2)
    
    def apply_damage(self):
        if self.player.item_collision.current_item:
            self.enemy.health -= self.player.meele_attack.damage
'''