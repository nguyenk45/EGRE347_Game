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
        height * (max_health/10) - height/3, height - height/3,
        arcade.color.BLACK
    )
    #Draw remaining health
    if health > 0:
        arcade.draw_rectangle_filled(
            x - ((height * (max_health/10) - height * (health/10))/2), y,
            height * (health/10) - height/3, height - height/3,
            arcade.color.RED
        )