import random
import json
import os

from pico2d import *
import game_framework
import game_world

import start_state

#import enemis
import pause_sate
from player import Player

name = "MainState"

player=None
#Enemis=None


def enter():
   global player,Enemis
   global bullets
   player=Player()
   #Enemis = [enemis.Enemy() for i in range(100)]
   #bullets = [Bullet() for i in range(11)]
   game_world.add_object(player,1)
   #game_world.add_object(Enemis,1)



def exit():
    # del(player)
    # del(Enemis)
    # del(bullets)
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
           #Enemis.handle_event(event)






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
