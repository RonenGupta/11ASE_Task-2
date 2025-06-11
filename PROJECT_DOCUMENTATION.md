# Year 11 Accelerated Software Engineering Assessment Task 2 - First Person Shooter Simulator
### By Ronen

# Sprint 1
## Requirements Definition
***
### Functional Requirements

- Data Retrieval: The user must be able to view a gun or similar shooter on the side/middle of their screen, a crosshair in the middle.

- User Interface: The user must have a working PC or laptop with a keyboard, mouse and be aware on basic WASD and mouse clicking controls.

- Data Display: The user may be able to view kill count, ammo amount, possible a hotbar with weapons and ammo amounts corresponding to certain weapons, and other variables on the upper sides of the screen will have to be hidden.

***
### Non-Functional Requirements
- Performance: The system needs to load up in under 10 seconds, have at least above 100 FPS, and all functions must function.

- Reliability: The system must not include too many major bugs, and the data should be reliable in order to control realistic FPS physics.

- Usability and Accessibility: The system must be extremely easy to get a hold of. WASD, space and mouse controls will be the only controls for playing the game, and any other controls can be accessed from the instructions tab.
***
## Determining Specifications
***
### Functional Specifications
- User Requirements: The user must be able to move around and shoot with WASD, Jump and mouse controls as well as pick up and shoot a gun.

- Inputs and Outputs: Will need to accept keyboard controls such as WASD and Jump as well as left click and moving the mouse around.

- Core Features: The program must be able to provide a fun and enjoyable FPS simulator experience, with enemies and a custom simulation gamemode where the player can spawn enemies at will.

- User Interaction: Users can interact with the system through the Ursina module, notably used for python game making, and a README can be provided to help users navigate.

- Error Handling: The system may fail to launch, crash mid-way, or miscellaneous errors may occur from runtime to developer based issues during launch.
***
### Non-Functional Specifications

- Performance: The system should be able to load in less than 30 seconds, and user input must not be delayed and FPS should be high.

- Usability/Accessibility: Possibly add a UI main menu if supported in Ursina, tutorial tab, free play (If wanting to test all weapons, gamemodes). 

- Reliability: UI design and map design will be an issue, and miscalculations along the way would possibly occur in the development process, however these will be addressed firmly due to their difficulty.
***
### Use Case

- Actor: User (Gamer/FPS Game Fan)

- Preconditions: Internet access; required specs for game, modules installed, controls understood.

- Main Flow:

1. Launch Game: User launches the game and sees a menu screen with 3 tabs. Play, tutorial, and exit.

2. Clicks Play: User clicks play (As it is the normal option) and spawns in a map with a gun on the floor, and on the UI appears his health bar.

3. Simulation: After the user picks up the gun, they can press keys on their keyboard to spawn corresponding enemies, or an enemy to simulate an FPS experience.

4. Game End: After the game has ended, (The user has died ingame) the game shows the scores of the player (This may not be possible due to how Ursina renders certain game objects and deletes them)

5. Loop: The user is then prompted to the menu screen again with the same 3 tabs, leading to a loop until they press the exit button, where they can view the tutorial or play before exiting.

- Postconditions: User has played the simulator, understands how to play the game and has viewed their score.

***
## Design
***
## Build and Test
***
### Sprint 1 - FPS Text Based GUI Modularized with a Wave Based Gamemode

- Sprint 1 README.md
```python
# Year 11 Accelerated Software Engineering Assessment Task 2 FPS Game - Sprint 1

### Author
Ronen Gupta

## Features

- Main Menu: Choose between 4 choices, Play, Free Play, View the Tutorial, or exit the game.
- Play Mode: Standard FPS gameplay with 5 moves, but text based.
- Free Play Mode: Try from 5 weapons in text based GUI and practice shooting.
- Tutorial: View the controls for the text-based main game.
- Exit: Exit the game.

## Requirements

- To run this program, you need to install the following dependencies:
- Python 3.8 or higher
- [Ursina Engine](https://www.ursinaengine.org/) (If you want to try main.py, but Sprint 2 will contain this)

### Install dependencies
To install the required dependencies, you can run:

```bash
pip install -r requirements.txt
```
- Sprint1Module.py
```python
def show_menu():
    """Displays the main menu of the game."""
    print("==================================")
    print("Welcome to Just a normal FPS game!")
    print("==================================")
    
    
def show_options():
    """Displays the options available in the game."""
    print("- Play: Play the normal game!")
    print("- Tutorial: Understand how to play the game!")
    print("- Free Play: Play the game with every weapon and infinite waves!")
    print("- Exit: Exit the game!")
 
    

