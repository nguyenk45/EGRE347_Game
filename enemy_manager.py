import arcade
import random
from constant import *
from enemy import Enemy, Attack_Collision_Damage
from scaling import ScalingSystem

demon_spritesheet = "images/demonanim.png"
imp_spritesheet = "images/impanim.png"

class EnemyManager:
    def __init__(self, game_window):
        self.game_window = game_window
        self.enemies = arcade.SpriteList()
        self.attack_collisions = []
        self.scaling_system = ScalingSystem()

    def create_enemies(self, current_room):
        self.enemies.clear()  # Clear previous enemies
        self.attack_collisions = []  # Clear previous collision handlers
        
        num_enemies = 0
        
        if current_room == 1:
            return  # No enemies in room 1
        elif current_room == 2:
            num_enemies = 1  # One enemy in room 2
        elif current_room == 3:
            num_enemies = 2  # Two enemies in room 3
        elif current_room == 4:
            num_enemies = 3  # Three enemies in room 4
        else:
            # Random number of enemies (2-6) after room 4
            num_enemies = random.randint(2, 6)
        
        # Always add one chasing enemy and one vertical enemy after room 3
        if current_room >= 3:
            # Add chasing enemy
            chase_enemy = Enemy(imp_spritesheet, (36,44), 6, self.scaling_system, current_room, is_vertical=False)
            chase_enemy.pos_x = random.randint(RECT_WIDTH, SCREEN_WIDTH - RECT_WIDTH)
            chase_enemy.pos_y = random.randint(RECT_HEIGHT, GAME_HEIGHT - RECT_HEIGHT)
            self.enemies.append(chase_enemy)
            self.attack_collisions.append(Attack_Collision_Damage(self.game_window.player, chase_enemy))
            
            # Add vertical enemy
            vertical_enemy = Enemy(demon_spritesheet, (82, 56), 5, self.scaling_system, current_room, is_vertical=True)
            vertical_enemy.pos_x = random.randint(RECT_WIDTH, SCREEN_WIDTH - RECT_WIDTH)
            vertical_enemy.pos_y = random.randint(RECT_HEIGHT, GAME_HEIGHT - RECT_HEIGHT)
            self.enemies.append(vertical_enemy)
            self.attack_collisions.append(Attack_Collision_Damage(self.game_window.player, vertical_enemy))
            
            # Enemies to spawn
            num_enemies = max(0, num_enemies - 2)  # Subtract 2 for requried spawns
        
            # Add rest of enemies
            for i in range(num_enemies):
                is_vertical = random.choice([True, False])  # Randomly enemy type
                if is_vertical:
                    spritesheet = demon_spritesheet
                    dim = (82, 56)
                    cols = 5
                else:
                    spritesheet = imp_spritesheet
                    dim = (36,44)
                    cols = 6
                enemy = Enemy(spritesheet, dim, cols, self.scaling_system, current_room, is_vertical=is_vertical)
                enemy.pos_x = random.randint(RECT_WIDTH, SCREEN_WIDTH - RECT_WIDTH)
                enemy.pos_y = random.randint(RECT_HEIGHT, GAME_HEIGHT - RECT_HEIGHT)
                self.enemies.append(enemy)
                self.attack_collisions.append(Attack_Collision_Damage(self.game_window.player, enemy))
        
        else: 
            # For rooms 1-2, just add chasing enemies
            for i in range(num_enemies):
                is_vertical = False
                enemy = Enemy(imp_spritesheet, (36,44), 5, self.scaling_system, current_room, is_vertical=is_vertical)
                enemy.pos_x = random.randint(RECT_WIDTH, SCREEN_WIDTH - RECT_WIDTH)
                enemy.pos_y = random.randint(RECT_HEIGHT, GAME_HEIGHT - RECT_HEIGHT)
                self.enemies.append(enemy)
                self.attack_collisions.append(Attack_Collision_Damage(self.game_window.player, enemy))

    def update(self, delta_time):
        for i, enemy in enumerate(self.enemies):
            if enemy.health > 0:
                enemy.update(delta_time)
                enemy.follow_player(self.game_window.player)
                self.attack_collisions[i].check_attack_collision()
                enemy.check_player_collision(self.game_window.player)
            else:
                self.enemies.pop(i)
                self.attack_collisions.pop(i)

    def draw(self):
        for e in self.enemies:
            e.draw()
        self.enemies.draw()

    def are_enemies_alive(self):
        return any(enemy.health > 0 for enemy in self.enemies)
    
    def enemy_died(self):
        self.scaling_system.enemy_killed()  

        # Heal player
        if self.game_window.player.health < Player_Health:
            self.game_window.player.health += 2
