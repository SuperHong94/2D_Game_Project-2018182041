import random
import json
import os

from pico2d import *
import game_framework
import game_world

from player import Player
import start_state

#import title_state
import enemis
import pause_sate


name = "MainState"

font = None
player=None
Enemis=None
i=0


class Bullet:
    image=None
    def __init__(self):
        if Bullet.image==None:
            Bullet.image=load_image('resource/bullet.png')
        self.x,self.y=player.x,player.y+10
        self.being=False
        self.speed=1
    def draw(self):
        if self.being==True:
            Bullet.image.clip_draw(0,0,7,7,self.x,self.y)
    def update(self):
        if self.being==True:
            if(self.y<get_canvas_height()+100):
                self.y+=self.speed
            else:
                self.x, self.y = player.x, player.y+10
                self.being=False
        else:
            self.x, self.y = player.x, player.y + 10


def enter():
   global player
   player.Player()
   game_world.add_object(player,1)




def exit():
    game_world.clear()
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            game_framework.quit()
        else:
            player.handle_event(event)

    pass




def update():
    for game_object in game_world.all_objects():
        game_object.update()
    pass


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

    pass
