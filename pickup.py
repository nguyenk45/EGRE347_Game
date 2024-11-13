import arcade
from constant import *

class item_collision:
    def __init__(self, player):
        self.player = player
        self.current_item = None
        self.can_pickup = False

    def pickup(self):
        if not hasattr(self.player, 'game_window') or not self.player.game_window:
            return False
            
        item = self.player.game_window.item
        if not item:
            return False

        if (abs(self.player.movement.rect_x - item.x) < (RECT_WIDTH + ITEM_WIDTH)/2 and 
            abs(self.player.movement.rect_y - item.y) < (RECT_HEIGHT + ITEM_HEIGHT)/2):           
            self.can_pickup = True
            return True
        
        self.can_pickup = False
        return False
    
    def on_key_press(self, key):
        if not hasattr(self.player, 'game_window') or not self.player.game_window:
            return
            
        if key == arcade.key.E and self.can_pickup and not self.player.game_window.item.is_picked:
            self.player.game_window.item.is_picked = True
            self.current_item = True
            self.player.game_window.item.Tutorial_Text = False
        
    def update(self, delta_time):
        self.pickup()