def show_Play(main):
    """Starts the main game function."""
    print("==================================")
    counter = 0 # Counter to track moves (Will be changed to a health bar/wave counter)
    gunpickup = int(input("Ready to play the game? Press 1 to pick up the gun or 2 to exit! "))
    if gunpickup == 1: # If the player picks up the gun
                    while counter != 5: # While moves are less than 5
                        # Instructions
                        print("- Move: Press 1 to move in a random direction!")
                        print("- Shoot: Press 2 to shoot an enemy!")
                        moves =  int(input("What do you want to do? ")) # Asks the user for their choice
                        if moves == 1:
                            counter += 1 # Adds 1 to the counter every move
                            print("You move north, east, south or west!")
                        elif moves == 2:
                            counter += 1 # Adds 1 to the counter every move
                            print("You shoot an enemy!")
                        else:
                             print("Invalid option!")
                    print("Game Over!")
                    main() # Calls the main function again

    if gunpickup == 2: # Exit the game
         main()

def show_Tutorial(main):
     """Displays the tutorial for the game."""
     print("==============================")
     print("===========Tutorial===========")
     print("- Move: Press 1 to move in a random direction!")
     print("- Shoot: Press 2 to shoot an enemy!")
     main() # Calls the main function after viewing

def show_freeplay(main):
     """Starts the free play mode of the game."""
     print("==================================")
     choice1 = input("Welcome to free play! Would you like to choose between weapons or exit? (Weapons or Exit are the choices) ") # Choose between weapons or exit
     if choice1.lower() == "weapons":
          weapons = {1: "Machine Gun", 2: "Submachine Gun", 3: "Shotgun", 4: "Pistol", 5: "Rocket Launcher"} # Dictionary of weapons and numbers
          print("What weapon would you like to choose? Pick a number: (1 - Machine Gun, 2 - Submachine Gun, 3 - Shotgun, 4 - Pistol, 5 - Rocket Launcher ") # Asks the user for their choice
          choice2 = int(input("Enter the number of your choice: ")) # Input the weapon number
          if choice2 in weapons: # Check if the key is in the dictionary
                    print(f"You have chosen the {weapons[choice2]}!") # Prints the weapon name from the dictionary
                    while True: # Until the user exits because its free play
                        action = input("What would you like to do? (Move, Shoot or Exit) ") # Asks the user for their choice of action
                        # Actions that can be taken
                        if action.lower() == "move":
                                print("You move north, east, south or west!")
                        elif action.lower() == "shoot":
                                print("You shoot an enemy!")
                        elif action.lower() == "exit":
                                main()
                        else:
                             print("Invalid option!")
                             show_freeplay() # Calls the show_freeplay function again
          else:
                    print("Invalid choice! Please try again.")
                    show_freeplay() # Calls the show_freeplay function again
     elif choice1.lower() == "exit": # If exit is chosen
            main() # Calls the main function again
```

- Sprint1.py
```python
from Sprint1Module import * # Imports all functions from the Sprint1Module

def main():
    """The main function that runs the text-based game."""
    show_menu() # Calls the show_menu function, displaying the menu
    show_options() # Calls the show_options function, displaying the options

    choice = str(input("Choose from Play, Tutorial, Free Play, or Exit! ")) # Asks the user for their choice
    
    if choice.lower() == "play": # Calls the show_Play function starts the game
        show_Play(main)
    elif choice.lower() == "tutorial": # Calls the show_Tutorial function, displays the tutorial
        show_Tutorial(main)
    elif choice.lower() == "free play": # Calls the show_freeplay function, starts free play
        show_freeplay(main)
    elif choice.lower() == "exit": # Calls the exit function, exits the game
        print("Thanks for playing!")
        exit()

