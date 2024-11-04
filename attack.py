import arcade
from constant import RECT_WIDTH, RECT_HEIGHT


class Attacks:
    def __init__(self, player):
        self.player = player
        self.attack_cooldown = 0
        self.is_attacking = False
        self.attack_duration = 20
        self.attack_range = 30
        self.damage = 10
        self.attack_direction = 'right'


class Meele(Attacks):
    def __init__(self, player):
        super().__init__(player)
        self.attack_box = None

    def stab(self, direction):
        if not self.is_attacking and self.attack_cooldown <= 0:
            self.is_attacking = True
            self.attack_cooldown = 30
            self.attack_direction = direction

            # Direction of attack
            if direction == 'right':
                self.attack_box = {
                    'x': self.player.rect_x + RECT_WIDTH/2,
                    'y': self.player.rect_y,
                    'width': self.attack_range,
                    'height': self.attack_range/2
                }
            elif direction == 'left':
                self.attack_box = {
                    'x': self.player.rect_x - RECT_WIDTH/2,
                    'y': self.player.rect_y,
                    'width': self.attack_range,
                    'height': self.attack_range/2
                }
            elif direction == 'up':
                self.attack_box = {
                    'x': self.player.rect_x,
                    'y': self.player.rect_y + RECT_HEIGHT/2,
                    'width': self.attack_range/2,
                    'height': self.attack_range
                }
            elif direction == 'down':
                self.attack_box = {
                    'x': self.player.rect_x,
                    'y': self.player.rect_y - RECT_HEIGHT/2,
                    'width': self.attack_range/2,
                    'height': self.attack_range
                }
            
            return True
        return False
    
    def update(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        if self.is_attacking:
            self.attack_duration -= 1
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