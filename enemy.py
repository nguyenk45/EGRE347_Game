import arcade
import math
from constant import *
from invincibility import Invincible


class Enemy(Invincible):
    def __init__(self):
        super().__init__()
        self.rect_x = SCREEN_WIDTH/2
        self.rect_y = 2*(SCREEN_HEIGHT/3)
        self.health = 100

        self.change_x = 0
        self.change_y = 0
        self.enemy_speed = 2  # Enemy Speed


    def follow_player(self, player):
        if self.health <= 0:
            return  # Don't move if dead
            
        # Distance to player
        dx = player.movement.rect_x - self.rect_x
        dy = player.movement.rect_y - self.rect_y
        distance = math.sqrt(dx**2 + dy**2)

        if distance > 0:  # Division by zero
            self.change_x = (dx / distance) * self.enemy_speed
            self.change_y = (dy / distance) * self.enemy_speed
            
            # Update position
            self.rect_x += self.change_x
            self.rect_y += self.change_y

    def update(self):
        self.update_invincibility()

    def draw(self):
        if self.health > 0:
            arcade.draw_rectangle_filled(
                self.rect_x, self.rect_y,
                RECT_WIDTH, RECT_HEIGHT,
                arcade.color.GREEN
            )

    def check_player_collision(self, player):
        if (abs(self.rect_x - player.movement.rect_x) < RECT_WIDTH and 
            abs(self.rect_y - player.movement.rect_y) < RECT_HEIGHT and
            not player.invincible):
            player.take_damage(Enemy_Damage)

            
class Attack_Collision_Damage:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        
    def check_attack_collision(self):
        if (########################################arcade.check_for_collision()
            self.player.meele_attack.is_attacking and 
            self.player.meele_attack.attack_box and 
            self.enemy.health > 0 and
            not self.enemy.invincible):
            
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
                print("Enemy:", self.enemy.health)
                self.enemy.invincibility = Time
