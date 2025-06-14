from ursina import * # Ursina library
import random # Random library
from ursina.prefabs.first_person_controller import FirstPersonController # First Person Controller from Ursina
from ursina.prefabs.health_bar import HealthBar # Health Bar from Ursina

def random_spawn_enemy(player):
    """Spawns enemies at random positions within a specified range (-50 to 50 on x and z axes)."""
    try:
        x = random.uniform(-50, 50) # Random x-coordinate
        z = random.uniform(-50, 50) # Random z-coordinate
        randhealth = random.randint(75, 200)
        enemy = Entity(model='assets/AlienGrub1.obj', texture='assets/AlienGrub1_Base_Diffuse.jpg', collider = 'box', scale = (0.025, 0.05, 0.025), position=(x, 1, z), health=randhealth) # Creates an enemy at a random position
        enemy.add_script(GroundedSmoothFollow(target=player, offset=[0, 0, 0], speed=10)) # Adds a script to follow the player using GroundedSmoothFollow
        return enemy # Returns the created enemy entity
    except Exception as e: # Error handling
        print(f"Error spawning random enemy: {e}")

# Spawn Enemy function
def spawn_enemy(player):
    """Function to spawn an enemy at a given position with specified properties."""
    try:
        enemy = Entity(model='assets/AlienGrub1.obj', texture='assets/AlienGrub1_Base_Diffuse.jpg', collider = 'box', scale = (0.025, 0.05, 0.025), position=(5, 1, 5), health=100) # Creates an enemy entity
        enemy.add_script(GroundedSmoothFollow(target=player, offset=[0, 0, 0], speed=10)) # Adds a script to follow the player using GroundedSmoothFollow
        return enemy # Returns the created enemy entity
    except Exception as e: # Error handling
        print(f"Error spawning enemy: {e}")

# Menu function
def menu(start_game, survival_game, instructions):
    """Function to handle the main menu of the game."""
    try:
        menu_bg = Entity(parent = camera.ui, model = 'quad', scale = (0.7,0.5), color = color.dark_gray, z = 1) # Menu BG

        title = Text(text="Doom.py", scale = 2, y = 0.25, parent = camera.ui, color = color.azure, background=True, origin=(0,0)) # Title for the game

        start_button = Button(text="Simulator Game", scale=(0.3, 0.12), y=0, x=-0.18, color= color.azure, parent=camera.ui) # Start Button for Simulator Game
        survivalplay_button = Button(text="Survival Game", scale=(0.3, 0.12), y=0, x=-0.50, color = color.azure, parent=camera.ui) # Start Button for Survival Game
        tutorial_button = Button(text="Tutorial", scale=(0.3, 0.12), y=0, x=0.50, color= color.azure, parent=camera.ui) # Tutorial Button
        exit_button = Button(text="Exit Game", scale=(0.3, 0.12), y=0, x=0.18, color = color.red, parent=camera.ui) # Exit Button

        start_button.on_click = lambda: (destroy(menu_bg), destroy(title), destroy(start_button), destroy(exit_button), destroy(survivalplay_button), destroy(tutorial_button), start_game(), print("Game Started!")) # Calls the start_game function in Sprint2.py when the start button is clicked
        survivalplay_button.on_click = lambda: (destroy(menu_bg), destroy(title), destroy(start_button), destroy(exit_button), destroy(survivalplay_button), destroy(tutorial_button), survival_game(), print("Freeplay Mode Activated!")) # Calls the survival_game function in Sprint2.py when the survival button is clicked
        tutorial_button.on_click = lambda: (destroy(menu_bg), destroy(title), destroy(start_button), destroy(exit_button), destroy(survivalplay_button), destroy(tutorial_button), instructions(), print("Tutorial Mode Activated!")) # Calls the instructions function in Sprint2.py when the tutorial button is clicked
        exit_button.on_click = application.quit # Exits the game when the exit button is clicked
    except Exception as e: # Error handling
        print(f"Error in menu function: {e}")

