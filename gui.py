import arcade
from constant import *

class GUI:
    def __init__(self, player):
        self.player = player
        
    def draw(self):
        # Draw GUI background
        arcade.draw_rectangle_filled(
            SCREEN_WIDTH / 2,
            GAME_HEIGHT + GUI_HEIGHT / 2,
            SCREEN_WIDTH,
            GUI_HEIGHT,
            arcade.color.DARK_BLUE
        )
        
        # Draw divider line
        arcade.draw_line(
            0, GAME_HEIGHT,
            SCREEN_WIDTH, GAME_HEIGHT,
            arcade.color.WHITE,
            2
        )
        
        # Draw player health
        arcade.draw_text(
            f"Health: {self.player.health}/100",
            GUI_PADDING,
            GAME_HEIGHT + GUI_HEIGHT - GUI_PADDING * 2,
            arcade.color.WHITE,
            20
        )
        
        # Draw attack damage
        damage = self.player.meele_attack.damage if self.player.item_collision.current_item else 0
        arcade.draw_text(
            f"Attack Damage: {damage}",
            GUI_PADDING,
            GAME_HEIGHT + GUI_HEIGHT - GUI_PADDING * 4,
            arcade.color.WHITE,
            20
        )
        
        # Draw current level/room
        if hasattr(self.player, 'game_window'):
            level = self.player.game_window.room.current_room
            arcade.draw_text(
                f"Level: {level}",
                GUI_PADDING,
                GAME_HEIGHT + GUI_HEIGHT - GUI_PADDING * 6,
                arcade.color.WHITE,
                20
            )