from ursina import * # Ursina Library
from Sprint4Module import Gun, Shotgun, Minigun, Player, HealthPack, menu, spawn_enemy, random_spawn_enemy # Importing classes and functions from my Sprint4Module
import random # Import random for spawning enemies randomly

enemies_alive = [] # List to keep track of alive enemies
healthpacks_alive = [] # List to keep track of healthpacks spawned
enemies_killed = 0 # Variable to keep track of killed enemies
time_elapsed = 0 # Variable to keep track of time elapsed in survival mode

def start_game():
    """Initialises the simulator gamemode, where the player can spawn enemies and shoot them, as well as use a hookshot."""

    global ground, input, update, border_bottom, border_top, border_left, border_right # Global variables

    # Sync the game to the monitor's refresh rate, default 60hz to prevent screen tearing
    window.vsync = True

    # Window.borderless helps with mouse movement issues on macOS
    window.borderless = False 

    # Initialises the Player class and the Entity class from the ursina module as ground, as well as the Sky class for the sky
    player = Player()
    ground = Entity(model='plane', collider='box', scale = 128, texture ='grass')
    border_top = Entity(model='cube', scale=(128, 10, 1), position=(0, 5, 64), collider='box', visible=False)
    border_bottom = Entity(model='cube', scale=(128, 10, 1), position=(0, 5, -64), collider='box', visible=False)
    border_left = Entity(model='cube', scale=(1, 10, 128), position=(-64, 5, 0), collider='box', visible=False)
    border_right = Entity(model='cube', scale=(1, 10, 128), position=(64, 5, 0), collider='box', visible=False)
    Sky()

    # Gives the player no gun at the start, initialises 3 guns
    player.gun = None
    gun = Gun(model='assets/glock.obj', color=color.gray, position=(3,1,3), scale=(.2,.2,.1))
    gun.on_click = lambda: gun.get_gun(player)

    shotgun = Shotgun(model='assets/gun.obj', color=color.gold, position=(5, 1, 3), scale=(.4,.4,.2))
    shotgun.on_click = lambda: shotgun.get_gun(player)

    minigun = Minigun(model = 'assets/Minigun_.obj', color=color.gray, position=(7, 1, 3), scale=(.05,.05,.025))
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
        for healthpack in healthpacks_alive[:]:
             if healthpack.intersects(scene.player).hit:
                if healthpack.heal():
                    healthpacks_alive.remove(healthpack)

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
        if key == 'r':
            healthpack = HealthPack(position=(8, 1, 5))
            healthpacks_alive.append(healthpack)

def survival_game():
    """Initialises the survival gamemode, where the player must survive for as long as possible against endless waves of enemies."""
    global ground, input, time_elapsed, update, gun, border_bottom, border_top, border_left, border_right

    # Sync the game to the monitor's refresh rate, default 60hz to prevent screen tearing
    window.vsync = True

    # Initialises the program to be defaulted to fullscreen and window.borderless helps with mouse movement issues on macOS
    window.borderless = False 

    # Time elapsed variable
    time_elapsed = 0

    # Initialises the Player class and the Entity class from the ursina module as ground, as well as the Sky class for the sky
    player = Player()
    ground = Entity(model='plane', collider='box',scale = 128, texture ='grass')
    border_top = Entity(model='cube', scale=(128, 10, 1), position=(0, 5, 64), collider='box', visible=False)
    border_bottom = Entity(model='cube', scale=(128, 10, 1), position=(0, 5, -64), collider='box', visible=False)
    border_left = Entity(model='cube', scale=(1, 10, 128), position=(-64, 5, 0), collider='box', visible=False)
    border_right = Entity(model='cube', scale=(1, 10, 128), position=(64, 5, 0), collider='box', visible=False)
    Sky()

    # Initialises the player having a gun and makes a gun from the Button class and calls the get_gun function instantly
    gun = Gun(model='assets/glock.obj', color=color.gray, position=(3,0,3), scale=(.2,.2,.2))
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
            minigun = Minigun(model = 'assets/Minigun_.obj', color=color.gray, position=(7, 0, 3), scale=(.4,.4,.2))
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
        invoke(spawn_enemies_randomly, delay=random.uniform(1, 7))

    # Calls the function
    spawn_enemies_randomly()

    def spawn_healthpack_randomly():
        """Spawns healthpacks randomly and adds them to the healthpacks_alive list."""
        x = random.uniform(-50, 50) # Random x-coordinate
        z = random.uniform(-50, 50) # Random z-coordinate
        healthpack = HealthPack(position=(x, 1, z))
        healthpacks_alive.append(healthpack)
        invoke(spawn_healthpack_randomly, delay=random.uniform(10, 20))

    # Calls the function
    spawn_healthpack_randomly()

    # Updates the time every frame, using the unique update function in Ursina
    def update():
        update_time_elapsed_texts()
        for enemy in enemies_alive[:]: # Loops through all alive enemies
            if player.intersects(enemy).hit:
                player.enmdmg(1)
        for healthpack in healthpacks_alive[:]:
            if healthpack.intersects(scene.player).hit:
                if healthpack.heal():
                    healthpacks_alive.remove(healthpack)


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
     maingamemodes = Text("How to play:\n" "Survival Gamemode: Survive waves of enemies and live for as long as you can!\n" "Freeplay Gamemode: Spawn enemies with the E key\n or spawn health packs with the R key,\n use different guns, and simulate FPS!\n" "Exit: Exits the game (See ya!)", parent=tutorial_bg, position=(-0.85, 0.25), scale=1.75, color=color.white)
     maincontrols = Text("Main Controls:\n" "WASD: Move the player around!\n" "Left mouse button: Shoot the gun!\n" "Shift: Sprint like the wind!\n" "E Key (Only in Freeplay): Spawns Enemies!\n" "R Key (Only in Freeplay): Spawns Health Packs!", parent=tutorial_bg, position=(-0.85, -0.25), scale=1.75, color=color.white)
     exit_button = Button(text="Exit", parent=tutorial_bg, position=(-1.1, 0.91), scale=(0.1, 0.05), color=color.red, on_click= lambda: (destroy(maincontrols), destroy(maingamemodes), destroy(tutorial_bg), destroy(exit_button), menu(start_game, survival_game, instructions)))


# Calls the menu function, fullscreen, and runs the game
app = Ursina(fullscreen=True)
menu(start_game, survival_game, instructions)
app.run()

