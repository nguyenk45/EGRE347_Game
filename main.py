import arcade
from constant import *
from character import Player
from items import Item
from enemy import Enemy
from move_room import Room
from attack import Attack_Collision

guide_sprite = "images/guide.png"

class RectangleGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # Set the background color
        arcade.set_background_color(arcade.color.LIGHT_GRAY)

        # Initialize Room
        self.room = Room()
        self.player_list = arcade.SpriteList()

        # Initialize player
        self.player = Player(guide_sprite)
        self.player_list.append(self.player)
        self.player.game_window = self
        
        # Initialize item and enemy
        self.item = Item()
        self.enemy = Enemy()
        
        # Initialize room number
        self.current_room = 1

        # Initialize Attack Collision
        self.attack_collision = Attack_Collision(self.player, self.enemy)

    def on_draw(self):
        self.clear()
        
        # Draw door and room number
        self.room.draw()
        
        # Draw game objects
        self.player_list.draw()
        self.player.draw()
        self.item.draw()
        self.enemy.draw()

    def on_key_press(self, key, modifiers):
        self.player.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.player.on_key_release(key, modifiers)

    def check_door_collision(self):
        self.room.check_door_collision(self)
  
    def on_update(self, delta_time):
        # Update player
        self.player.update(delta_time)
        
        # Update enemy collision and damage
        self.attack_collision.check_attack_collision()
      
        # Check for room transition
        self.room.update(self.player)

def main():
    window = RectangleGame()
    arcade.run()

if __name__ == "__main__":
    main()