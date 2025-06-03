from ursina import * # Ursina library
import random # Random library

def random_spawn_enemy(player):
    """Spawns enemies at random positions within a specified range (-50 to 50 on x and z axes)."""
    try:
        x = random.uniform(-50, 50) # Random x-coordinate
        z = random.uniform(-50, 50) # Random z-coordinate
        enemy = Entity(model='cube', color=color.blue, collider = 'box', scale = (1, 2, 1), position=(x, 1, z), health=100) # Creates an enemy at a random position
        enemy.collider.visible = True # Makes the collider visible
        enemy.add_script(GroundedSmoothFollow(target=player, offset=[0, 0, 0], speed=10)) # Adds a script to follow the player
        return enemy # Returns the created enemy entity
    except Exception as e:
        print(f"Error spawning random enemy: {e}")


# Sprinting function (Works)
def sprint(player, key):
    """Function to handle sprinting mechanics for the player."""
    try:
        if key == "shift": # Checks if the shift key is pressed
            player.speed = 20 # Sets player speed to 20 when sprinting
        elif key == "shift up": # Checks if the shift key is released
            player.speed = 10 # Resets player speed to 10 when not sprinting
    except Exception as e:
        print(f"Error in sprint function: {e}")

# Spawn Enemy function
def spawn_enemy(player):
    """Function to spawn an enemy at a given position with specified properties."""
    try:
        enemy = Entity(model='cube', color=color.blue, collider = 'box', scale = (1, 2, 1), position=(5, 1, 5), health=100) # Creates an enemy entity
        enemy.collider.visible = True # Makes the collider visible
        enemy.add_script(GroundedSmoothFollow(target=player, offset=[0, 0, 0], speed=10)) # Adds a script to follow the player
        return enemy # Returns the created enemy entity
    except Exception as e:
        print(f"Error spawning enemy: {e}")

# Get gun function (Works)
def get_gun(player, gun):
    """Function to equip a gun to the player."""
    try:
        gun.parent = camera # Sets the parent of the gun to the camera
        gun.position = Vec3(0,-.75,.5) # Sets the position of the gun relative to the camera
        player.gun = gun # Assigns the gun to the player
        gun.collider = None # Removes the collider from the gun to prevent collisions
    except Exception as e:
        print(f"Error getting gun: {e}")

# Made an inherited class from Entity to create a bullet that moves in the direction it was shot
class Bullet(Entity):
    """A class inherited from Entity, being a bullet with properties such as position, direction, and collision."""
    def __init__(self, position, direction): # Position and direction are passed as parameters
        try:
            super().__init__(parent=scene, model='cube', scale=1, color=color.black, collider='box', position = position) # Initializes the bullet entity with a cube model, black color, and box collider
            self.direction = direction.normalized() # Sets the direction of the bullet
            self.look_at(position + self.direction) # Makes the bullet look at the position it is moving towards
        except Exception as e:
            print(f"Error initializing Bullet: {e}")

    def update(self):
        """Updates the bullets position and checks for collisions."""
        try:
            # Moves the bullet in the direction it is facing, checks for collisions, destroys if it hits something or if it goes 1000 units away from the camera
            self.position += self.direction * 1000 * time.dt # Moves the bullet in the direction it is facing
            hit_info = self.intersects() # Checks for collisions with other entities
            if hit_info.hit: # If the bullet hits something
                destroy(self) # Destroy the bullet if it hits something
                return # Exit the update method, prevent further movement
            if distance(self.position, camera.world_position) > 1000: # Checks if the bullet is further than 1000 units away from the camera
                destroy(self) # Destroys the bullet if it is too far away from the camera
        except Exception as e:
            print(f"Error updating Bullet: {e}")

# Controls gun shooting, such as sound, gun color, bullets, and bullet shooting
def shoot(gun, key):
    """Function to spawn bullets when the left mouse button is pressed."""
    try:
        if key == 'left mouse down': # If the left mouse button is pressed
            Audio("assets/laser_sound.wav") # Play the laser sound
            gun.blink(color.red) # Makes the gun blink red to indicate shooting
            offset = Vec3(0, 0, 0) # Offset for the bullet position is straight in front of the gun
            Bullet(position=gun.world_position + gun.forward * 1.5 + offset, direction=gun.forward) # Creates a bullet entity at the position of the gun
    except Exception as e:
        print(f"Error in shoot function: {e}")


# Controls enemy damaging player and death
def enmdmg(player, healthbar, enemy): 
    """Function to handle enemy damage and death"""
    try:
        if distance(player.position, enemy.position) < 2: 
            healthbar.value -= 1 # Decreases the health bar value by 1
        if healthbar.value <= 0: # Checks if the health bar value is less than or equal to 0
            quit() # Quit the game if the healthbar is empty (Will change to game over screen later)
    except Exception as e:
        print(f"Error in enmdmg function: {e}")


