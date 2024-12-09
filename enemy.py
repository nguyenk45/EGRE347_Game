import arcade
import math
from constant import *
from invincibility import Invincible
from hitbox import draw_hitbox


class Enemy(Invincible, arcade.Sprite):
    def __init__(self):
        arcade.Sprite.__init__(self)
        Invincible.__init__(self)

        self.pos_x = SCREEN_WIDTH/2
        self.pos_y = 2*(SCREEN_HEIGHT/3)
        self.max_health = 100
        self.health = 100

        self.change_x = 0
        self.change_y = 0
        self.enemy_speed = 2  # Enemy Speed

        self.center_x = self.pos_x
        self.center_y = self.pos_y

    def follow_player(self, player):
        if self.health <= 0:
            return  # Don't move if dead
            
        # Distance to player
        dx = player.movement.pos_x - self.pos_x
        dy = player.movement.pos_y - self.pos_y
        distance = math.sqrt(dx**2 + dy**2)

        if distance > 0:  # Division by zero
            self.change_x = (dx / distance) * self.enemy_speed
            self.change_y = (dy / distance) * self.enemy_speed
            
            # Update position
            self.pos_x += self.change_x
            self.pos_y += self.change_y
            self.center_x = self.pos_x
            self.center_y = self.pos_y

    def update(self):
        self.update_invincibility()

    def draw(self):
        draw_hitbox(self.max_health, self.health, 10, self.rect_x - 0.75*RECT_WIDTH, self.rect_y + 0.75*RECT_HEIGHT)
        if self.health > 0:
            arcade.draw_rectangle_filled(
                self.pos_x, self.pos_y,
                RECT_WIDTH, RECT_HEIGHT,
                arcade.color.GREEN
            )

    def check_player_collision(self, player):
        if (abs(self.pos_x - player.movement.pos_x) < RECT_WIDTH and 
            abs(self.pos_y - player.movement.pos_y) < RECT_HEIGHT and
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

        return (abs(attack_box['x'] - self.enemy.pos_x) < (attack_box['width'] + RECT_WIDTH)/2 and 
                abs(attack_box['y'] - self.enemy.pos_y) < (attack_box['height'] + RECT_HEIGHT)/2)
    
    def apply_damage(self):
        if self.player.item_collision.current_item:
                self.enemy.health -= self.player.meele_attack.damage
                print("Enemy:", self.enemy.health)
                self.enemy.invincibility = Time