main()
```
***
## Review
1. The program so far does not exactly follow the functional and non-functional requirements exactly, but provides a layout of what the finished program would possibly look like. This text based UI can be implemented into Ursina, as I have previously created a program suitable for the requirements of Sprint 2 with Ursina meeting most of the functional and non-functional requirements. So on and so forth, this program serves as a base for the finished product, being a text based GUI. I did not choose to do a UI based Sprint 1 due to Ursina's inbuilt Person class, which makes movement automatic and without the requirement of UI based buttons. I tried this and I found it useless, so I resorted to a text based GUI which allowed for a more dynamic approach to what would be the finished product. Sprint 2 may include some features from Sprint 1, but will not have all of them but will be in much better quality overall via Ursina Engine rendering.

2. The use case I created was perfectly replicated by the text based GUI I made, being incredibly similar in progression and only contains few minor changes (I made the main game end in 5 moves instead of waiting for the player to die as I would require Ursina). It takes input and produces output to a high standard, allowing for good behavourial replication.

3. Organisation and readability was distinctive in the text based GUI I made. With the use of modularization, docstrings, comments and function organisation/naming, it was simply impossible for not being able to understand the program. Overall, an outstanding use of quality in the GUI.

4. The next stage of development should immediately implement OOP and further complex aspects of classes. I had already created a base for Sprint 2 which I originally planned to be Sprint 1, however due to Sprint 1 requirements of text based GUI, I resorted to the main.py that is currently in the repository to be submitted as Sprint 2 after being modularised and tweaked a little more. This would add the inbuilt function for FPS controller, and I would also add a working gun (Pistol for now) and an interesting feature, a hookshot, allowing for the user to traverse quicker as if using a grapple gun, possibly a good idea for map design in the game. Overall, huge changes would occur when transitioning from text based to Ursina, and I would be ready to further enhance further from Sprint 2 onwards, adding a simulation, UI and other functional/non-functional requirements that the game requires.

5. Additional Note: I would change my idea from a wave based gamemode to a simulation gamemode, as a simulation would allow for a more dynamic user experience in sprint 2. This sprint was only for a planning and a base, but I will have created sprint 2 with a much more dynamic experience, via spawning enemies.
***
# Sprint 2
***
## Design
***
## Build and Test
***

### Sprint 2 Ursina FPS Game with GUI Modularized with a survival gamemode

- Sprint 2 README.md
```python
# Year 11 Accelerated Software Engineering Assessment Task 2 FPS Game - Sprint 2

### Author
Ronen Gupta

## Features

- Main Menu: Choose between 4 choices, Survival, Free Play, View the Tutorial, or exit the game.
- Survival Mode: Standard survival FPS gameplay, with hookshots and enemies, survive for as long as you can!
- Free Play Mode: Try spawning enemies of your own and try guns! (Will add more guns and enemies)
- Tutorial: View the controls for the gamemodes.
- Exit: Exit the game.

## Requirements