def plrdmg(player, enemy):
    """Function to handle player damage to the enemy. Uses raycasting to detect if it hit anything and if it is the enemy."""
    try:
        hit_info = raycast(camera.world_position, camera.forward, distance=500, ignore=[player], debug=False) # Raycasts from the camera's position in the direction it is facing
        if hit_info.hit and hit_info.entity == enemy: # Checks if the raycast hit an entity
            enemy.blink(color.red) # Blinks the enemy red to indicate it has been hit
            invoke(setattr, enemy, 'color', color.blue, delay=0.15) # Delay the color change to blue after being hit
            enemy.health -= 5 # Decreases the enemy's health by 5
            print(f"Enemy hit! Health: {enemy.health}") # Prints the enemy health to the console
            if enemy.health <= 0: # Checks if the enemy's health is less than or equal to 0
                print("Enemy defeated!") # Prints a message to the console when the enemy is defeated
                destroy(enemy) # Destroys the enemy entity when defeated
                return True # Returns True if enemy is defeated, for potential actions
    except Exception as e:
        print(f"Error in plrdmg function: {e}")

# Only allow jumping when grounded, fixes bugs in jumping to the player
def override(player):
    """Function to override the player's jumping behavior to ensure it only occurs when grounded."""
    try:
        # Checks if the player is not grounded and is above ground level, then it moves the player down
        # and rounds the players position to 3 decimal places to prevent no-clipping.
        if not player.grounded and player.y > 0:
            player.y -= 0.1
            player.position = Vec3(round(player.x, 3), round(player.y, 3), round(player.z, 3))
    except Exception as e:
        print(f"Error in override function: {e}")

def menu(start_game, survival_game, instructions):
    """Function to handle the main menu of the game."""
    try:
        menu_bg = Entity(parent = camera.ui, model = 'quad', scale = (0.7,0.5), color = color.dark_gray, z = 1) # Menu BG

        title = Text(text="Generic FPS Game.py", scale = 2, y = 0.25, parent = camera.ui, color = color.azure, background=True, origin=(0,0)) # Title

        start_button = Button(text="Simulator Game", scale=(0.3, 0.12), y=0, x=-0.18, color= color.azure, parent=camera.ui) # Start Button for Simulator Game
        survivalplay_button = Button(text="Survival Game", scale=(0.3, 0.12), y=0, x=-0.50, color = color.azure, parent=camera.ui) # Start Button for Survival Game
        tutorial_button = Button(text="Tutorial", scale=(0.3, 0.12), y=0, x=0.50, color= color.azure, parent=camera.ui) # Tutorial Button
        exit_button = Button(text="Exit Game", scale=(0.3, 0.12), y=0, x=0.18, color = color.red, parent=camera.ui) # Exit Button

        start_button.on_click = lambda: (destroy(menu_bg), destroy(title), destroy(start_button), destroy(exit_button), destroy(survivalplay_button), destroy(tutorial_button), start_game(), print("Game Started!")) # Calls the start_game function in Sprint2.py when the start button is clicked
        survivalplay_button.on_click = lambda: (destroy(menu_bg), destroy(title), destroy(start_button), destroy(exit_button), destroy(survivalplay_button), destroy(tutorial_button), survival_game(), print("Freeplay Mode Activated!")) # Calls the survival_game function in Sprint2.py when the survival button is clicked
        tutorial_button.on_click = lambda: (destroy(menu_bg), destroy(title), destroy(start_button), destroy(exit_button), destroy(survivalplay_button), destroy(tutorial_button), instructions(), print("Tutorial Mode Activated!")) # Calls the instructions function in Sprint2.py when the tutorial button is clicked
        exit_button.on_click = application.quit # Exits the game when the exit button is clicked
    except Exception as e:
        print(f"Error in menu function: {e}")
        
    
# Make sure the enemy is always grounded and never no-clipping
class GroundedSmoothFollow(SmoothFollow):
    # Make a subclass using inhertance from the SmoothFollow class in Ursina
    """A subclass/childclass of SmoothFollow from Ursina that ensures the entity not only follows the target but also stays grounded."""
    # We use a form of polymorphism here to override the update method of SmoothFollow
    def update(self):
        try:
            min_distance = 2  # Adjust as needed
            dist = distance(self.target.position, self.entity.position)
            if dist > min_distance:
                direction = Vec3(self.target.x - self.entity.x, 0, self.target.z - self.entity.z).normalized() # Calculates the direction vector from the target to the entity, ignoring the y axis to keep the entity grounded
                self.entity.position += direction * self.speed * time.dt # Moves the entity towards the target at a specified speed, ensuring it stays grounded by not changing the y position
        except Exception as e:
            print(f"Error in GroundedSmoothFollow update method: {e}")