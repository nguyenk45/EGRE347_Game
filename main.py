import arcade
from attack import *
from constant import *
from move_room import *
from movement import *

class RectangleGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # Set the background color (light gray)
        arcade.set_background_color(arcade.color.LIGHT_GRAY)

        # Initialize Movement
        self.movement = Movement(self)

        # Initialize attack
        self.meele_attack = Meele(self)

        # Initialize room system
        self.room = Room(self)

        # Inistialize health
        self.health = 100

    def on_draw(self): #Render the screen
        self.clear()
        
        # Draw the room elements (door and room number)
        self.room.draw()
        
        # Draw the rectangle (blue)
        arcade.draw_rectangle_filled(
            self.movement.rect_x, self.movement.rect_y,
            RECT_WIDTH, RECT_HEIGHT,
            arcade.color.BLUE
        )

        # Draw attack if attacking
        self.meele_attack.draw()

    def on_key_press(self, key, modifiers):
        self.movement.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.movement.on_key_release(key, modifiers)

    def on_update(self, delta_time):
        self.meele_attack.update()
        self.room.update()
        self.movement.on_update(delta_time)

def main():
    window = RectangleGame()
    arcade.run()

if __name__ == "__main__":
    main() 