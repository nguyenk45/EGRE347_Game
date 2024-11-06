import arcade
import random
from constant import *
from movement import *

#set the size of the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 30


class Room:
    def __init__(self, player):
        self.player = player
        self.current_room = 1
    
        #keep track of what room we are in
        self.current_room = 1
    
    def check_door_collision(self):
        player_x = self.player.movement.rect_x
        player_y = self.player.movement.rect_y


        # Check if player has reached the door
        if (self.player.movement.rect_x + RECT_WIDTH/2 > SCREEN_WIDTH - DOOR_WIDTH and
            self.player.movement.rect_y > SCREEN_HEIGHT//2 - DOOR_HEIGHT//2 and
            self.player.movement.rect_y < SCREEN_HEIGHT//2 + DOOR_HEIGHT//2):
            
            # Move to next room and randomize player position
            self.current_room += 1
            self.player.movement.rect_x = random.randint(RECT_WIDTH//2, SCREEN_WIDTH - RECT_WIDTH//2)
            self.player.movement.rect_y = random.randint(RECT_HEIGHT//2, SCREEN_HEIGHT - RECT_HEIGHT//2)
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
            10, SCREEN_HEIGHT - 30,
            arcade.color.WHITE,
            20
        )

    def update(self):
        self.check_door_collision()
        
    def setup(self): #empty but can add game objects if needed
        pass