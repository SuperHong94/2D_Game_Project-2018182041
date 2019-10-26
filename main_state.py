import random
import json
import os

from pico2d import *

import game_framework

import start_state

#import title_state

import pause_sate


name = "MainState"

boy = None
grass = None
font = None
player=None




class Player:
    def __init__(self):
        self.image=load_image('resource/player.png')
        self.image.

        pass

    def update(self):

        pass

    def draw(self):
        self.image.clip_draw(0,0,100,100,400,400)
        pass

def enter():
   ''' global boy,grass
    grass=Grass()'''
   global player
   player=Player()



def exit():
    #global boy,grass
    #del(boy)
    #del(grass)
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
            print("ahffk")
            #game_framework.change_state(title_state)
        elif event.type==SDL_KEYDOWN and event.key==SDLK_p:
            game_framework.push_state(pause_sate)
    pass


def update():
    pass


def draw():
    clear_canvas()
    player.draw()
    update_canvas()

    pass





