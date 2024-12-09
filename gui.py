import arcade
from constant import *
from healthbar import draw_healthbar

player_icon_sprites = ["images/Guid_pfp.PNG", "images/guide_dying.png", "images/guide_dead.png"]

class GUI:
    def __init__(self, player):
        self.player = player

        self.player_icon = arcade.Sprite(player_icon_sprites[0], center_x=GUI_PADDING + 650, center_y=GAME_HEIGHT + GUI_HEIGHT - GUI_PADDING * 4, scale = 0.5)
        self.sprites_list = arcade.SpriteList()
        self.sprites_list.append(self.player_icon)
        #Add GUI to damage observers
        player.register_damage_observer(self)

    #When player takes damage, change player icon texture if appropriate
    def notified_damage(self):
        if(self.player.health < 20):
            self.player_icon.texture = arcade.load_texture(player_icon_sprites[2])
            self.player_icon.scale = 5
        elif(self.player.health < 40):
            self.player_icon.texture = arcade.load_texture(player_icon_sprites[1])
            self.player_icon.scale = 5

        
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
        
        # Draw sprites
        self.sprites_list.draw()