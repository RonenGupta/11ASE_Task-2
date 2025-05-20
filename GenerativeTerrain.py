from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
app = Ursina()
player = FirstPersonController(model='cube', color=color.orange, scale_y=2, speed = 20, height = 100)
Sky()

cube = Entity(model = 'cube', collider = 'mesh', texture= 'grass')
terrain_width = 40
noise = PerlinNoise(octaves=1, seed=92324097)
freq = 4
amp = 6
for i in range(terrain_width*terrain_width):
    cube = Entity(model = 'cube', collider = 'mesh', texture= 'grass')
    cube.x = floor(i/terrain_width)
    cube.z = floor(i%terrain_width)
    cube.y = floor(noise([cube.x/freq, cube.z/freq])*amp)
app.run()