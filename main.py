import arcade
from attack import Attacks, Meele
from constant import *

class MovingRectangle(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the background color (light gray)
        arcade.set_background_color(arcade.color.LIGHT_GRAY)

        # Rectangle position
        self.rect_x = SCREEN_WIDTH / 2
        self.rect_y = SCREEN_HEIGHT / 2

        # Track which keys are currently pressed
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False

        # Initialize attack
        self.melee_attack = Meele(self)  # Fixed class name to match attacks.py

    def on_draw(self):
        """Render the screen"""
        self.clear()
        
        # Draw the rectangle (blue)
        arcade.draw_rectangle_filled(
            self.rect_x, self.rect_y,
            RECT_WIDTH, RECT_HEIGHT,
            arcade.color.BLUE
        )

        # Draw attack if attacking
        self.melee_attack.draw()

    def on_key_press(self, key, modifiers):
        """Called when a key is pressed"""
        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

        # WASD attack
        elif key == arcade.key.W:
            self.melee_attack.stab('up')
        elif key == arcade.key.S:
            self.melee_attack.stab('down')
        elif key == arcade.key.A:
            self.melee_attack.stab('left')
        elif key == arcade.key.D:
            self.melee_attack.stab('right')

    def on_key_release(self, key, modifiers):
        """Called when a key is released"""
        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        """Movement and game logic"""
        # Update rectangle position based on pressed keys
        if self.up_pressed:
            self.rect_y += MOVEMENT_SPEED
        if self.down_pressed:
            self.rect_y -= MOVEMENT_SPEED
        if self.left_pressed:
            self.rect_x -= MOVEMENT_SPEED
        if self.right_pressed:
            self.rect_x += MOVEMENT_SPEED

        self.melee_attack.update()

def main():
    window = MovingRectangle()
    arcade.run()

if __name__ == "__main__":
    main()