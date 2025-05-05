from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
window.vsync = False
app = Ursina()
player = FirstPersonController(model='cube', color=color.clear, speed = 20, scale_y=2)
ground = Entity(model='plane', collider='box',scale = 128, texture ='grass')
Sky()

def Sprint():
    if held_keys['shift']:
        print("Shift")

Sprint()
app.run()