# Made an inherited class from Entity to create a bullet that moves in the direction it was shot
class Bullet(Entity):
    """A class inherited from Entity, being a bullet with properties such as position, direction, and collision."""
    def __init__(self, position, direction): # Position and direction are passed as parameters
        try:
            super().__init__(parent=scene, model='cube', scale=1, color=color.black, collider='box', position = position) # Initializes the bullet entity with a cube model, black color, and box collider
            self.direction = direction.normalized() # Sets the direction of the bullet
            self.look_at(position + self.direction) # Makes the bullet look at the position it is moving towards
        except Exception as e: # Error handling
            print(f"Error initializing Bullet: {e}")

    # Class method that updates the bullets position after predetermined attributes
    def update(self):
        """Updates the bullets position and checks for collisions."""
        try:
            self.position += self.direction * 1000 * time.dt # Moves the bullet in the direction it is facing
            hit_info = self.intersects() # Checks for collisions with other entities
            if hit_info.hit: # If the bullet hits something
                destroy(self) # Destroy the bullet if it hits something
                return # Exit the update method, prevent further movement
            if distance(self.position, camera.world_position) > 1000: # Checks if the bullet is further than 1000 units away from the camera
                destroy(self) # Destroys the bullet if it is too far away from the camera
        except Exception as e: # Error handling
            print(f"Error updating Bullet: {e}")

