from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
window.vsync = False
__name__ == '__main__'
app = Ursina(fullscreen = True)
player = FirstPersonController(model='cube', color=color.clear, speed = 20, scale_y=2)
ground = Entity(model='plane', collider='box',scale = 128, texture ='grass')
Sky()

def Sprint():
    if held_keys['shift']:
        print("Shift")

player.gun = None


gun = Button(parent=scene, model='assets/gun.obj', color=color.gold, origin_y=-.5, position=(3,0,3), collider='box', scale=(.4,.4,.2))
def get_gun():
        gun.parent = camera
        gun.position = Vec3(0,-.75,.5)
        player.gun = gun
gun.on_click = get_gun


hookshot_target = Button(parent=scene, model='cube', color=color.brown, position=(4,5,5))
hookshot_target.on_click = Func(player.animate_position, hookshot_target.position, duration=.5, curve=curve.linear)

def input(key):
        if key == 'left mouse down':
            Audio("assets/laser_sound.wav")
            gun.blink(color.red)
            bullet = Entity(parent=gun, model='cube', scale=.6, color=color.black)
            bullet.world_parent = scene
            bullet.animate_position(bullet.position+(bullet.forward*3000), curve=curve.linear, duration=0.5)
            destroy(bullet, delay=0.5)


Sprint()
app.run()