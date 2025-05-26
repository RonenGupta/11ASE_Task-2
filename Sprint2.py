from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar
from Sprint2Module import get_gun, sprint, shoot, enmdmg

# Sync the game to the monitor's refresh rate, default 60hz to prevent screen tearing
window.vsync = False

# Initialises the program to be defaulted to fullscreen
app = Ursina(fullscreen = True)

# Initialises the FirstPersonController class from the inbuilt ursina.prefabs.first_person_controller module as player, 
# and the Entity class from the ursina module as ground, as well as the sky class and healthbar from the ursina.prefabs.health_bar module as HealthBar.
player = FirstPersonController(model='cube', color=color.clear, speed = 10, scale_y=2, collider='box')
healthbar = HealthBar(bar_color = color.lime.tint(-.25), roundness=.5, highlight_color = color.yellow.tint(-.2))
ground = Entity(model='plane', collider='box',scale = 128, texture ='grass')
Sky()

# Initialises the player having no gun and makes a gun from the Button class and calls the get_gun function
player.gun = None
gun = Button(parent=scene, model='assets/gun.obj', color=color.gold, origin_y=-.5, position=(3,0,3), collider='box', scale=(.4,.4,.2))
gun.on_click = lambda: get_gun(player, gun)

# Makes a hookshot as a test from the inbuilt ursina.prefabs.first_person_controller module as well as the functions
hookshot_target = Button(parent=scene, model='cube', color=color.brown, position=(4,5,5))
hookshot_target.on_click = Func(player.animate_position, hookshot_target.position, duration=.5, curve=curve.out_quad)

# Add an example enemy that follows the player using the SmoothFollow class
enemy = Entity(model='cube', color=color.red, collider = 'box')
enemy.add_script(SmoothFollow(target=player, offset=[0, 0, 0], speed=1))

# Handles other functions such as sprinting and shooting from other module
def input(key):
    sprint(player, key)
    shoot(gun, key)
    enmdmg(player, healthbar, enemy)

# Runs the program
app.run()