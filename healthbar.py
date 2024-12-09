import arcade

def draw_healthbar(max_health, health, height, x, y):
    #Draw outline
    arcade.draw_rectangle_filled(
        x, y,
        height * (max_health/10), height,
        arcade.color.GRAY
    )
    #Draw lost health
    arcade.draw_rectangle_filled(
        x, y,
        height/1.2 * (max_health/10), height/1.2,
        arcade.color.BLACK
    )
    #Draw remaining health
    arcade.draw_rectangle_filled(
        x, y,
        height/1.2 * (health/10), height/1.2,
        arcade.color.RED
    )