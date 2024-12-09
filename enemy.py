import arcade
import math
from constant import *
from invincibility import Invincible
from healthbar import draw_healthbar
from scaling import ScalingSystem


class Enemy(Invincible, arcade.Sprite):
    def __init__(self, scaling_system, current_room, is_vertical = False):
        arcade.Sprite.__init__(self)
        Invincible.__init__(self)

        self.pos_x = SCREEN_WIDTH/2
        self.pos_y = 2*(SCREEN_HEIGHT/3)

        # Initial Stats
        self.max_health = scaling_system.enemy_health(current_room)
        self.health = self.max_health
        self.damage = scaling_system.enemy_damage(current_room)

        self.change_x = 0
        self.change_y = 0
        self.enemy_speed = 2  # Enemy Speed

        self.is_vertical = is_vertical
        self.vertical_speed = scaling_system.vertical_speed(current_room) if is_vertical else 0
        self.moving_up = True

#        self.center_x = self.pos_x
#        self.center_y = self.pos_y

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

        if self.is_vertical:
            self.update_vertical_movement()

    def update_vertical_movement(self):
        if self.moving_up:
            self.pos_y += self.vertical_speed
            if self.pos_y > GAME_HEIGHT - RECT_HEIGHT:
                self.moving_up = False
        else:
            self.pos_y -= self.vertical_speed
            if self.pos_y < RECT_HEIGHT:
                self.moving_up = True
                
        self.center_y = self.pos_y

    def follow_player(self, player):
        if self.health <= 0 or self.is_vertical:
            return

        dx = player.movement.pos_x - self.pos_x
        dy = player.movement.pos_y - self.pos_y
        distance = math.sqrt(dx**2 + dy**2)

        if distance > 0:
            self.change_x = (dx / distance) * self.enemy_speed
            self.change_y = (dy / distance) * self.enemy_speed
            
            self.pos_x += self.change_x
            self.pos_y += self.change_y
            self.center_x = self.pos_x
            self.center_y = self.pos_y
    

    def draw(self):
        if self.health > 0:
            draw_healthbar(self.max_health, self.health, 10, self.pos_x, self.pos_y + 0.75*RECT_HEIGHT)
            arcade.draw_rectangle_filled(
                self.pos_x, self.pos_y,
                RECT_WIDTH, RECT_HEIGHT,
                arcade.color.GREEN
            )

    def check_player_collision(self, player):
        if (abs(self.pos_x - player.movement.pos_x) < RECT_WIDTH and 
            abs(self.pos_y - player.movement.pos_y) < RECT_HEIGHT and
            not player.invincible):
            player.take_damage(self.damage)

            
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
            base_damage = self.player.meele_attack.damage
            scaled_damage = int(base_damage * self.player.game_window.enemy_manager.scaling_system.player_damage())
            self.enemy.health -= scaled_damage
            
            if self.enemy.health <= 0:
                self.player.game_window.enemy_manager.enemy_died()
            
            print("Enemy:", self.enemy.health)
            self.enemy.invincibility = Time