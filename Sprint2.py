from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar
from Sprint2Module import get_gun, sprint, shoot, enmdmg, override, plrdmg, menu, spawn_enemy, random_spawn_enemy
import random

enemies_alive = []
enemies_killed = 0
time_elapsed = 0

def start_game():

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

    # Initialises the player having no gun and makes a gun from the Button class and calls the get_gun function
    player.gun = None
    gun = Button(parent=scene, model='assets/gun.obj', color=color.gold, origin_y=-.5, position=(3,0,3), scale=(.4,.4,.2))
    gun.on_click = lambda: get_gun(player, gun)

    # Makes a hookshot as a test from the inbuilt ursina.prefabs.first_person_controller module as well as the functions
    hookshot_target = Button(parent=scene, model='cube', color=color.brown, position=(4,5,5))
    hookshot_target.on_click = Func(player.animate_position, hookshot_target.position, duration=.5, curve=curve.out_quad)

    enemies_text = Text(text = f'Enemies Killed: {enemies_killed} | Enemies Alive: {len(enemies_alive)}', position = (0, 0.45), scale = 1, color = color.white)

    def update_enemy_texts():
        """Updates the enemies text to show the number of enemies killed and alive."""
        enemies_text.text = f'Enemies Killed: {enemies_killed} | Enemies Alive: {len(enemies_alive)}'

    # Handles other functions such as sprinting, shooting, enemy damaging, and an override function to prevent buggy player
    def input(key):
        global enemies_killed, enemies_alive
        """Function that handles the main input for the game, such as sprinting, shooting, and player/enemy damage."""
        sprint(player, key)
        override(player)
        if player.gun == gun:
            shoot(gun, key)
        if key == 'left mouse down':
            for enemy in enemies_alive:
                if plrdmg(player, enemy):
                    enemies_alive.remove(enemy)
                    enemies_killed += 1
                    update_enemy_texts()
        if key == 'e':
            enemy = spawn_enemy(player)
            enemies_alive.append(enemy)
            update_enemy_texts()
        for enemy in enemies_alive:
            enmdmg(player, healthbar, enemy)

def survival_game():

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

    # Initialises the player having no gun and makes a gun from the Button class and calls the get_gun function
    gun = Button(parent=scene, model='assets/gun.obj', color=color.gold, origin_y=-.5, position=(3,0,3), scale=(.4,.4,.2))
    player.gun = gun
    get_gun(player, gun)

    # Makes a hookshot as a test from the inbuilt ursina.prefabs.first_person_controller module as well as the functions
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
        sprint(player, key)
        override(player)
        if player.gun == gun:
            shoot(gun, key)
        if key == 'left mouse down':
            for enemy in enemies_alive[:]:
                if plrdmg(player, enemy):
                    enemies_alive.remove(enemy)
                    enemies_killed += 1
                    update_enemy_texts()
        for enemy in enemies_alive:
            enmdmg(player, healthbar, enemy)

def instructions():
     tutorial_bg = Entity(parent=camera.ui, model='quad', scale=(0.7, 0.5), color=color.dark_gray, z=1)
     maingamemodes = Text("How to play:\n" "Survival Gamemode: Survive waves of enemies and live for as long as you can!\n" "Freeplay Gamemode: Spawn enemies with the E key, use different guns, and simulate FPS!\n" "Exit: Exits the game (See ya!)", parent=tutorial_bg, position=(-0.85, 0.25), scale=1.75, color=color.white)
     maincontrols = Text("Main Controls:\n" "WASD: Move the player around!\n" "Left mouse button: Shoot the gun!\n" "Shift: Sprint like the wind!\n" "E Key (Only in Freeplay): Spawns Enemies!", parent=tutorial_bg, position=(-0.85, -0.25), scale=1.75, color=color.white)
     exit_button = Button(text="Exit", parent=tutorial_bg, position=(-1.1, 0.91), scale=(0.1, 0.05), color=color.red, on_click= lambda: (destroy(maincontrols), destroy(maingamemodes), destroy(tutorial_bg), destroy(exit_button), menu(start_game, survival_game, instructions)))


# Calls the menu function, fullscreen, and runs the game
app = Ursina(fullscreen=True)
menu(start_game, survival_game, instructions)
app.run()

