from constant import *

# scaling.py
class ScalingSystem:
    def __init__(self):
        self.enemies_killed = 0
        self.base_enemy_health = Enemy_Health
        self.base_enemy_damage = Enemy_Damage
        self.base_vertical_speed = Vertical_Enemy_Speed
        self.damage_multiplier = 1.0
        
    def enemy_killed(self):
        self.enemies_killed += 1
        if self.enemies_killed % 5 == 0:  # Every 5 kills
            self.damage_multiplier *= 1.05  # 5% increase
            
    def enemy_health(self, current_room):
        health_multiplier = 1.0
        health_increases = (current_room - 1) // 5  # Every 5 levels
        if health_increases > 0:
            health_multiplier = (1.2 ** health_increases)  # 20% increase per 5 levels
        return int(self.base_enemy_health * health_multiplier)
    
    def enemy_damage(self, current_room):
        damage_multiplier = 1.0
        damage_increases = (current_room - 1) // 3  # Every 3 levels
        if damage_increases > 0:
            damage_multiplier = (1.2 ** damage_increases)  # 20% increase per 3 levels
        return int(self.base_enemy_damage * damage_multiplier)
    
    def vertical_speed(self, current_room):
        speed_multiplier = 1.0
        speed_increases = (current_room - 1) // 5  # Every 5 levels
        if speed_increases > 0:
            speed_multiplier = (1.25 ** speed_increases)  # 25% increase per 5 levels
        return self.base_vertical_speed * speed_multiplier
    
    def player_damage(self):
        return self.damage_multiplier