- To run this program, you need to install the following dependencies:
- Python 3.8 or higher
- [Ursina Engine](https://www.ursinaengine.org/)

### Install dependencies
To install the required dependencies, you can run:

```bash
pip install -r requirements.txt
```

- Sprint2Module.py
```python
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
        if player.intersects(enemy).hit: # Checks if the player collides with the enemy
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
            direction = Vec3(self.target.x - self.entity.x, 0, self.target.z - self.entity.z).normalized() # Calculates the direction vector from the target to the entity, ignoring the y axis to keep the entity grounded
            self.entity.position += direction * self.speed * time.dt # Moves the entity towards the target at a specified speed, ensuring it stays grounded by not changing the y position
        except Exception as e:
            print(f"Error in GroundedSmoothFollow update method: {e}")
```

- Sprint2.py
```python
from ursina import * # Ursina Library
from ursina.prefabs.first_person_controller import FirstPersonController # First Person Controller from Ursina
from ursina.prefabs.health_bar import HealthBar # Health Bar from Ursina
from Sprint2Module import get_gun, sprint, shoot, enmdmg, override, plrdmg, menu, spawn_enemy, random_spawn_enemy # Importing function from my Sprint2Module
import random # Import random for spawning enemies randomly

enemies_alive = [] # List to keep track of alive enemies
enemies_killed = 0 # Variable to keep track of killed enemies
time_elapsed = 0 # Variable to keep track of time elapsed in survival mode

def start_game():
    """Initialises the simulator gamemode, where the player can spawn enemies and shoot them, as well as use a hookshot."""

    global ground, input

    # Sync the game to the monitor's refresh rate, default 60hz to prevent screen tearing
    window.vsync = True

    # Initialises the program to be defaulted to fullscreen and window.borderless helps with mouse movement issues on macOS
    window.borderless = False 

    # Initialises the FirstPersonController class from the inbuilt ursina.prefabs.first_person_controller module as player, 
    # and the Entity class from the ursina module as ground, as well as the sky class and healthbar from the ursina.prefabs.health_bar module as HealthBar.
    player = FirstPersonController(model='cube', color=color.clear, speed = 10, scale_y=2, collider='box')
    healthbar = HealthBar(bar_color = color.lime.tint(-.25), roundness=.5, highlight_color = color.yellow.tint(-.2))
    ground = Entity(model='plane', collider='box',scale = 128, texture ='grass')
    Sky()

    # Initialises the player having no gun and makes a gun from the Button class and puts it on the ground, and calls the get_gun function
    player.gun = None
    gun = Button(parent=scene, model='assets/gun.obj', color=color.gold, origin_y=-.5, position=(3,0,3), scale=(.4,.4,.2))
    gun.on_click = lambda: get_gun(player, gun)

    # Makes a hookshot from the inbuilt ursina.prefabs.first_person_controller module as well as the functions
    hookshot_target = Button(parent=scene, model='cube', color=color.brown, position=(4,5,5))
    hookshot_target.on_click = Func(player.animate_position, hookshot_target.position, duration=.5, curve=curve.out_quad)

    # Text that shows the user the number of enemies currently alive and killed
    enemies_text = Text(text = f'Enemies Killed: {enemies_killed} | Enemies Alive: {len(enemies_alive)}', position = (0, 0.45), scale = 1, color = color.white)

    def update_enemy_texts():
        """Updates the enemies text to show the number of enemies killed and alive."""
        enemies_text.text = f'Enemies Killed: {enemies_killed} | Enemies Alive: {len(enemies_alive)}'

    # Handles other functions such as sprinting, shooting, enemy damaging, and an override function to prevent buggy player
    def input(key):
        global enemies_killed, enemies_alive
        """Function that handles the main input for the game, such as sprinting, shooting, and player/enemy damage."""
        sprint(player, key) # Sprint function
        override(player) # Prevents jumping when not grounded
        if player.gun == gun: # Checks if the player has a gun
            shoot(gun, key) # Allows the player to shoot the gun
        if key == 'left mouse down': # Checks if the left mouse button is pressed
            for enemy in enemies_alive[:]: # Loops through all alive enemies
                if plrdmg(player, enemy): # Checks if the player kills the enemy
                    enemies_alive.remove(enemy) # Removes the enemy from the alive list
                    enemies_killed += 1 # Adds to the enemies killed count
                    update_enemy_texts() # Updates the enemies text
        if key == 'e': # Checks if the E key is pressed
            enemy = spawn_enemy(player) # Spawns an enemy
            enemies_alive.append(enemy) # Adds the enemy to the alive list
            update_enemy_texts() # Updates the enemies text
        for enemy in enemies_alive: # Loops through all alive enemies
            enmdmg(player, healthbar, enemy) # Handles enemy damaging the player

def survival_game():
    """Initialises the survival gamemode, where the player must survive for as long as possible against endless waves of enemies."""
    global ground, input, time_elapsed, update, gun

    # Sync the game to the monitor's refresh rate, default 60hz to prevent screen tearing
    window.vsync = True

    # Initialises the program to be defaulted to fullscreen and window.borderless helps with mouse movement issues on macOS
    window.borderless = False 

    # Time elapsed variable
    time_elapsed = 0

    # Initialises the FirstPersonController class from the inbuilt ursina.prefabs.first_person_controller module as player, 
    # and the Entity class from the ursina module as ground, as well as the sky class and healthbar from the ursina.prefabs.health_bar module as HealthBar.
    player = FirstPersonController(model='cube', color=color.clear, speed = 10, scale_y=2, collider='box')
    healthbar = HealthBar(bar_color = color.lime.tint(-.25), roundness=.5, highlight_color = color.yellow.tint(-.2))
    ground = Entity(model='plane', collider='box',scale = 128, texture ='grass')
    Sky()

    # Initialises the player having a gun and makes a gun from the Button class and calls the get_gun function instantly
    gun = Button(parent=scene, model='assets/gun.obj', color=color.gold, origin_y=-.5, position=(3,0,3), scale=(.4,.4,.2))
    player.gun = gun
    get_gun(player, gun)

    # Makes a hookshot from the inbuilt ursina.prefabs.first_person_controller module as well as the functions
    hookshot_target = Button(parent=scene, model='cube', color=color.brown, position=(4,5,5))
    hookshot_target.on_click = Func(player.animate_position, hookshot_target.position, duration=.5, curve=curve.out_quad)

    # Enemies text which tracks the enemies killed and alive
    enemies_text = Text(text = f'Enemies Killed: {enemies_killed} | Enemies Alive: {len(enemies_alive)}', position = (0, 0.45), scale = 1, color = color.white)

    # Function that updates the enemies text
    def update_enemy_texts():
        """Updates the enemies text to show the number of enemies killed and alive."""
        enemies_text.text = f'Enemies Killed: {enemies_killed} | Enemies Alive: {len(enemies_alive)}'

    # Time text that tracks the elapsed time when the survival gamemode is selected
    time_text = Text(text = f'Elapsed Time: {int(time_elapsed)}', position = (0.5, 0.45), scale=1, color= color.white)

    # Updates the time elapsed per frame and the text
    def update_time_elapsed_texts():
        """Updates the elapsed time to show the time elapsed"""
        global time_elapsed
        time_elapsed += time.dt
        time_text.text = f'Elapsed time: {int(time_elapsed)}'

    # Spawns enemies randomly and adds them to a list, and tracks the alive enemies
    def spawn_enemies_randomly():
        """Spawns enemies randomly and adds them to the enemies_alive list."""
        enemy = random_spawn_enemy(player)
        enemies_alive.append(enemy)
        update_enemy_texts()
        invoke(spawn_enemies_randomly, delay=random.uniform(5, 12))

    # Calls the function
    spawn_enemies_randomly()

    # Updates the time every frame, using the unique update function in Ursina
    def update():
        update_time_elapsed_texts()

    # Controls the main functions of the game
    def input(key):
        global enemies_killed, enemies_alive
        """Function that handles the main input for the game, such as sprinting, shooting, and player/enemy damage."""
        sprint(player, key) # Sprint function
        override(player) # Prevents jumping when not grounded
        if player.gun == gun: # Checks if the player has a gun
            shoot(gun, key) # Allows the player to shoot the gun
        if key == 'left mouse down': # Checks if the left mouse button is pressed
            for enemy in enemies_alive[:]: # Loops through all alive enemies
                if plrdmg(player, enemy): # Checks if the player kills the enemy
                    enemies_alive.remove(enemy) # Removes the enemy from the alive list
                    enemies_killed += 1 # Adds to the enemies killed count
                    update_enemy_texts() # Updates the enemies text
        for enemy in enemies_alive: # Loops through all alive enemies
            enmdmg(player, healthbar, enemy) # Handles enemy damaging the player

def instructions():
     """Initialises the instructions menu for the game, showing the user how to play the game and the controls."""
     tutorial_bg = Entity(parent=camera.ui, model='quad', scale=(0.7, 0.5), color=color.dark_gray, z=1)
     maingamemodes = Text("How to play:\n" "Survival Gamemode: Survive waves of enemies and live for as long as you can!\n" "Freeplay Gamemode: Spawn enemies with the E key, use different guns, and simulate FPS!\n" "Exit: Exits the game (See ya!)", parent=tutorial_bg, position=(-0.85, 0.25), scale=1.75, color=color.white)
     maincontrols = Text("Main Controls:\n" "WASD: Move the player around!\n" "Left mouse button: Shoot the gun!\n" "Shift: Sprint like the wind!\n" "E Key (Only in Freeplay): Spawns Enemies!", parent=tutorial_bg, position=(-0.85, -0.25), scale=1.75, color=color.white)
     exit_button = Button(text="Exit", parent=tutorial_bg, position=(-1.1, 0.91), scale=(0.1, 0.05), color=color.red, on_click= lambda: (destroy(maincontrols), destroy(maingamemodes), destroy(tutorial_bg), destroy(exit_button), menu(start_game, survival_game, instructions)))


# Calls the menu function, fullscreen, and runs the game
app = Ursina(fullscreen=True)
menu(start_game, survival_game, instructions)
app.run()

```
***
## Review
1. Judging by my newly made functional and non-functional requirements, Sprint 2 successfully meets the majority outlined in my documentation. The game provides a visible gun, crosshair, healthbar, and allows the player to move, shoot and spawn enemies as specified. A UI menu has also been incorporated for the gamemodes, and the tutorial, which are highly accessible, meeting user interaction requirements. Non-functional requirements such as performance and reliability are also addressed, as the game loads quickly, runs smoothly, and includes error handling in all major functions to prevent crashing. There are clear controls and instructions provided, and the UI updates in real time to reflect game state changes. Furthermore, the project is exponentially successful in aligning with functional and non-functional requirements from the last sprint, meeting the planned criteria and expectations.

2. The program performs well against the modified use-cases identified. When the game is launched, users are greeted with a menu and can easily navigate to different gamemodes or the tutorial. Many functionalities in the use case process such as picking up the gun, shooting, and spawning enemies all work as intended. UI elements such as the healthbar and enemy counters also update correctly, however the game can be enhanced if the user is directed to the menu after ingame death rather than breaking from the ingame loop. The program behaves as expected for most of the use-case, however it would be enhanced if the score was outputted to the user and they were prompted back to the main menu after death.

3. The code demonstrates good readability and maintainability. Functions and classes are modularized from the main gameflow, and docstrings and comments explain their purpose. Error handling is robustly applied for each function, allowing for debugging to be made easier. The structure in both the main.py and module.py also enhanced structure and makes future modifications straightforward. Overall, the code is clean, well documented, and easy to maintain.

4. Several improvements can be made in Sprint 3. As I have already implemented OOP fundamentals, the next sprint will be mostly about adding more features and organising code. Feature-wise, adding more weapons, enemies, and a gameover screen (May or may not be possible) would allow for gameplay variety and user engagement. These enhancements will allow for a polished, feature-complete product, and will pave the way for models and possibly shaders to be implemented.

***

# Sprint 3
***
## Design
***
## Build and Test
***
### Sprint 3 Ursina FPS Game with more features, already containing classes and also added functions as class methods
***

- Sprint3README
```python
# Year 11 Accelerated Software Engineering Assessment Task 2 FPS Game - Sprint 3

### Author
Ronen Gupta

## Features

- Main Menu: Choose between 4 choices, Survival, Free Play, View the Tutorial, or exit the game.
- Survival Mode: Standard survival FPS gameplay, with hookshots and enemies, survive for as long as you can!
- Free Play Mode: Try spawning enemies of your own and try guns! (Added the minigun and the shotgun)
- Tutorial: View the controls for the gamemodes.
- Exit: Exit the game.

## Requirements

- To run this program, you need to install the following dependencies:
- Python 3.8 or higher
- [Ursina Engine](https://www.ursinaengine.org/)

### Install dependencies
To install the required dependencies, you can run:

```bash
pip install -r requirements.txt
```
- Sprint3Module.py
```python
from ursina import * # Ursina library
import random # Random library
from ursina.prefabs.first_person_controller import FirstPersonController # First Person Controller from Ursina
from ursina.prefabs.health_bar import HealthBar # Health Bar from Ursina

def random_spawn_enemy(player):
    """Spawns enemies at random positions within a specified range (-50 to 50 on x and z axes)."""
    try:
        x = random.uniform(-50, 50) # Random x-coordinate
        z = random.uniform(-50, 50) # Random z-coordinate
        enemy = Entity(model='cube', color=color.blue, collider = 'box', scale = (1, 2, 1), position=(x, 1, z), health=100) # Creates an enemy at a random position
        enemy.add_script(GroundedSmoothFollow(target=player, offset=[0, 0, 0], speed=10)) # Adds a script to follow the player using GroundedSmoothFollow
        return enemy # Returns the created enemy entity
    except Exception as e: # Error handling
        print(f"Error spawning random enemy: {e}")

# Spawn Enemy function
def spawn_enemy(player):
    """Function to spawn an enemy at a given position with specified properties."""
    try:
        enemy = Entity(model='cube', color=color.blue, collider = 'box', scale = (1, 2, 1), position=(5, 1, 5), health=100) # Creates an enemy entity
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
            self.position = Vec3(0,-.75,.5) # Sets the position of the new gun relative to the camera
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
            self.position = Vec3(0,-.75,.5) # Sets the position of the new gun relative to the camera
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
```
- Sprint3.py
```python
from ursina import * # Ursina Library
from Sprint3Module import Gun, Shotgun, Minigun, Player, menu, spawn_enemy, random_spawn_enemy # Importing function from my Sprint3Module
import random # Import random for spawning enemies randomly

enemies_alive = [] # List to keep track of alive enemies
enemies_killed = 0 # Variable to keep track of killed enemies
time_elapsed = 0 # Variable to keep track of time elapsed in survival mode

def start_game():
    """Initialises the simulator gamemode, where the player can spawn enemies and shoot them, as well as use a hookshot."""

    global ground, input, update # Global variables

    # Sync the game to the monitor's refresh rate, default 60hz to prevent screen tearing
    window.vsync = True

    # Window.borderless helps with mouse movement issues on macOS
    window.borderless = False 

    # Initialises the Player class and the Entity class from the ursina module as ground, as well as the Sky class for the sky
    player = Player()
    ground = Entity(model='plane', collider='box', scale = 128, texture ='grass')
    Sky()

    # Gives the player no gun at the start, initialises 3 guns
    player.gun = None
    gun = Gun(model='assets/gun.obj', color=color.gold, position=(3,0,3), scale=(.4,.4,.2))
    gun.on_click = lambda: gun.get_gun(player)

    shotgun = Shotgun(model='assets/gun.obj', color=color.gold, position=(5, 0, 3), scale=(.4,.4,.2))
    shotgun.on_click = lambda: shotgun.get_gun(player)

    minigun = Minigun(model = 'assets/gun.obj', color=color.gray, position=(7, 0, 3), scale=(.4,.4,.2))
    minigun.on_click = lambda: minigun.get_gun(player)

    # Makes a hookshot allowing the player to traverse better
    hookshot_target = Button(parent=scene, model='cube', color=color.brown, position=(4,5,5))
    hookshot_target.on_click = Func(player.animate_position, hookshot_target.position, duration=.5, curve=curve.out_quad)

    # Text that shows the user the number of enemies currently alive and killed
    enemies_text = Text(text = f'Enemies Killed: {enemies_killed} | Enemies Alive: {len(enemies_alive)}', position = (0, 0.45), scale = 1, color = color.white)

    def update_enemy_texts():
        """Updates the enemies text to show the number of enemies killed and alive."""
        enemies_text.text = f'Enemies Killed: {enemies_killed} | Enemies Alive: {len(enemies_alive)}' # Updates the enemies text

    def update():
        """Updates the conditional statement of hitting an enemy or not every frame"""
        for enemy in enemies_alive: # Loops through all alive enemies
            if player.intersects(enemy).hit: # If the player hits any
                player.enmdmg(1) # Damages the player by 1 

    # Handles other input required functions such as sprinting, shooting
    def input(key):
        global enemies_killed, enemies_alive
        """Function that handles the main input for the game, such as sprinting, shooting, and player/enemy damage."""
        player.sprint(key) # Sprint function
        player.override() # Prevents jumping when not grounded
        if player.gun: # If the player has a gun
            if isinstance(player.gun, Minigun) and held_keys['left mouse']: # If the gun is from the minigun class and the left mouse button is held down
                if player.gun.shoot(): # If the player successfully shoots
                    for enemy in enemies_alive[:]: # Loops through all alive enemies
                        if player.plrdmg(enemy, player.gun.damage): # Checks if the player kills the enemy
                            enemies_alive.remove(enemy) # Removes the enemy from the alive list
                            enemies_killed += 1 # Adds to the enemies killed count
                            update_enemy_texts() # Updates the enemies text
            elif key == 'left mouse down': # If the player only presses left mouse down once
                if player.gun.shoot(): # If the player successfully shoots
                    for enemy in enemies_alive[:]: # Loops through all alive enemies (Copy of the existing list)
                        if player.plrdmg(enemy, player.gun.damage): # Checks if the player kills the enemy
                            enemies_alive.remove(enemy) # Removes the enemy from the alive list
                            enemies_killed += 1 # Adds to the enemies killed count
                            update_enemy_texts() # Updates the enemies text
        if key == 'e': # Checks if the E key is pressed
            enemy = spawn_enemy(player) # Spawns an enemy
            enemies_alive.append(enemy) # Adds the enemy to the alive list
            update_enemy_texts() # Updates the enemies text

def survival_game():
    """Initialises the survival gamemode, where the player must survive for as long as possible against endless waves of enemies."""
    global ground, input, time_elapsed, update, gun

    # Sync the game to the monitor's refresh rate, default 60hz to prevent screen tearing
    window.vsync = True

    # Initialises the program to be defaulted to fullscreen and window.borderless helps with mouse movement issues on macOS
    window.borderless = False 

    # Time elapsed variable
    time_elapsed = 0

    # Initialises the Player class and the Entity class from the ursina module as ground, as well as the Sky class for the sky
    player = Player()
    ground = Entity(model='plane', collider='box',scale = 128, texture ='grass')
    Sky()

    # Initialises the player having a gun and makes a gun from the Button class and calls the get_gun function instantly
    gun = Gun(model='assets/gun.obj', color=color.gold, position=(3,0,3), scale=(.4,.4,.2))
    gun.on_click = lambda: gun.get_gun(player)

    # Makes a hookshot from the inbuilt ursina.prefabs.first_person_controller module as well as the functions
    hookshot_target = Button(parent=scene, model='cube', color=color.brown, position=(4,5,5))
    hookshot_target.on_click = Func(player.animate_position, hookshot_target.position, duration=.5, curve=curve.out_quad)

    # Enemies text which tracks the enemies killed and alive
    enemies_text = Text(text = f'Enemies Killed: {enemies_killed} | Enemies Alive: {len(enemies_alive)}', position = (0, 0.45), scale = 1, color = color.white)

    # Function that updates the enemies text
    def update_enemy_texts():
        """Updates the enemies text to show the number of enemies killed and alive."""
        enemies_text.text = f'Enemies Killed: {enemies_killed} | Enemies Alive: {len(enemies_alive)}'

    # Time text that tracks the elapsed time when the survival gamemode is selected
    time_text = Text(text = f'Elapsed Time: {int(time_elapsed)}', position = (0.5, 0.45), scale=1, color= color.white)

    # Updates the time elapsed per frame and the text
    def update_time_elapsed_texts():
        """Updates the elapsed time to show the time elapsed"""
        global time_elapsed
        time_elapsed += time.dt
        time_text.text = f'Elapsed time: {int(time_elapsed)}'

    # Spawns the shotgun and minigun when called
    def spawn_shotgun():
            shotgun = Shotgun(model='assets/gun.obj', color=color.gold, position=(3,0,3), scale=(.4,.4,.2))
            shotgun.on_click = lambda: shotgun.get_gun(player)
    
    def spawn_minigun():
            minigun = Minigun(model = 'assets/gun.obj', color=color.gray, position=(7, 0, 3), scale=(.4,.4,.2))
            minigun.on_click = lambda: minigun.get_gun(player)

    # Spawns both guns at a set amount of time by calling the individual functions
    invoke(spawn_shotgun, delay = 200)
    invoke(spawn_minigun, delay = 500)

    # Spawns enemies randomly and adds them to a list, and tracks the alive enemies
    def spawn_enemies_randomly():
        """Spawns enemies randomly and adds them to the enemies_alive list."""
        enemy = random_spawn_enemy(player)
        enemies_alive.append(enemy)
        update_enemy_texts()
        invoke(spawn_enemies_randomly, delay=random.uniform(5, 12))

    # Calls the function
    spawn_enemies_randomly()

    # Updates the time every frame, using the unique update function in Ursina
    def update():
        update_time_elapsed_texts()
        for enemy in enemies_alive: # Loops through all alive enemies
            if player.intersects(enemy).hit:
                player.enmdmg(1)


    # Controls the main input functions of the game
    def input(key):
        global enemies_killed, enemies_alive
        """Function that handles the main input for the game, such as sprinting, shooting, and player/enemy damage."""
        player.sprint(key) # Sprint function
        player.override() # Prevents jumping when not grounded
        if player.gun: # Checks if the player has a gun
            if isinstance(player.gun, Minigun) and key == held_keys['left mouse']: # If the gun is from the minigun class and the left mouse button is held down
                if player.gun.shoot(): # If the player successfully shoots the gun
                    for enemy in enemies_alive[:]: # Loops through all alive enemies in a copy of the original list
                        if player.plrdmg(enemy, player.gun.damage): # Checks if the player kills the enemy
                            enemies_alive.remove(enemy) # Removes the enemy from the alive list
                            enemies_killed += 1 # Adds to the enemies killed count
                            update_enemy_texts() # Updates the enemies text
                        
            elif key == 'left mouse down': # Checks if the player has a gun
                if player.gun.shoot(): 
                    for enemy in enemies_alive[:]: # Loops through all alive enemies
                        if player.plrdmg(enemy, player.gun.damage): # Checks if the player kills the enemy
                            enemies_alive.remove(enemy) # Removes the enemy from the alive list
                            enemies_killed += 1 # Adds to the enemies killed count
                            update_enemy_texts() # Updates the enemies text

def instructions():
     """Initialises the instructions menu for the game, showing the user how to play the game and the controls."""
     tutorial_bg = Entity(parent=camera.ui, model='quad', scale=(0.7, 0.5), color=color.dark_gray, z=1)
     maingamemodes = Text("How to play:\n" "Survival Gamemode: Survive waves of enemies and live for as long as you can!\n" "Freeplay Gamemode: Spawn enemies with the E key, use different guns, and simulate FPS!\n" "Exit: Exits the game (See ya!)", parent=tutorial_bg, position=(-0.85, 0.25), scale=1.75, color=color.white)
     maincontrols = Text("Main Controls:\n" "WASD: Move the player around!\n" "Left mouse button: Shoot the gun!\n" "Shift: Sprint like the wind!\n" "E Key (Only in Freeplay): Spawns Enemies!", parent=tutorial_bg, position=(-0.85, -0.25), scale=1.75, color=color.white)
     exit_button = Button(text="Exit", parent=tutorial_bg, position=(-1.1, 0.91), scale=(0.1, 0.05), color=color.red, on_click= lambda: (destroy(maincontrols), destroy(maingamemodes), destroy(tutorial_bg), destroy(exit_button), menu(start_game, survival_game, instructions)))


# Calls the menu function, fullscreen, and runs the game
app = Ursina(fullscreen=True)
menu(start_game, survival_game, instructions)
app.run()
```
***
## Review
1. The project sincerely performs well against the non-functional and functional requirements. From the previous sprint, I have only added a feature and finished most of the logic in the game. Maintaining no bugs or issues, and keeping the quality of the previous sprint, Sprint 3 clearly demonstrates its already implemented use of OOP, and also other features added, from the demand of other gun choices as well, including the shotgun and the minigun. As I have included these features and maintained performance from the previous sprint, this sprint maintains expectations.

2. The program maintains equality similar to my provided use case. In relation to Sprint 2, it would follow the same flow except there would be the inclusion of multiple other guns which the user could choose from. Additionally, I added a note in my use case possibly deferring the use of the gameover screen, as Ursina has trouble deleting all gameplay elements and maintaining certain aspects of the game. When I tried this before, the game would simply keep running even after destroying most elements, which led me to believe it would be difficult to implement a feature like so. For this reason, I added a note dictating that it may or may not be possible to implement such a feature. However, everything else remains the same.

3. The code demonstrates good readability and maintainability. Classes are not only modularized from the main gameflow, but also included inside these classes are functions which I implemented into these class methods for readability and to avoid cluttering, as well as future maintainability. Docstrings and comments explain the purpose of each method inside the classes. From Sprint 2, error handling remains the same. Overall, the code is clean, well documented, and easy to maintain.

4. Several improvements can be made in Sprint 4. As I have already implemented OOP fundamentals and also added many features regarding game logic, the next sprint will be mostly about touch-ups and another feature to enhance the players experience: Shaders and/or proper models. This would allow for user engagement. These enhancements will allow for a polished, complete product incorporating both logic and creativity.
