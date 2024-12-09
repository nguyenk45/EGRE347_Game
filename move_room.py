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

        # Check if player has reached the door
        if (player.movement.pos_x + RECT_WIDTH/2 > SCREEN_WIDTH - DOOR_WIDTH and
            player.movement.pos_y > SCREEN_HEIGHT//2 - DOOR_HEIGHT//2 and
            player.movement.pos_y < SCREEN_HEIGHT//2 + DOOR_HEIGHT//2):
            
            # Move to next room and randomize player position
            self.current_room += 1
            player.movement.pos_x = random.randint(RECT_WIDTH//2, SCREEN_WIDTH - RECT_WIDTH//2)
            player.movement.pos_y = random.randint(RECT_HEIGHT//2, SCREEN_HEIGHT - RECT_HEIGHT//2)
            return True
        return False

    def draw(self):
        # Draw the door
        arcade.draw_rectangle_filled(
            SCREEN_WIDTH - DOOR_WIDTH//2, 
            SCREEN_HEIGHT//2,
            DOOR_WIDTH, DOOR_HEIGHT,
            arcade.color.BROWN
        )
        
        # Draw room number
        arcade.draw_text(
            f"Room {self.current_room}",
            SCREEN_WIDTH - 140, SCREEN_HEIGHT - 30,
            arcade.color.WHITE,
            20
        )

    def update(self, player):
        self.check_door_collision(player)
        
    def setup(self): #empty but can add game objects if needed
        pass