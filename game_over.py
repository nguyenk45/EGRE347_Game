import arcade
from constant import *
import time

class GameOver:
    def __init__(self, game_window):
        self.game_window = game_window
        self.start_time = time.time()
        self.end_time = None
        
    def set_end_time(self):
        if self.end_time is None:
            self.end_time = time.time()
    
    def draw(self):
        current_time = self.end_time if self.end_time else time.time()

        arcade.draw_rectangle_filled(
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            arcade.color.BLACK
        )
        
        stats_box_width = 400
        stats_box_height = 350
        arcade.draw_rectangle_filled(
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2,
            stats_box_width,
            stats_box_height,
            arcade.color.GRAY
        )
        
        total_kills = self.game_window.enemy_manager.scaling_system.enemies_killed
        level_reached = self.game_window.room.current_room
        base_damage = self.game_window.player.meele_attack.damage
        scaled_damage = int(base_damage * self.game_window.enemy_manager.scaling_system.player_damage())
        time_played = int(current_time - self.start_time)
        damage_taken = self.game_window.player.total_damage_taken
        minutes = time_played // 60
        seconds = time_played % 60
        
        
        text_color = arcade.color.WHITE
        text_size = 20
        center_x = SCREEN_WIDTH / 2
        start_y = SCREEN_HEIGHT / 2 + 100
        line_spacing = 40
        
        # Game Over text
        arcade.draw_text(
            "GAME OVER",
            center_x - 100,
            start_y + 200,
            text_color,
            50,
            width=200,
            align="center",
            bold=True
        )
        
        # Stats
        stats_text = [
            f"Enemies Killed: {total_kills}",
            f"Level Reached: {level_reached}",
            f"Final Attack Power: {scaled_damage}",
            f"Total Healing: {total_kills} HP",
            f"Damage Taken: {damage_taken}",
            f"Time Played: {minutes:02d}:{seconds:02d}"
        ]
        
        for i, text in enumerate(stats_text):
            arcade.draw_text(
                text,
                center_x - 150,
                start_y - (i * line_spacing),
                text_color,
                text_size
            )