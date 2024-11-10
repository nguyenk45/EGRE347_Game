import arcade
from constant import *
from movement import *
from items import *

class item_collision:
    def __init__(self, object):
        self.object = object
        self.current_item = None
        self.can_pickup = False


    def pickup(self):
        player_x = self.object.movement.rect_x
        player_y = self.object.movement.rect_y

        item_x = self.object.item.x
        item_y = self.object.item.y

        if (abs(player_x - item_x) < (RECT_WIDTH + ITEM_WIDTH)/2 and 
            abs(player_y - item_y) < (RECT_HEIGHT + ITEM_HEIGHT)/2):           
            self.can_pickup = True
            return True
        
        self.can_pickup = False
        return False
    
    def on_key_press(self, key):
        if key == arcade.key.E and self.can_pickup and not self.object.item.is_picked:
            self.object.item.is_picked = True
            self.current_item = True
            self.object.item.Tutorial_Text = False
        
    def update(self, delta_time):
        self.pickup()