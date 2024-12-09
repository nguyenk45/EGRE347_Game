import arcade
import arcade
import random
from constant import *

#set the size of the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 30

class Room:
    def __init__(self):
        #keep track of what room we are in
        self.current_room = 1

        #For drawing sprite
        self.door_sprite = arcade.Sprite("images/door.png", center_x=SCREEN_WIDTH - DOOR_WIDTH//2, center_y=GAME_HEIGHT//2, scale = 0.5)
    
    def check_door_collision(self, player):

        # Check for door collision if door is visible
        if not self.draw_door(player.game_window): 
            return False

        # Check if player has reached the door
        if (player.movement.pos_x + RECT_WIDTH/2 > SCREEN_WIDTH - DOOR_WIDTH and
            player.movement.pos_y > SCREEN_HEIGHT//2 - DOOR_HEIGHT//2 and
            player.movement.pos_y < SCREEN_HEIGHT//2 + DOOR_HEIGHT//2):
            
            # Move to next room and player position after door
            self.current_room += 1
            player.movement.pos_x = RECT_WIDTH
            player.movement.pos_y = SCREEN_HEIGHT//2
            return True
        return False
    
    def draw_door(self, game_window):
        # Door appears if there's no enemy
        if game_window.current_room == 1:
            return True
        return not game_window.enemy_manager.are_enemies_alive()

    def draw(self, game_window):
        # Draw the door
        if self.draw_door(game_window):
            self.door_sprite.draw()

    def get_level(self):
        return self.current_room

    def update(self, player):
        return self.check_door_collision(player)
        
    def setup(self): #empty but can add game objects if needed
        pass