# Player class inherited from FirstPersonController
class Player(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(model='cube', color=color.clear, speed=10, scale_y=2, collider='box', **kwargs) # Uses super to set attributes to certain values and store in dict using **kwargs
        self.gun = None # Initialises the player to not have a gun
        self.healthbar = HealthBar(bar_color=color.lime.tint(-.25), roundness=.5, highlight_color=color.yellow.tint(-.2)) # Initialises a healthbar for the player
        scene.player = self

    # Sprint method for the class
    def sprint(self, key):
        """Function to handle sprinting mechanics for the player."""
        try:
            if key == "shift": # Checks if the shift key is pressed
                self.speed = 20 # Sets player speed to 20 when sprinting
            elif key == "shift up": # Checks if the shift key is released
                self.speed = 10 # Resets player speed to 10 when not sprinting
        except Exception as e: # Error handling
            print(f"Error in sprint function: {e}")

    # Fixes the player's jumps so it doesn't glitch out
    def override(self):
        """Function to override the player's jumping behavior to ensure it only occurs when grounded."""
        try:
            if not self.grounded and self.y > 0: # If the player is not grounded and is above ground level
                self.y -= 0.1 # Move the player down -.1
                self.position = Vec3(round(self.x, 3), round(self.y, 3), round(self.z, 3)) # Round coords of the player to ensure no no-clipping
        except Exception as e: # Error handling
            print(f"Error in override function: {e}")

    # Handles player damage from enemies
    def enmdmg(self, amount):
        """Function to handle player damage from enemies."""
        try:
            self.healthbar.value -= amount # Subtracts the healthbar amount
            if self.healthbar.value <= 0: # If the healthbar amount is less than or equal to 0
                quit() # Quit the game as the player has died
        except Exception as e: # Error handling
            print(f"Error in enmdmg function: {e}")

    # Handles player damage to the enemy
    def plrdmg(self, enemy, damage):
        """Function to handle player damage to the enemy. Uses raycasting to detect if it hit anything and if it is the enemy."""
        try:
            hit_info = raycast(camera.world_position, camera.forward, distance=500, ignore=[self], debug=False) # Raycasts from the camera's position in the direction it is facing
            if hit_info.hit and hit_info.entity == enemy: # Checks if the raycast hit an entity
                enemy.blink(color.red) # Blinks the enemy red to indicate it has been hit
                invoke(setattr, enemy, 'color', color.blue, delay=0.15) # Delay the color change to blue after being hit
                enemy.health -= damage # Decreases the enemy's health by gun damage
                print(f"Enemy hit! Health: {enemy.health}") # Prints the enemy health to the console
                if enemy.health <= 0: # Checks if the enemy's health is less than or equal to 0
                    print("Enemy defeated!") # Prints a message to the console when the enemy is defeated
                    destroy(enemy) # Destroys the enemy entity when defeated
                    return True # Returns True if enemy is defeated, for potential actions
        except Exception as e: # Error handling
            print(f"Error in plrdmg function: {e}")
      
# Make sure the enemy is always grounded and never no-clipping
class GroundedSmoothFollow(SmoothFollow):
    # Make a subclass using inhertance from the SmoothFollow class in Ursina
    """A subclass/childclass of SmoothFollow from Ursina that ensures the entity not only follows the target but also stays grounded."""
    # We use a form of polymorphism here to override the update method of SmoothFollow
    def update(self):
        try:
            direction = Vec3(self.target.x - self.entity.x, 0, self.target.z - self.entity.z).normalized() # Calculates the direction vector from the target to the entity, ignoring the y axis to keep the entity grounded
            self.entity.position += direction * self.speed * time.dt # Moves the entity towards the target at a specified speed, ensuring it stays grounded by not changing the y position
        except Exception as e: # Error handling
            print(f"Error in GroundedSmoothFollow update method: {e}")

# Gun class that the player can equip and shoot inherited from button
class Gun(Button):
    """A subclass/childclass of Button that allows the user to press it like a button ingame and pick it up, also allowing for shooting"""
    def __init__(self, model, color, position, scale, damage=50, fire_rate=0.5, **kwargs): # Sets some attributes in a dict using **kwargs and defines some beforehand
        super().__init__(parent=scene, model=model, color=color, origin_y=-.5, position=position, scale=scale, **kwargs) # Values added to keys defined in attributes beforehand using super avoiding redundancy
        # New attributes for the gun
        self.damage = damage 
        self.fire_rate = fire_rate
        self.last_shot_time = 0 

    def shoot(self):
        """Shoots the players gun."""
        from time import time # Time to check the last shot time and maintain firerate
        try:
            if time() - self.last_shot_time >= self.fire_rate: # Checks if the time since the last shot is greater than or equal to the fire rate
                Audio("assets/laser_sound.wav") # Play audio
                self.blink(color.red) # Blinks the gun red
                offset = Vec3(0, 0, 0) # Offset for the bullet position is straight in front of the gun
                Bullet(position=self.world_position + self.forward * 1.5 + offset, direction=self.forward) # Creates a bullet entity at the position of the gun
                self.last_shot_time = time() # Updates the last shot time to the current shot
                return True # Tells that the gun was successfully shot
            return False # No shot was fired due to fire rate restriction
        except Exception as e: # Error handling
            print(f"Error in Gun shoot method: {e}")
            return False # Returns false if there was an error in shooting
        
    def get_gun(self, player):
        """Function to equip a gun to the player."""
        try:
            if player.gun: # Checks if the player has a gun
                player.gun.drop_gun(player) # Drops the players current gun using the drop_gun function
            self.parent = camera # Sets the parent of the new gun to the camera
            self.position = Vec3(0,-.80,1) # Sets the position of the new gun relative to the camera
            player.gun = self # Assigns the new gun to the player
            self.collider = None # Removes the collider from the new gun to prevent collisions
        except Exception as e: # Error handling
            print(f"Error getting gun: {e}")
    
    def drop_gun(self, player):
        """Function to drop a gun from the player to the ground"""
        try:
            if self.parent == camera: # If the player has a gun
                self.parent = scene # Set the gun to the scene
                player.gun = None # Unequips the gun from the player
                drop_point = player.position + Vec3(0, 1, 1) # Drops it near the player a little higher
                self.position = drop_point # Sets the position to the drop point
                self.collider = 'box' # Gives the collider back
        except Exception as e: # Error handling
            print(f"Error dropping gun: {e}")

class Shotgun(Gun):
    """Inherited from the Gun class, this gun incorporates a multiple bullet approach to make it look aesthetic, as well as random damage"""
    def __init__(self, model, color, position, scale, damage=50, fire_rate=0.7, **kwargs): # Uses **kwargs to set predetermined values and keys in a dict
        super().__init__(model=model, color=color, position=position, scale=scale, damage=damage, fire_rate=fire_rate, **kwargs) # Uses super to assign some of these values in the **kwargs constructor and avoid redundancy

    def shoot(self):
        """Shoots the players gun."""
        from time import time
        try:
            if time() - self.last_shot_time >= self.fire_rate: # Checks if the time since the last shot is greater than or equal to the fire rate
                Audio("assets/laser_sound.wav") # Plays audio
                self.blink(color.orange) # Blinks the gun orange
                random_damage = random.randint(90, 120) # Random damage variable which resets every time we check fire rate
                self.damage = random_damage # Sets damage to random damage
                for i in range(5):  # Spawns 5 bullets
                    offset = Vec3(0, 0, i * 0.0001)  # Offset of the bullets
                    Bullet(position=self.world_position + self.forward * 1.5 + offset, direction=self.forward + Vec3(random.uniform(-0.02, 0.02), 0, random.uniform(-0.02, 0.02))) # Random coordinates where the shotgun shoots
                self.last_shot_time = time() # Updates the last shot time to the current shot
                return True # Tells that the gun was successfully shot
            return False # No shot was fired due to fire rate restriction
        except Exception as e: # Error handling
                print(f"Error in Gun shoot method: {e}")
                return False # Returns false if there was an error in shooting
        
    def get_gun(self, player):
        """Function to equip a gun to the player."""
        try:
            if player.gun: # If the player has a gun
                player.gun.drop_gun(player) # Drops the old gun
            self.parent = camera # Sets the parent of the new gun to the camera
            self.position = Vec3(0,-.75,.5) # Sets the position of the new gun relative to the camera
            player.gun = self # Assigns the new gun to the player
            self.collider = None # Removes the collider from the new gun to prevent collisions
        except Exception as e: # Error handling
            print(f"Error getting gun: {e}")
    
    def drop_gun(self, player):
        """Function to drop a gun from the player to the ground"""
        try:
            if self.parent == camera: # If the gun is equipped to the camera
                self.parent = scene # Set the gun parent to the scene
                drop_point = player.position + Vec3(0, 1, 1) # Determines drop point close to player
                self.position = drop_point # Sets position to drop point
                self.collider = 'box' # Sets box collider
        except Exception as e: # Error handling
            print(f"Error dropping gun: {e}")

class Minigun(Gun):
    def __init__(self, model, color, position, scale, damage=5, fire_rate=0.1, **kwargs): # Uses **kwargs to store key and values of attributes
        super().__init__(model=model, color=color, position=position, scale=scale, damage=damage, fire_rate=fire_rate, **kwargs) # Uses super to forward certain attribute values to the dict

    def shoot(self):
        from time import time
        try:
            if time() - self.last_shot_time >= self.fire_rate: # Checks if the time since the last shot is greater than or equal to the fire rate
                Audio("assets/laser_sound.wav") # Plays Audio
                self.blink(color.red) # Blinks gun red
                offset = Vec3(0, 0, 0) # Offset for the bullet position is straight in front of the gun
                Bullet(position=self.world_position + self.forward * 1.5 + offset, direction=self.forward) # Creates a bullet entity at the position of the gun
                self.last_shot_time = time() # Updates the last shot time to the current shot
                return True # Tells that the gun was successfully shot
            return False # No shot was fired due to fire rate restriction
        except Exception as e:
            print(f"Error in Gun shoot method: {e}")
            return False # Returns false if there was an error in shooting
        
    def get_gun(self, player):
        """Function to equip a gun to the player."""
        try:
            if player.gun: # If the player has a gun
                player.gun.drop_gun(player) # Drops the players old gun
            self.parent = camera # Sets the parent of the new gun to the camera
            self.position = Vec3(0,-1.10,.5) # Sets the position of the new gun relative to the camera
            player.gun = self # Assigns the new gun to the player
            self.collider = None # Removes the collider from the new gun to prevent collisions
        except Exception as e:
            print(f"Error getting gun: {e}")

    def drop_gun(self, player):
        """Function to drop a gun from the player to the ground"""
        try:
            if self.parent == camera: # If the player's gun is equipped to the camera
                self.parent = scene # Sets the players gun to the scene
                drop_point = player.position + Vec3(0, 1, 1) # Determines drop point close to the player
                self.position = drop_point # Sets position to the drop point
                self.collider = 'box' # Sets collider for the gun
        except Exception as e: # Error handling
            print(f"Error dropping gun: {e}")

class HealthPack(Entity):
    def __init__(self, position, heal_amount = 25):
        super().__init__(parent=scene, model='assets/HealthPack.Obj', texture = "assets/HealthPack_Albedo.tga", collider='box', position=position, scale=(0.02, 0.05, -0.02))
        self.heal_amount = heal_amount

    def heal(self):
        """Checks if the player hits the healthpack, and if so heals them"""
        try:
            scene.player.healthbar.value = min(scene.player.healthbar.value + self.heal_amount, 100)
            Audio('assets/laser_sound.wav')
            destroy(self)
            print(f"Sucessfully healed! Health: {scene.player.healthbar.value}")
            return True
        except Exception as e:
            print(f"Error in heal method: {e}")
            return False



            
            