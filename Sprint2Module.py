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
        bullet.animate_position(bullet.position + (bullet.forward * 1000), curve=curve.linear, duration=0.5)
        destroy(bullet, delay=0.5)


# Controls enemy damaging player and death
def enmdmg(player, healthbar, enemy):
    """Function to handle enemy damage and death"""
    if player.intersects().hit and player.intersects().entity == enemy:
        healthbar.value -= 5
    if healthbar.value == 0:
        quit()

# Checks if the player does damage to the enemy with the bullets
def plrdmg(player, enemy):
     """Function to handle player damage to the enemy. Uses raycasting to detect if it hit anything and if it is the enemy."""
     hit_info = raycast(camera.world_position, camera.forward, distance=500, ignore=[player], debug=False)
     if hit_info.hit and hit_info.entity == enemy:
        enemy.blink(color.red)
        invoke(setattr, enemy, 'color', color.blue, delay=0.15)
        enemy.health -= 5
        print(f"Enemy hit! Health: {enemy.health}")
        if enemy.health <= 0:
            print("Enemy defeated!")
            destroy(enemy)
        
# Only allow jumping when grounded, fixes bugs in jumping to the player
def override(player):
    """Function to override the player's jumping behavior to ensure it only occurs when grounded."""
    # Checks if the player is not grounded and is above ground level, then it moves the player down
    # and rounds the players position to 3 decimal places to prevent no-clipping.
    if not player.grounded and player.y > 0:
        player.y -= 0.1
        player.position = Vec3(round(player.x, 3), round(player.y, 3), round(player.z, 3))

def menu(start_game):
    """Function to handle the main menu of the game."""

    menu_bg = Entity(parent = camera.ui, model = 'quad', scale = (0.7,0.5), color = color.dark_gray, z = 1)

    title = Text(text="Generic FPS Game.py", scale = 2, y = 0.25, parent = camera.ui, color = color.azure, background=True, origin=(0,0))

    start_button = Button(text="Start Game", scale=(0.3, 0.12), y=0, x=-0.18, parent=camera.ui)
    freeplay_button = Button(text="Freeplay", scale=(0.3, 0.12), y=0, x=-0.50, parent=camera.ui)
    tutorial_button = Button(text="Tutorial", scale=(0.3, 0.12), y=0, x=0.50, parent=camera.ui)
    exit_button = Button(text="Exit Game", scale=(0.3, 0.12), y=0, x=0.18, parent=camera.ui)

    
    start_button.on_click = lambda: (destroy(menu_bg), destroy(title), destroy(start_button), destroy(exit_button), destroy(freeplay_button), destroy(tutorial_button), start_game(), print("Game Started!"))
    freeplay_button.on_click = lambda: (destroy(menu_bg), destroy(title), destroy(start_button), destroy(exit_button), destroy(freeplay_button), destroy(tutorial_button), print("Freeplay Mode Activated!"))
    tutorial_button.on_click = lambda: (destroy(menu_bg), destroy(title), destroy(start_button), destroy(exit_button), destroy(freeplay_button), destroy(tutorial_button), print("Tutorial Mode Activated!"))
    exit_button.on_click = application.quit
    
    
# Make sure the enemy is always grounded and never no-clipping
class GroundedSmoothFollow(SmoothFollow):
    # Make a subclass using inhertance from the SmoothFollow class in Ursina
    """A subclass/childclass of SmoothFollow from Ursina that ensures the entity not only follows the target but also stays grounded."""
    # We use a form of polymorphism here to override the update method of SmoothFollow
    def update(self):
        # Makes a target position for the entity to follow, and also ensures it stays grounded by setting the y position to the entity's y position whereas
        # the x and z positions are set to the player's x and z positions.
        target_pos = Vec3(self.target.x, self.entity.y, self.target.z)
        # Uses the lerp function (linear interpolation) to smoothly move the entity towards the target position at a speed defined by self.speed.
        # The function takes 3 arguments, the current entity position, the target which we want, and the delta time multiplied by the speed
        # for the speed of the movement to be smooth.
        # We multiply the time.dt (delta time) by self.speed to ensure the movement is frame rate centralized.
        self.entity.position = lerp(self.entity.position, target_pos, time.dt * self.speed) 