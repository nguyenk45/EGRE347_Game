import arcade
from constant import *
from character import Player
from items import Item
from enemy import Enemy, Attack_Collision_Damage
from move_room import Room

class RectangleGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # Set the background color
        arcade.set_background_color(arcade.color.LIGHT_GRAY)

        # Initialize Room
        self.room = Room()

        # Initialize player
        self.player = Player()
        self.player.game_window = self
        
        # Initialize item and enemy
        self.item = Item()
        self.enemy = Enemy()
        
        # Initialize room number
        self.current_room = 1

        # Initialize Attack Collision
        self.attack_collision_damage = Attack_Collision_Damage(self.player, self.enemy)

    def on_draw(self):
        self.clear()
        
        # Draw door and room number
        self.room.draw()
        
        # Draw game objects
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

        self.enemy.update()
        
        # Update enemy collision and damage
        self.attack_collision_damage.check_attack_collision()
      
        # Check for room transition
        self.room.update(self.player)

        if self.enemy.health > 0:  # Only check if enemy is alive
            self.enemy.check_player_collision(self.player)

def main():
    window = RectangleGame()
    arcade.run()

if __name__ == "__main__":
    main()