from pico2d import *

import game_world
import main_state
class Explosion:
    image = None

    def __init__(self,x,y):
        if Explosion.image is None:
            self.image = load_image('resource/explosion.png')

        self.x, self.y = x, y
        self.Xframe = 0
        self.Yframe = 0
        self.size = 64
        self.timer=0

    def draw(self):
        self.image.clip_draw(self.size * self.Xframe, self.size * self.Yframe, self.size, self.size, self.x, self.y)

    def update(self):
        if self.timer>20:
            game_world.remove_object(self)
        if self.Xframe < 4:
            self.Xframe += 1
        else:
            self.Yframe += 1
            self.Xframe = 0
        self.timer+=1