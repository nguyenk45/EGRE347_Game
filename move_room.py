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
        return game_window.enemy is None or game_window.enemy.health <= 0

    def draw(self, game_window):
        # Draw the door
        if self.draw_door(game_window):
            arcade.draw_rectangle_filled(
                SCREEN_WIDTH - DOOR_WIDTH//2, 
                GAME_HEIGHT//2,
                DOOR_WIDTH, DOOR_HEIGHT,
                arcade.color.BROWN
            )


    def get_level(self):
        return self.current_room

    def update(self, player):
        return self.check_door_collision(player)
        
    def setup(self): #empty but can add game objects if needed
        pass