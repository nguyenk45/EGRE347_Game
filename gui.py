import arcade
from constant import *
from healthbar import draw_healthbar

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
            arcade.color.TAN
        )
        
        # Draw divider line
        arcade.draw_line(
            0, GAME_HEIGHT,
            SCREEN_WIDTH, GAME_HEIGHT,
            arcade.color.WHITE,
            2
        )

        draw_healthbar(
            100, 
            self.player.health, 
            20, 
            GUI_PADDING + 650,
            GAME_HEIGHT + GUI_HEIGHT - GUI_PADDING * 8 
        )

        # Draw player health txt
        arcade.draw_text(
            f"Health: {self.player.health}/100",
            GUI_PADDING,
            GAME_HEIGHT + GUI_HEIGHT - GUI_PADDING * 2,
            arcade.color.WHITE,
            20
        )
        
        # Draw attack damage
        damage = self.player.meele_attack.damage if self.player.item_collision.current_item else 0
        if self.player.game_window and damage > 0:
            scaling_system = self.player.game_window.enemy_manager.scaling_system
            scaled_damage = int(damage * scaling_system.player_damage())
        else:
            scaled_damage = damage
        arcade.draw_text(
            f"Attack Damage: {scaled_damage}",
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