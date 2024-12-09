import arcade
from constant import *
from player import Player
from items import Item
from enemy import Enemy, Attack_Collision_Damage
from move_room import Room
from background import Background


guide_sprite = "images/guideanim.png"
background_sprites = ["images/stage1.png", "images/stage2.png"]

class RectangleGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.stage = 1 #Track current stage

        #Initialize Background
        self.background_list = arcade.SpriteList()
        self.background = Background(background_sprites)
        self.background_list.append(self.background)
        

        # Initialize Room
        self.room = Room()

        # Initialize player
        self.player_list = arcade.SpriteList()
        self.player = Player(guide_sprite)
        self.player_list.append(self.player)
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
        
        # Draw background first
        self.background_list.draw()

        # Draw door and room number
        self.room.draw()
        
        # Draw game objects
        self.player_list.draw()  # Draw sprites
        self.player.draw() # Draw attack box
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
        self.enemy.follow_player(self.player)
        
        # Update enemy collision and damage
        self.attack_collision_damage.check_attack_collision()
    
       # Check for room transition and update background
        if self.room.update(self.player):
            self.background.update(self.room.get_level())  # Update background on room change

        if self.enemy.health > 0:  # Only check if enemy is alive
            self.enemy.check_player_collision(self.player)

def main():
    window = RectangleGame()
    arcade.run()

if __name__ == "__main__":
    main()