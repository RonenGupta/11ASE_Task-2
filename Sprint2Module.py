from ursina import *

bullets = []

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
    gun.collider = None


# Controls gun shooting, such as sound, gun color, bullets, and bullet shooting
def shoot(gun, key):
    """Function to handle shooting mechanics for the gun."""
    """Handles shooting mechanics and tracks bullets."""
    if key == 'left mouse down':
        Audio("assets/laser_sound.wav")
        gun.blink(color.red)
        bullet = Entity(parent=gun, model='cube', scale=.6, color=color.black, collider='box')
        bullet.world_parent = scene
        bullet.animate_position(bullet.position + (bullet.forward * 500), curve=curve.linear, duration=0.5)
        
        bullets.append(bullet)  # Store bullet in the list
        destroy(bullet, delay=0.5)


# Controls enemy damaging player and death
def enmdmg(player, healthbar, enemy):
    """Function to handle enemy damage and death"""
    if player.intersects().hit and player.intersects().entity == enemy:
        healthbar.value -= 5
    if healthbar.value == 0:
        quit()

# Checks if the player does damage to the enemy with the bullets
def plrdmg(enemy):
    for bullet in bullets:  # Loop through all active bullets
        if bullet.intersects().hit and bullet.intersects().entity == enemy:
            enemy.health -= 10  # Reduce enemy health when hit
            enemy.healthbar.value -= 10
            print(f"Enemy hit! Health remaining: {enemy.health}")
            if enemy.health <= 0 or enemy.healthbar.value <= 0:
                destroy(enemy)  # Remove enemy when health reaches 0
                bullets.remove(bullet)  # Clean up the bullet after the enemy is destroyed

# Only allow jumping when grounded, fixes bugs in jumping to the player
def override(player):
    if not player.grounded and player.y > 0:
        player.y -= 0.1
        player.position = Vec3(round(player.x, 3), round(player.y, 3), round(player.z, 3)) 