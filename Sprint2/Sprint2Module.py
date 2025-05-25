from ursina import *

# Sprinting function (Works)
def sprint(player, key):
    """Function to handle sprinting mechanics for the player."""
    if key == "shift":
        player.speed = 20
    elif key == "shift up":
        player.speed = 10


# Get gun function (Works)
def get_gun(player, gun):
    """Function to equip a gun to the player."""
    gun.parent = camera
    gun.position = Vec3(0,-.75,.5)
    player.gun = gun


# Controls gun shooting, such as sound, gun color, bullets, and bullet shooting
def shoot(gun, key):
    """Function to handle shooting mechanics for the gun."""
    if key == 'left mouse down':
        Audio("assets/laser_sound.wav")
        gun.blink(color.red)
        bullet = Entity(parent=gun, model='cube', scale=.6, color=color.black)
        bullet.world_parent = scene
        bullet.animate_position(bullet.position+(bullet.forward*3000), curve=curve.linear, duration=0.5)
        destroy(bullet, delay=0.5)


